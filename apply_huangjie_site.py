#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Patch al-folio _config.yml for Jie Huang's academic homepage.
Run this file from the root directory of your al-folio repository.
"""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path.cwd()
CONFIG = ROOT / "_config.yml"

SITE_VALUES = {
    "title": '"Jie Huang | 黄婕"',
    "first_name": '"Jie"',
    "middle_name": '""',
    "last_name": '"Huang"',
    "email": '"huangjie2018@ruc.edu.cn"',
    "contact_note": '>',
    "description": '>',
    "keywords": "smart governance, public data governance, data standardization, semantic interoperability, AI data governance, smart cities, information resource management",
    "lang": "en",
    "icon": '"📊"',
    "baseurl": '""',
    "last_updated": "true",
    "bib_search": "true",
    "socials_in_search": "false",
    "posts_in_search": "false",
    "enable_navbar_social": "false",
}

BLOCK_VALUES = {
    "contact_note": "  The best way to reach me is by email.",
    "description": "  Jie Huang is a Lecturer at the School of Smart Governance, Renmin University of China. Her research focuses on smart governance, public data governance, data standardization, semantic interoperability, and AI data governance.",
}

FOOTER_TEXT = (
    "  Powered by [Jekyll](https://jekyllrb.com/) with [al-folio](https://github.com/alshedivat/al-folio) theme. "
    "Hosted by [GitHub Pages](https://pages.github.com/)."
)


def set_top_level_key(text: str, key: str, value: str, block_line: str | None = None) -> str:
    """Set a top-level YAML key while preserving the rest of the config file."""
    pattern = re.compile(rf"(?m)^{re.escape(key)}:\s*.*$")
    replacement = f"{key}: {value}"
    if pattern.search(text):
        text = pattern.sub(replacement, text, count=1)
    else:
        text += f"\n{replacement}\n"
    if value == ">" and block_line:
        # Remove old indented block immediately following key, but only until the next non-indented key.
        # Important: do not use DOTALL here; otherwise a single indented line can consume the rest of _config.yml.
        block_pattern = re.compile(rf"(?m)^{re.escape(key)}:\s*>\s*\n(?:[ \t]+.*(?:\n|$))*")
        text = block_pattern.sub(f"{key}: >\n{block_line}\n", text, count=1)
    return text


def patch_scholar(text: str) -> str:
    # Patch only inside the scholar block. If no scholar block exists, append a minimal one.
    m = re.search(r"(?ms)^scholar:\s*\n.*?(?=^[A-Za-z0-9_\-]+:|\Z)", text)
    if not m:
        return text + "\nscholar:\n  last_name: [Huang, 黄]\n  first_name: [Jie, 婕]\n"
    block = m.group(0)
    if re.search(r"(?m)^\s+last_name:\s*.*$", block):
        block = re.sub(r"(?m)^\s+last_name:\s*.*$", "  last_name: [Huang, 黄]", block, count=1)
    else:
        block = block.rstrip() + "\n  last_name: [Huang, 黄]\n"
    if re.search(r"(?m)^\s+first_name:\s*.*$", block):
        block = re.sub(r"(?m)^\s+first_name:\s*.*$", "  first_name: [Jie, 婕]", block, count=1)
    else:
        block = block.rstrip() + "\n  first_name: [Jie, 婕]\n"
    return text[:m.start()] + block + text[m.end():]


def main() -> None:
    if not CONFIG.exists():
        raise SystemExit("没有找到 _config.yml。请把本脚本放在 al-folio 仓库根目录运行。")

    username = input("请输入 GitHub 用户名，例如 jiehuang-ruc。未确定可直接回车：").strip()
    url = f"https://{username}.github.io" if username else "https://your-github-username.github.io"

    text = CONFIG.read_text(encoding="utf-8")
    backup = CONFIG.with_suffix(".yml.bak_huangjie")
    if not backup.exists():
        backup.write_text(text, encoding="utf-8")

    values = dict(SITE_VALUES)
    values["url"] = f'"{url}"'
    for key, value in values.items():
        block_line = BLOCK_VALUES.get(key)
        text = set_top_level_key(text, key, value, block_line)

    # Footer is a block scalar in most al-folio configs.
    text = set_top_level_key(text, "footer_text", ">", FOOTER_TEXT)
    text = patch_scholar(text)

    CONFIG.write_text(text, encoding="utf-8")
    print("\n已完成 _config.yml 修改。")
    print(f"备份文件：{backup.name}")
    print(f"站点 URL：{url}")
    print("下一步：git add . && git commit -m \"Build Jie Huang academic homepage\" && git push")

if __name__ == "__main__":
    main()
