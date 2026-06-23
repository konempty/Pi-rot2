#!/usr/bin/env python3
"""Extract a built-in ImageGen PNG result from Codex session logs.

The desktop ImageGen tool can render in chat while the PNG payload is stored in
the session JSONL as image_generation_end.result. This helper saves that payload
into the workspace and reports dimensions for ratio checks.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
from pathlib import Path

try:
    from PIL import Image
except ModuleNotFoundError:  # pragma: no cover - local environment fallback
    Image = None


def codex_home() -> Path:
    return Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")).expanduser()


def iter_session_logs() -> list[Path]:
    sessions = codex_home() / "sessions"
    if not sessions.exists():
        return []
    return sorted(sessions.glob("**/*.jsonl"), key=lambda p: p.stat().st_mtime, reverse=True)


def iter_imagegen_payloads(logs: list[Path]):
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
                result = payload.get("result")
                if not result:
                    continue
                yield {
                    "log": log,
                    "line": line_no,
                    "call_id": payload.get("call_id"),
                    "status": payload.get("status"),
                    "revised_prompt": payload.get("revised_prompt", ""),
                    "result": result,
                }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True, help="Destination PNG path")
    parser.add_argument("--call-id", help="Specific ImageGen call id to extract")
    parser.add_argument("--latest", action="store_true", help="Extract newest available ImageGen payload")
    parser.add_argument("--prompt-contains", help="Only extract a result whose revised prompt contains this text")
    parser.add_argument("--target-ratio", type=float, default=817 / 1014)
    parser.add_argument("--max-ratio-delta", type=float, default=0.03)
    args = parser.parse_args()

    if not args.latest and not args.call_id and not args.prompt_contains:
        raise SystemExit("Use --latest, --call-id, or --prompt-contains")

    matches = []
    for payload in iter_imagegen_payloads(iter_session_logs()):
        if args.call_id and payload["call_id"] != args.call_id:
            continue
        if args.prompt_contains and args.prompt_contains not in payload["revised_prompt"]:
            continue
        matches.append(payload)

    if not matches:
        raise SystemExit("No matching ImageGen result payload found")

    # Logs are newest-first, but payloads inside a log are oldest-first. Pick the
    # newest by log mtime and line number.
    matches.sort(key=lambda p: (p["log"].stat().st_mtime, p["line"]), reverse=True)
    payload = matches[0]

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(base64.b64decode(payload["result"]))

    print(f"saved: {out}")
    print(f"call_id: {payload['call_id']}")
    print(f"log: {payload['log']}:{payload['line']}")
    print(f"status: {payload['status']}")

    if Image is None:
        print("size: unavailable (Pillow is not installed)")
        print("ratio_ok: unchecked")
        return

    with Image.open(out) as im:
        ratio = im.width / im.height
        delta = abs(ratio - args.target_ratio)
        ok = delta <= args.max_ratio_delta
        print(f"size: {im.width}x{im.height}")
        print(f"ratio: {ratio:.4f}")
        print(f"target_ratio: {args.target_ratio:.4f}")
        print(f"ratio_delta: {delta:.4f}")
        print(f"ratio_ok: {str(ok).lower()}")

    if not ok:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
