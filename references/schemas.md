# Production schemas

## Script

```json
[
  {
    "id": "scene-01",
    "text": "Short spoken sentence.",
    "visual_intent": "What the viewer should understand",
    "claim_ids": ["claim-01"]
  }
]
```

## Claim ledger

```json
{
  "claims": [
    {
      "id": "claim-01",
      "claim": "The exact factual statement",
      "source": "relative/path/or-url",
      "locator": "page 9, symbol X, timestamp 00:31, or UI state",
      "confidence": "high",
      "evidence_type": "real",
      "preferred_visual": "full page with highlighted paragraph"
    }
  ]
}
```

`evidence_type` must be one of `real`, `derived`, or `conceptual`.

## Timeline

```json
{
  "sample_rate": 48000,
  "duration": 12.4,
  "segments": [
    {
      "id": "scene-01",
      "start": 0.0,
      "end": 7.2,
      "audio": "segments/scene-01.wav",
      "text": "Short spoken sentence."
    }
  ]
}
```

The final scene duration may add a short visual tail after the audio duration. Store that tail in video composition settings, not by falsifying audio metadata.
