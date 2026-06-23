# Targeted Round Pi Edit Manifest - 2026-06-19

현재 작업 기준:

- 원본 후보 디렉토리: `assets/tarot-cards-imagegen/inner-artslot-ratio-candidates/`
- 최종 카드 디렉토리: `assets/tarot-cards-imagegen/final/no-text/`
- 프롬프트 저장 디렉토리: `assets/tarot-cards-imagegen/prompts/ratio-regeneration/by-card/`
- 사용자 최신 지시: 전수 검사 결과를 신뢰하고 아래 대상만 처리한다.
- 편집 원칙: 기존 이미지를 입력 이미지로 사용하고, 이미지는 거의 그대로 유지한다. 사각형/직사각형/앱 아이콘형 Pi 컨테이너만 원형 보라-금색 코인/메달로 바꾼다.

## CLI/API 상태

- built-in `image_gen` 편집은 `06_major_06_the-lovers.png`에서 입력 이미지를 무시하고 무관한 이미지를 생성해 실패했다.
- 로컬 파일을 명시적으로 입력하는 편집에는 ImageGen CLI/API `edit` 경로가 필요하다.
- 현재 환경에서는 `OPENAI_API_KEY`가 설정되어 있지 않아 CLI/API 편집 실행 전 사용자 환경 설정이 필요하다.

## 대상 목록

| card | file | required edit |
| --- | --- | --- |
| Major 06 The Lovers | `06_major_06_the-lovers.png` | 사각 Pi 아이콘을 원형 코인으로 교정 |
| Major 07 The Chariot | `07_major_07_the-chariot.png` | 사각 Pi 아이콘을 원형 코인으로 교정 |
| Major 08 Strength | `08_major_08_strength.png` | 사각 Pi 아이콘을 원형 코인으로 교정 |
| Major 09 The Hermit | `09_major_09_the-hermit.png` | 사각 Pi 아이콘을 원형 코인으로 교정 |
| Major 11 Justice | `11_major_11_justice.png` | 사각 Pi 아이콘을 원형 코인으로 교정 |
| Major 13 Death | `13_major_13_death.png` | 사각 Pi 아이콘을 원형 코인으로 교정 |
| Major 14 Temperance | `14_major_14_temperance.png` | 사각 Pi 아이콘을 원형 코인으로 교정 |
| Major 16 The Tower | `16_major_16_the-tower.png` | 사각 Pi 아이콘을 원형 코인으로 교정, 떨어지는 인물 2명을 남성 1명/여성 1명으로 수정 |
| Wands 06 | `27_wands_six.png` | 완드가 7개로 보이는 문제를 정확히 6개로 수정 |
| Wands 10 | `31_wands_ten.png` | 완드 10개 유지, 주인공이 기진맥진한 느낌을 줄이고 수트 마지막 카드다운 긴장감/완성감으로 수정 |
| Swords King | `63_swords_king.png` | 사각 Pi 아이콘을 원형 코인으로 교정 |
| Pentacles Knight | `75_pentacles_knight.png` | 사각 Pi 아이콘을 원형 코인으로 교정 |

## 공통 편집 프롬프트 골격

```text
Use case: precise-object-edit
Input image: use the provided local PNG as the edit target.
Primary request: Preserve the input image almost exactly. Change only Pi Network symbols drawn as square app icons, square badges, rectangular patches, or flat square plaques into circular Pi coin medallions.
Canvas constraint: keep the exact same crop, framing, portrait art-slot aspect ratio, and no card border/nameplate/text.
Invariants: preserve characters, faces, poses, anatomy, clothing, background, lighting, color palette, tarot symbolism, and object counts unless a card-specific correction below explicitly says otherwise.
Pi coin requirement: every Pi symbol must sit inside a perfectly round purple-and-gold coin or medallion. No square icon, no rectangle patch, no app-icon tile, no flat square plaque, no C-shaped right side.
Avoid: changing anything except the named issue; no text, no border, no new objects, no style shift.
```

## CLI edit command template

```bash
python "$CODEX_HOME/skills/.system/imagegen/scripts/image_gen.py" edit \
  --image assets/tarot-cards-imagegen/inner-artslot-ratio-candidates/<input-file>.png \
  --prompt "<card-specific prompt>" \
  --quality high \
  --out /private/tmp/<input-file>_edited.png
```

After each accepted edit:

1. Check dimensions/ratio with `sips` or `magick identify`.
2. Inspect visually.
3. Copy accepted image over `assets/tarot-cards-imagegen/inner-artslot-ratio-candidates/<input-file>.png`.
4. Save the exact prompt to `assets/tarot-cards-imagegen/prompts/ratio-regeneration/by-card/<input-file>.md`.
5. Rebuild `final/no-text` and update `assets/tarot-cards-imagegen/preview/ratio-before-after-card-comparison.png`.
