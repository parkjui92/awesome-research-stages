#!/usr/bin/env python3
"""data/repos.json 에서 README.md 를 생성한다. 스타 수·최근 푸시일은 GitHub API로 새로 받는다.

사용: GITHUB_TOKEN=... python3 scripts/build_readme.py
토큰이 없어도 동작하지만 비인증 한도(시간당 60회)에 걸릴 수 있다.
"""
import datetime as dt
import json
import os
import pathlib
import ssl
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "repos.json"
README = ROOT / "README.md"
STALE_DAYS = 365

try:  # python.org 배포판 macOS 파이썬은 시스템 인증서를 못 읽는 경우가 있다
    import certifi
    SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    SSL_CTX = ssl.create_default_context()


def fetch(full_name):
    req = urllib.request.Request(f"https://api.github.com/repos/{full_name}")
    req.add_header("Accept", "application/vnd.github+json")
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=20, context=SSL_CTX) as r:
        d = json.load(r)
    return {
        "full_name": d["full_name"],
        "stars": d["stargazers_count"],
        "pushed": d["pushed_at"][:10],
        "archived": d.get("archived", False),
    }


def fmt_stars(n):
    return f"{n / 1000:.1f}k" if n >= 1000 else str(n)


def render_table(repos, today):
    rows = ["| 레포 | ★ | 최근 푸시 | 용도 |", "|---|---:|---|---|"]
    for r in sorted(repos, key=lambda x: -x["stars"]):
        pushed = r["pushed"]
        age = (today - dt.date.fromisoformat(pushed)).days
        flag = ""
        if r["archived"]:
            flag = " 🗄️"
        elif age > STALE_DAYS:
            flag = " 💤"
        rows.append(
            f"| [{r['full_name']}](https://github.com/{r['full_name']}) "
            f"| {fmt_stars(r['stars'])} | {pushed}{flag} | {r['note']} |"
        )
    return "\n".join(rows)


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    today = dt.date.today()
    failed = []
    total = 0

    parts = []
    toc = []
    for stage in data["stages"]:
        toc.append(f"- [{stage['title']}](#{stage['id']}) — {stage['subtitle']}")
        sec = [f'<a id="{stage["id"]}"></a>', f"## {stage['title']}", "", f"*{stage['subtitle']}*", ""]
        if stage.get("caveat"):
            sec += [f"> {stage['caveat']}", ""]
        for group in stage["groups"]:
            enriched = []
            for item in group["repos"]:
                try:
                    meta = fetch(item["repo"])
                except Exception as e:  # noqa: BLE001 — 한 레포 실패로 전체를 멈추지 않는다
                    failed.append(f"{item['repo']}: {e}")
                    continue
                enriched.append({**meta, "note": item["note"]})
                total += 1
            if group.get("name"):
                sec += [f"### {group['name']}", ""]
            sec += [render_table(enriched, today), ""]
        parts.append("\n".join(sec))

    header = (ROOT / "scripts" / "header.md").read_text(encoding="utf-8")
    footer = (ROOT / "scripts" / "footer.md").read_text(encoding="utf-8")
    body = "\n".join([
        header.strip(),
        "",
        f"레포 {total}개 · 스타 수 갱신일 **{today.isoformat()}** (GitHub Actions가 매주 자동 갱신)",
        "",
        "## 목차",
        "",
        *toc,
        "",
        *parts,
        footer.strip(),
        "",
    ])
    README.write_text(body, encoding="utf-8")
    print(f"README.md 생성: 레포 {total}개")

    if failed:
        print("조회 실패:", *failed, sep="\n  ", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
