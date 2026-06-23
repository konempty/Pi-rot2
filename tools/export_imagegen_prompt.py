#!/usr/bin/env python3
"""Export a built-in ImageGen revised prompt from Codex session logs.

This avoids grepping JSONL logs directly, because image_generation_end entries
also contain large base64 PNG payloads.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path


def codex_home() -> Path:
    return Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")).expanduser()


def iter_session_logs() -> list[Path]:
    sessions = codex_home() / "sessions"
    if not sessions.exists():
        return []
    return sorted(sessions.glob("**/*.jsonl"), key=lambda p: p.stat().st_mtime, reverse=True)


def iter_prompt_payloads(logs: list[Path]):
    for log in logs:
        with log.open("r", encoding="utf-8") as fh:
            for line_no, raw in enumerate(fh, 1):
                try:
                    obj = json.loads(raw)
                except json.JSONDecodeError:
                    continue
                payload = obj.get("payload", {})
                if payload.get("type") != "image_generation_end":
                    continue
                prompt = payload.get("revised_prompt", "")
                if not prompt:
                    continue
                yield {
                    "log": log,
                    "line": line_no,
                    "call_id": payload.get("call_id"),
                    "status": payload.get("status"),
                    "revised_prompt": prompt,
                }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True, help="Destination markdown file")
    parser.add_argument("--call-id", help="Specific ImageGen call id to export")
    parser.add_argument("--prompt-contains", help="Only export a prompt containing this text")
    parser.add_argument("--title", help="Markdown title")
    args = parser.parse_args()

    if not args.call_id and not args.prompt_contains:
        raise SystemExit("Use --call-id or --prompt-contains")

    matches = []
    for payload in iter_prompt_payloads(iter_session_logs()):
        if args.call_id and payload["call_id"] != args.call_id:
            continue
        if args.prompt_contains and args.prompt_contains not in payload["revised_prompt"]:
            continue
        matches.append(payload)

    if not matches:
        raise SystemExit("No matching ImageGen prompt payload found")

    matches.sort(key=lambda p: (p["log"].stat().st_mtime, p["line"]), reverse=True)
    payload = matches[0]

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    title = args.title or args.prompt_contains or payload["call_id"] or "ImageGen Prompt"
    body = [
        f"# {title}",
        "",
        f"- image_call_id: `{payload['call_id']}`",
        f"- source: `{payload['log']}:{payload['line']}`",
        f"- status: `{payload['status']}`",
        "",
        "```text",
        payload["revised_prompt"],
        "```",
        "",
    ]
    out.write_text("\n".join(body), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
