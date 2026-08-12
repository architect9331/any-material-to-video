#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import wave
from pathlib import Path


def audio_info(path: Path) -> tuple[int, int, int]:
    if path.suffix.lower() != ".wav":
        raise SystemExit(f"Timeline builder accepts WAV segments only: {path}")
    with wave.open(str(path), "rb") as handle:
        if handle.getnchannels() != 1:
            raise SystemExit(f"Expected mono WAV: {path}")
        return handle.getframerate(), handle.getsampwidth(), handle.getnframes()


def main() -> None:
    parser = argparse.ArgumentParser(description="Build an audio-derived timeline and optional concatenated WAV.")
    parser.add_argument("--segments", required=True, type=Path)
    parser.add_argument("--script", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--concat", type=Path)
    parser.add_argument("--gap", type=float, default=.3)
    args = parser.parse_args()

    script = json.loads(args.script.read_text(encoding="utf-8"))
    if not isinstance(script, list) or not script:
        raise SystemExit("Script must be a non-empty JSON array")

    timeline = []
    cursor = 0.0
    sample_rate = sample_width = None
    paths: list[Path] = []
    for index, row in enumerate(script):
        segment_id = row["id"]
        matches = sorted(args.segments.glob(f"{segment_id}.*"))
        if len(matches) != 1:
            raise SystemExit(f"Expected one audio file for {segment_id}, found {len(matches)}")
        path = matches[0]
        rate, width, frames = audio_info(path)
        sample_rate = sample_rate or rate
        sample_width = sample_width or width
        if rate != sample_rate or width != sample_width:
            raise SystemExit("All WAV segments must share sample rate and sample width")
        end = cursor + frames / rate
        timeline.append({"id": segment_id, "start": round(cursor, 3), "end": round(end, 3), "audio": str(path), "text": row["text"]})
        paths.append(path)
        cursor = end + (args.gap if index < len(script) - 1 else 0)

    payload = {"sample_rate": sample_rate, "duration": round(cursor, 3), "gap": args.gap, "segments": timeline}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    if args.concat:
        args.concat.parent.mkdir(parents=True, exist_ok=True)
        assert sample_rate is not None and sample_width is not None
        silence = b"\0" * int(round(args.gap * sample_rate)) * sample_width
        with wave.open(str(args.concat), "wb") as output:
            output.setnchannels(1)
            output.setsampwidth(sample_width)
            output.setframerate(sample_rate)
            for index, path in enumerate(paths):
                with wave.open(str(path), "rb") as source:
                    output.writeframes(source.readframes(source.getnframes()))
                if index < len(paths) - 1:
                    output.writeframes(silence)
    print(json.dumps(payload, ensure_ascii=False))


if __name__ == "__main__":
    main()
