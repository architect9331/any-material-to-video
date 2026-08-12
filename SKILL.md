---
name: any-material-to-video
description: Turn mixed source materials into a polished, narrated, evidence-bound video through a reproducible pipeline. Use when Codex needs to create a project demo, course recap, research presentation, report explainer, product launch, portfolio film, or social video from repositories, PDFs, DOCX, PPTX, webpages, spreadsheets, charts, screenshots, images, audio, or existing video; also use when the user asks for automatic scripting, source-to-shot binding, zero-human TTS, Remotion animation, subtitle synchronization, rendering, or audiovisual quality control.
---

# Any Material to Video

Build videos as reproducible software artifacts, not opaque editing sessions. Preserve real source evidence, animate abstract relationships, synthesize replaceable narration, and drive scenes and captions from the mastered audio timeline.

## Operating contract

- Treat every factual claim as requiring a source or an explicit `conceptual` label.
- Use real interfaces, documents, charts, and interactions when describing their contents. Never substitute a decorative image that only resembles the evidence.
- Do not crop away context needed to understand a real interface. Prefer full-frame fit, masks, pointers, highlights, and state changes over continuous zoom.
- Keep generated narration replaceable by segment. Do not require a single irreversible audio render.
- Derive scene and caption timing from the final mastered audio, not from estimated reading speed.
- Render a preview and inspect a contact sheet before the final render.
- Never claim that the pipeline is literally one-click unless the required adapters and credentials are configured. Describe missing adapters honestly.

## Workflow

### 1. Establish the delivery contract

Resolve or reasonably infer:

- audience and outcome;
- target duration, aspect ratio, resolution, frame rate, language, and pace;
- desired style and whether a public voice, generated voice, or user-supplied recording is allowed;
- output folder and whether source code must be delivered;
- privacy, licensing, and attribution constraints.

Default to 1920×1080, 30 fps, H.264 + AAC, captions enabled, and roughly 120–150 seconds for a detailed showcase.

### 2. Inventory the material

Run `scripts/inventory.py INPUT... --output work/inventory.json`. Keep the result with the production artifacts.

Group inputs by role:

- **identity**: title, owner, purpose, logo;
- **evidence**: real UI, documents, charts, citations, test output;
- **explanation**: architecture, process, relationships, chronology;
- **audio/video**: recordings, interviews, screen captures;
- **constraints**: brand, permissions, confidentiality, attribution.

For format-specific extraction and adapter choices, read [references/input-adapters.md](references/input-adapters.md).

### 3. Build a claim ledger

Create `work/claim-ledger.json` using [references/schemas.md](references/schemas.md). For every proposed narration claim, record:

- exact claim;
- source path or URL;
- source locator such as page, timestamp, code symbol, commit, or UI state;
- confidence;
- preferred visual;
- evidence type: `real`, `derived`, or `conceptual`.

Drop unsupported claims or weaken them explicitly. A conceptual animation may explain a mechanism but must not masquerade as a real product screen or measured result.

### 4. Design the story

Choose a structure based on the requested outcome:

- product: friction → workflow → proof → architecture → outcome;
- course: question → concepts → examples → recap;
- research: problem → method → evidence → limitations → result;
- report: headline → supporting data → implications → actions;
- portfolio: context → decisions → craft → result → reusable capability.

Write short spoken sentences. Bind each sentence to a real visual, a derived visualization, or a conceptual animation. Use [references/visual-grammar.md](references/visual-grammar.md) for shot selection and motion rules.

If the inputs do not establish a topic, audience, or supported result, do not invent one. Continue with a transparent material-readiness or process explainer when that still serves the request; otherwise report the missing inputs. Mark estimated timings as provisional until narration has been mastered.

### 5. Prepare real evidence

- Capture the whole system or page before emphasizing a region.
- Capture interaction states before and after clicks when narration describes navigation or evidence location.
- Render PDF, PPTX, DOCX, and spreadsheets before deciding their crop.
- Rebuild charts from data when the original image is unreadable, and label them as derived.
- Preserve source identifiers in the claim ledger even when they do not appear on screen.

### 6. Produce narration without manual recording

Keep the TTS backend replaceable. Prefer a two-stage setup:

1. generate or select a voice anchor using a short representative passage;
2. synthesize the final script as individually replaceable segments.

Normalize silence, gaps, sample rate, dynamics, and loudness after synthesis. A common target is about -16 LUFS with true peak at or below -1.5 dBTP.

Run `scripts/build_timeline.py --segments work/voice-segments --script work/script.json --output work/timeline.json --concat work/narration.wav` after segment generation. If the user asks for fast speech, shorten copy first and use modest time compression second. Avoid making speech intelligibility depend on aggressive acceleration.

Read [references/audio.md](references/audio.md) before choosing a TTS backend or mastering settings.

### 7. Build the video as code

Use an existing video project when present. Otherwise copy `assets/remotion-starter/` into a work directory and install its declared dependencies.

Drive all scenes from `timeline.json`. A scene must not own a second hand-maintained copy of its timestamps.

Combine:

- real evidence frames for factual demonstrations;
- charts and diagrams for exact relationships;
- small programmatic animations for ingestion, parsing, ranking, audio waveforms, timelines, quality gates, and feedback loops;
- full-context layouts before detail emphasis;
- captions inside a consistent safe area.

### 8. Validate in gates

Run these gates in order:

1. **Static**: typecheck or lint, asset existence, duration consistency.
2. **Preview**: render at half scale; inspect start, middle, end, and every evidence-bound scene.
3. **Contact sheet**: generate 12–20 evenly spaced frames and inspect hierarchy, clipping, blank scenes, and repetition.
4. **Final**: render the delivery resolution.
5. **Media QC**: run `scripts/media_qc.py FINAL.mp4 --width 1920 --height 1080 --fps 30 --audio`.
6. **Speech QC**: transcribe the mastered narration or final video with an available ASR system and compare names, numbers, and technical terms against the script.

Do not deliver a final video when the preview has unresolved evidence mismatch, illegible real UI, overflow, missing audio, or silent gaps caused by timeline errors.

### 9. Iterate surgically

Map feedback to the narrowest rebuild:

- pronunciation or wording → regenerate one narration segment;
- overall pace → revise copy or remaster audio, then rebuild the timeline;
- evidence mismatch → replace the visual and its locator;
- style → change theme tokens and layout components;
- timing → regenerate from audio metadata;
- isolated animation → patch one scene.

Re-run every downstream gate affected by the change.

### 10. Deliver reproducibly

Deliver at minimum:

- final video;
- mastered narration;
- script and timeline;
- claim ledger;
- production specification;
- contact sheet;
- reusable video source when requested.

Keep temporary model files, caches, private source material, credentials, and licensed media out of the deliverable and repository.

## Resource routing

- Read [references/input-adapters.md](references/input-adapters.md) when deciding how to extract or capture a specific file type.
- Read [references/schemas.md](references/schemas.md) when creating production JSON files or validating their fields.
- Read [references/visual-grammar.md](references/visual-grammar.md) when storyboarding or reviewing visual quality.
- Read [references/audio.md](references/audio.md) before configuring voice design, TTS, mastering, or ASR.
- Use `scripts/inventory.py`, `scripts/build_timeline.py`, and `scripts/media_qc.py` rather than rewriting those operations.
- Use `assets/remotion-starter/` only when the target workspace has no suitable video codebase.
