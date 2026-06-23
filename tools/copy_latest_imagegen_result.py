#!/usr/bin/env python3
"""Copy the newest built-in ImageGen PNG into the project and validate ratio."""

from __future__ import annotations

import argparse
import os
import shutil
import sys
import time
from pathlib import Path

from PIL import Image


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True, help="Workspace path for copied PNG.")
    parser.add_argument("--after", type=float, default=0.0, help="Only consider files modified after this unix timestamp.")
    parser.add_argument("--target-ratio", type=float, default=817 / 1014)
    parser.add_argument("--max-ratio-delta", type=float, default=0.03)
    parser.add_argument("--generated-root", default=None)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    codex_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
    root = Path(args.generated_root) if args.generated_root else codex_home / "generated_images"
    if not root.exists():
        print(f"generated root does not exist: {root}", file=sys.stderr)
        return 1

    candidates = [
        p
        for p in root.rglob("*.png")
        if p.is_file() and p.stat().st_mtime >= args.after
    ]
    if not candidates:
        print(f"no generated PNG found under {root} after {args.after}", file=sys.stderr)
        return 1

    src = max(candidates, key=lambda p: p.stat().st_mtime)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, out)

    with Image.open(out) as im:
        ratio = im.width / im.height
        delta = abs(ratio - args.target_ratio)
        print(f"copied={out}")
        print(f"source={src}")
        print(f"size={im.width}x{im.height}")
        print(f"ratio={ratio:.6f}")
        print(f"target={args.target_ratio:.6f}")
        print(f"delta={delta:.6f}")
        if delta > args.max_ratio_delta:
            print("ratio check failed", file=sys.stderr)
            return 2

    # Make it easy to see which generation was just consumed.
    print(f"source_mtime={time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(src.stat().st_mtime))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
