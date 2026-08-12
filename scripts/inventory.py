#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
from pathlib import Path


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a deterministic source-material inventory.")
    parser.add_argument("inputs", nargs="+", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    files: list[Path] = []
    for item in args.inputs:
        if item.is_file():
            files.append(item)
        elif item.is_dir():
            files.extend(path for path in item.rglob("*") if path.is_file() and ".git" not in path.parts)
        else:
            raise SystemExit(f"Input does not exist: {item}")

    rows = []
    for path in sorted(set(path.resolve() for path in files), key=str):
        mime, _ = mimetypes.guess_type(path.name)
        stat = path.stat()
        rows.append({
            "path": str(path),
            "name": path.name,
            "extension": path.suffix.lower(),
            "mime": mime or "application/octet-stream",
            "bytes": stat.st_size,
            "sha256": digest(path),
        })

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps({"count": len(rows), "files": rows}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(rows)} entries to {args.output}")


if __name__ == "__main__":
    main()
