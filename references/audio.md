# Audio pipeline

## Backend selection

Choose in this order when available:

1. user-supplied clean recording;
2. locally generated or licensed custom voice;
3. high-quality hosted TTS configured by the user;
4. public preset voice, disclosed when relevant.

Never ship model weights or provider credentials inside the skill.

## Segmentation

- Keep one semantic sentence or short paragraph per segment.
- Use stable IDs shared by script, audio, timeline, scene, and caption.
- Regenerate only the affected segment after wording or pronunciation changes.
- Preserve the exact transcript used to synthesize every segment.

## Mastering

- Trim leading and trailing dead air conservatively.
- Use intentional inter-segment gaps, commonly 0.20–0.45 seconds.
- Resample consistently, commonly 48 kHz for delivery.
- Use light high-pass, low-pass, compression, and loudness normalization.
- Aim near -16 LUFS and true peak no higher than -1.5 dBTP for general web delivery.
- Prefer rewriting over acceleration. Keep time compression modest and verify intelligibility.

## Quality control

- Listen at the beginning, middle, and end.
- Run ASR on the final master.
- Compare proper nouns, numbers, abbreviations, and technical terms manually or with a scripted diff.
- Check for clipped consonants introduced by silence trimming.
- Verify there is no unintended accent or prosody inconsistent with the requested style.
