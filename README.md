# Any Material to Video

An open-source Codex Skill for turning repositories, documents, webpages, screenshots, charts, audio, and existing video into polished narrated videos through a reproducible workflow.

It focuses on the parts that make automated video credible rather than merely flashy:

- every factual claim is bound to real, derived, or explicitly conceptual evidence;
- real interfaces remain readable and retain enough context to be understood;
- narration is generated in replaceable segments, with the mastered audio driving the timeline;
- Remotion scenes, captions, previews, contact sheets, and media checks are treated as code and test artifacts;
- targeted feedback only rebuilds the affected stages.

## 中文概要

这是一个把“任意素材 → 成片”沉淀为可复用能力的 Codex Skill。它可以处理项目仓库、论文、报告、PPT、网页、表格、截图、录音和已有视频，并把素材盘点、证据绑定、脚本设计、零人工配音、程序化动画、时间轴生成和质量检查串成一条可复现流水线。

## Install

```bash
git clone https://github.com/architect9331/any-material-to-video.git
cp -R any-material-to-video ~/.codex/skills/any-material-to-video
```

Restart Codex after installation so the Skill is discovered.

## Use

Invoke it explicitly:

```text
Use $any-material-to-video to turn these source materials into a polished,
narrated, evidence-bound video.
```

Or describe a matching task naturally, such as:

```text
Create a two-minute project showcase from this repository, its screenshots,
and the architecture document. Use automatic Mandarin narration and deliver
the Remotion source, timeline, claim ledger, contact sheet, and final MP4.
```

## What is included

```text
any-material-to-video/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── audio.md
│   ├── input-adapters.md
│   ├── schemas.md
│   └── visual-grammar.md
├── scripts/
│   ├── inventory.py
│   ├── build_timeline.py
│   └── media_qc.py
└── assets/remotion-starter/
```

The Python helpers use only the standard library except that `media_qc.py` expects `ffprobe` to be available. The Remotion starter declares its own pinned JavaScript dependencies.

## Core pipeline

```text
materials
  → deterministic inventory
  → claim/evidence ledger
  → source-bound script and storyboard
  → segmented TTS and audio mastering
  → audio-derived timeline
  → Remotion composition
  → preview and contact-sheet review
  → media and speech QC
  → reproducible delivery package
```

The Skill intentionally does not hard-code a TTS provider. It defines quality and interface requirements so local models, hosted APIs, or a user-selected voice backend can be exchanged without rewriting the rest of the pipeline.

## Validate

If the Codex `skill-creator` utilities are installed:

```bash
python /path/to/skill-creator/scripts/quick_validate.py .
```

You can also test the deterministic helpers directly:

```bash
python scripts/inventory.py ./materials --output work/inventory.json
python scripts/build_timeline.py \
  --segments work/voice-segments \
  --script work/script.json \
  --output work/timeline.json \
  --concat work/narration.wav
python scripts/media_qc.py output.mp4 --width 1920 --height 1080 --fps 30 --audio
```

## License

[MIT](LICENSE)
