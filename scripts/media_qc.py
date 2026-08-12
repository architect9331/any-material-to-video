#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate final video stream metadata with ffprobe.")
    parser.add_argument("media", type=Path)
    parser.add_argument("--width", type=int)
    parser.add_argument("--height", type=int)
    parser.add_argument("--fps", type=float)
    parser.add_argument("--audio", action="store_true")
    args = parser.parse_args()

    command = ["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(args.media)]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    data = json.loads(result.stdout)
    video = next((row for row in data["streams"] if row.get("codec_type") == "video"), None)
    audio = next((row for row in data["streams"] if row.get("codec_type") == "audio"), None)
    errors = []
    if not video:
        errors.append("missing video stream")
    else:
        if args.width and video.get("width") != args.width:
            errors.append(f"width {video.get('width')} != {args.width}")
        if args.height and video.get("height") != args.height:
            errors.append(f"height {video.get('height')} != {args.height}")
        if args.fps:
            numerator, denominator = map(float, video["r_frame_rate"].split("/"))
            actual = numerator / denominator
            if abs(actual - args.fps) > .01:
                errors.append(f"fps {actual} != {args.fps}")
    if args.audio and not audio:
        errors.append("missing audio stream")
    if float(data["format"].get("duration", 0)) <= 0:
        errors.append("invalid duration")
    summary = {"file": str(args.media), "duration": data["format"].get("duration"), "video": video, "audio": audio, "errors": errors}
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
