# Input adapters

Select the narrowest reliable adapter already available in the environment. Preserve the original file and record the derived artifact.

| Input | Preferred extraction | Visual preparation | Locator |
| --- | --- | --- | --- |
| Repository | `rg`, language tooling, tests, `git log` | terminal/code cards, real UI capture | path, line, symbol, commit |
| PDF | text extraction plus rendered pages | full page before crop/highlight | page and quoted span |
| DOCX | OOXML/text extraction plus rendered pages | rendered page or derived diagram | page/heading |
| PPTX | slide text plus rendered slides | full slide or rebuilt motion layout | slide number |
| Spreadsheet | workbook parser and chart/data inspection | readable derived chart | sheet and range |
| Webpage | browser DOM inspection and screenshot | full page/viewport state | URL and selector/section |
| Image | metadata, OCR when needed, visual inspection | fit without destructive crop | file and region |
| Audio | metadata and ASR | waveform, speaker card, captions | timestamp |
| Video | metadata, sampled frames, ASR | real clips or frames | timestamp/range |

## Mixed inputs

Normalize every item into:

- stable source identifier;
- media type;
- extracted text or transcript when available;
- visual derivative paths;
- locators;
- license/privacy note;
- checksum.

Never treat OCR or ASR output as exact evidence without checking names, numbers, and technical terms against the source.
