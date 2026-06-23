# PI Tarot Next Session Handoff

## 2026-06-19 최신 상태 요약

현재 작업 위치는 `/Users/kakao/Desktop/etc/PI 타로2`이다.

사용자 최신 피드백 반영 완료:

- `25_wands_four.png`: 완드 4개가 명확하지 않던 문제를 수정. 현재는 좌 2개 + 우 2개, 총 4개의 별도 완드가 보인다.
- `27_wands_six.png`: 완드 7개처럼 보이던 문제를 수정. 현재는 총 6개의 별도 완드가 보인다.
- `28_wands_seven.png`: 완드 8개처럼 보이던 문제를 수정. 현재는 총 7개의 별도 완드가 보인다.
- `31_wands_ten.png`: 완드 11개처럼 보이던 문제를 수정. 현재는 총 10개의 별도 완드가 보인다.
- `45_cups_ten.png`: 컵 11개처럼 보이던 문제를 수정. 현재는 5+5 배열, 총 10개의 컵이 보인다.
- `30_wands_nine.png`는 사용자가 9개가 맞다고 확인했으므로 재생성하지 않았다.
- 새로 재생성한 카드들은 Pi motif를 사각 패치가 아니라 원형 코인/메달로 제한했다.
- `*rejected*` 이름으로 남은 파일은 현재 없다.

최신 산출물:

- 내부 후보: `assets/tarot-cards-imagegen/inner-artslot-ratio-candidates/` 78장
- 최종 no-text 카드: `assets/tarot-cards-imagegen/final/no-text/` 78장
- 카드별 프롬프트: `assets/tarot-cards-imagegen/prompts/ratio-regeneration/by-card/` 78개
- 최신 contact sheet:
  - `assets/tarot-cards-imagegen/preview/all-78-ratio-candidates-contact.png`
  - `assets/tarot-cards-imagegen/preview/imagegen-no-text-contact-sheet.png`

최신 검증:

- inner PNG count: 78
- final/no-text PNG count: 78
- prompt md count: 78
- 변경된 5개 final/no-text 카드 크기: 전부 `1024x1536`, `srgba`
- final/no-text 모서리 투명도 샘플: `srgba(0,0,0,0)`

주의:

- 현재 기본 `python3`에는 Pillow가 없어 `tools/render_imagegen_deck.py`가 바로 실패한다.
- 임시로 ImageMagick `magick`을 사용해 변경된 5장만 final/no-text에 합성했다.
- `tools/extract_imagegen_result.py`는 Pillow가 없어도 PNG 추출은 가능하도록 수정했다. Pillow가 없으면 비율 검증만 건너뛰고, 치수는 `sips` 또는 `magick identify`로 확인한다.
- `magick montage`는 현재 폰트 목록이 비어 있어 실패했다. contact sheet는 Python subprocess로 `magick ... +append/-append` 방식으로 직접 생성했다.
- ImageGen 결과 추출이 세션 JSONL에 의존하므로, 새 이미지/프롬프트 추출을 모두 끝내기 전에는 현재 `$CODEX_HOME/sessions` 로그를 삭제하지 말 것.
- 세션이 느려지면 이 문서를 읽고 새 세션에서 이어가는 것이 가장 안전하다.

작성일: 2026-06-17  
작업 위치: `/Users/kimhanbin/Documents/PI 타로`

## 2026-06-17 최종 스토리 리워크 완료 메모

사용자의 최신 완화 규칙을 반영했다.

- 주인공은 계속 중심에 두되, 얼굴이 보이지 않는 손/팔/몸 일부는 인원 제한에 포함하지 않는다.
- 화면이 너무 붐비지 않는 선에서 소수의 보조 인물, 마을 사람, 전령, 조력자를 허용한다.
- 이 규칙을 `assets/tarot-cards-imagegen/minor-number-storyboard.md`, `assets/tarot-cards-imagegen/minor-story-bible.md`, `tools/build_imagegen_prompt_queue.py`에 반영했다.

이번 완료 작업:

- Wands Ace~Ten을 연속 서사로 재구성해 `inner/22_wands_ace.png` ~ `inner/31_wands_ten.png`에 반영했다.
  - Five of Wands는 떠다니는 완드 대신 보조자의 손/팔이 잡은 훈련 구도로 교체했다.
  - Eight of Wands는 떠다니는 완드 대신 전령 둘이 각각 네 개씩 들고 달리는 릴레이 구도로 교체했다.
  - Ten of Wands는 얼굴 없는 보조 손이 돕는 5+5 두 묶음으로 교체해 열 개 가독성을 높였다.
- Cups Six를 낮은 돌탁자 위 3+3 컵 구도로 교체했다.
- Swords Seven~Ten을 전략 → 시험 → 불안 → 상징적 새벽 결말로 다시 연결했다.
- Pentacles는 단조로운 트레이 구도를 줄이기 위해 Two, Five, Seven, Nine, Ten을 추가 교체했다.
  - Two: 시장 저울 사이드뷰.
  - Five: 비 오는 골목의 천 보따리 3+2.
  - Seven: 넓은 테라스 밭 4+3.
  - Nine: 온실 통로 3+3+3.
  - Ten: 넓은 가게/정원 마당 5+5.
- `tools/build_imagegen_prompt_queue.py`의 `REPLACE_FILENAMES`를 비워 현재 큐는 완료 상태다.
- `assets/tarot-cards-imagegen/imagegen-prompt-queue.md`는 `Total prompts: 0`이다.
- `tools/render_imagegen_deck.py`를 실행해 final with-text/no-text를 전체 재렌더링했다.
- 검증 결과:
  - `assets/tarot-cards-imagegen/inner`: 78장, 전부 1024x1536, 손상 없음.
  - `assets/tarot-cards-imagegen/final/with-text`: 78장, 전부 1024x1536, 손상 없음.
  - `assets/tarot-cards-imagegen/final/no-text`: 78장, 전부 1024x1536, 손상 없음.
  - `assets/tarot-cards-imagegen/metadata.json`: `generated_count` 78, `missing_inner_images` 빈 배열, `cards` 78.
  - 최신 미리보기: `assets/tarot-cards-imagegen/preview/imagegen-with-text-contact-sheet.png`, `assets/tarot-cards-imagegen/preview/imagegen-no-text-contact-sheet.png`.

## 2026-06-17 이어받은 세션 진행 메모

이번 세션에서 실제 worktree를 다시 확인했다.

- 최신 사용자 지시: 이미지 생성은 Codex 내장 `image_gen`/imageGen 스킬만 사용한다.
- 최신 사용자 지시 추가: 카드 외각 템플릿은 바뀔 수 있으니 매번 최종 카드 렌더링을 하지 않아도 된다. 시간을 아껴 내부 일러스트(`inner/`)를 더 빨리 생성하는 것을 우선한다. `tools/render_imagegen_deck.py`는 여러 장을 모은 뒤 점검하거나 템플릿이 확정됐을 때 실행한다.
- 최신 사용자 피드백 추가: Page/Knight/Queen/King은 궁정/특수 아르카나이므로 본편 스토리에서 조금 벗어나도 괜찮다. 유지 가능.
- 최신 사용자 피드백 추가: Ace~Ten은 각 수트별로 기승전결이 있는 시간 순서 스토리의 주요 이벤트처럼 보여야 한다.
  - Wands는 스토리와 그림체가 이어지지 않는다. Ace~Ten 전체를 같은 Ember Trail 서사/스타일로 재생성 대상에 넣었다.
  - Cups Six는 컵 6개가 잘 읽히지 않는다. 3+3 낮은 탁자 구도로 재생성 대상에 넣었다.
  - Swords Seven/Nine은 뜬금없고, Ten의 영웅적 상징 죽음은 좋은 컨셉이지만 Eight/Nine에서 빌드업이 필요하다. Seven~Ten을 연결 서사로 재생성 대상에 넣었다.
  - Pentacles는 조용한 상인의 일상 컨셉은 좋지만 대부분 비슷한 구도라 단조롭다. Ace~Ten을 유지 컨셉+다양한 앵글로 재생성 대상에 넣었다.
- 최신 반영 완료: 번호 카드용 스토리보드 문서를 추가했다.
  - `assets/tarot-cards-imagegen/minor-number-storyboard.md`
  - Ace~Ten을 각 수트 본편 타임라인으로 정리했고, Page/Knights/Queen/King은 궁정 카드 초상으로 분리했다.
- 최신 반영 완료: `assets/tarot-cards-imagegen/minor-story-bible.md`가 새 번호 스토리보드를 source of truth로 참조하도록 업데이트했다.
- 최신 반영 완료: `tools/build_imagegen_prompt_queue.py`의 교체 큐를 새 스토리 기준 25장으로 설정했다.
  - Wands Ace~Ten: `22_wands_ace.png` ~ `31_wands_ten.png`
  - Cups Six: `41_cups_six.png`
  - Swords Seven~Ten: `56_swords_seven.png` ~ `59_swords_ten.png`
  - Pentacles Ace~Ten: `64_pentacles_ace.png` ~ `73_pentacles_ten.png`
  - 현재 `assets/tarot-cards-imagegen/imagegen-prompt-queue.md`는 `Total prompts: 25`
- 최신 반영 완료: `25_wands_four.png`는 Pi Network 아이콘형 금화 문양으로 교체 완료했다.
  - 내장 imageGen 결과가 파일로 바로 저장되지는 않았지만, 세션 JSONL의 `image_generation_call.result` PNG 데이터를 추출해 `assets/tarot-cards-imagegen/attempts/25_wands_four_pi-icon-fixed_attempt.png`로 저장했다.
  - 기존 내부 이미지는 `assets/tarot-cards-imagegen/attempts/replaced-inner/25_wands_four_before_pi-icon-fix.png`로 백업했다.
  - 새 내부 이미지를 `assets/tarot-cards-imagegen/inner/25_wands_four.png`에 반영했고, `tools/render_imagegen_deck.py`로 `final/with-text`와 `final/no-text`를 다시 렌더링했다.
  - 큰 금화는 수학 기호 π가 아니라 두 점, 둥근 상단 브리지, 두 세로 줄기, 오른쪽 말림이 있는 Pi Network 아이콘형으로 보인다.
- 최신 추가 반영 완료: `26_wands_five.png`도 군중형 문제 버전을 교체 완료했다.
  - 내장 imageGen으로 주인공 1명 + 작은 fox 1마리 + 정확히 다섯 지팡이 구도를 생성했다.
  - 생성 결과는 세션 JSONL의 `image_generation_call.result` PNG 데이터를 추출해 `assets/tarot-cards-imagegen/attempts/26_wands_five_single-protagonist_pi-icon_attempt.png`로 저장했다.
  - 기존 내부 이미지는 `assets/tarot-cards-imagegen/attempts/replaced-inner/26_wands_five_before_single-protagonist-fix.png`로 백업했다.
  - 새 내부 이미지를 `assets/tarot-cards-imagegen/inner/26_wands_five.png`에 반영했고, `tools/render_imagegen_deck.py`로 `final/with-text`와 `final/no-text`를 다시 렌더링했다.
  - 최종 카드에서는 사람 1명, fox 1마리, 지팡이 5개가 보이며, 이전처럼 여러 명이 싸우는 장면이 아니다.
- 최신 추가 반영 완료: `61_swords_knight.png`를 새로 생성해 추가했다.
  - 내장 imageGen으로 주인공 1명 + owl familiar + 정확히 검 1자루 중심의 비폭력 학원/바람 장면을 생성했다.
  - 생성 결과는 세션 JSONL의 `image_generation_call.result` PNG 데이터를 추출해 `assets/tarot-cards-imagegen/attempts/61_swords_knight_one-sword_pi-icon_attempt.png`로 저장했다.
  - 새 내부 이미지를 `assets/tarot-cards-imagegen/inner/61_swords_knight.png`에 반영했고, `tools/render_imagegen_deck.py`로 `final/with-text`와 `final/no-text`를 다시 렌더링했다.
  - 최종 카드에서는 검 1자루, 주인공 1명, owl familiar 1마리, Pi Network 아이콘형 메달이 보인다.
- 최신 추가 반영 완료: `62_swords_queen.png`를 새로 생성해 추가했다.
  - 내장 imageGen으로 고요한 Queen 좌상/정적 자세, 주인공 1명, owl familiar 1마리, 검 1자루 중심의 비폭력 학원/달빛 장면을 생성했다.
  - 생성 결과는 세션 JSONL의 `image_generation_call.result` PNG 데이터를 추출해 `assets/tarot-cards-imagegen/attempts/62_swords_queen_serene_one-sword_pi-icon_attempt.png`로 저장했다.
  - 새 내부 이미지를 `assets/tarot-cards-imagegen/inner/62_swords_queen.png`에 반영했고, `tools/render_imagegen_deck.py`로 `final/with-text`와 `final/no-text`를 다시 렌더링했다.
  - 최종 카드에서는 검 1자루, 주인공 1명, owl familiar 1마리, 큰 Pi Network 아이콘형 메달이 보인다.
- 최신 추가 반영 완료: `63_swords_king.png`를 새로 생성해 추가했다.
  - 내장 imageGen으로 안정적인 King 좌상/정적 자세, 주인공 1명, owl familiar 1마리, 검 1자루 중심의 비폭력 학원/관측소 장면을 생성했다.
  - 생성 결과는 세션 JSONL의 `image_generation_call.result` PNG 데이터를 추출해 `assets/tarot-cards-imagegen/attempts/63_swords_king_one-sword_pi-icon_attempt.png`로 저장했다.
  - 새 내부 이미지를 `assets/tarot-cards-imagegen/inner/63_swords_king.png`에 반영했고, `tools/render_imagegen_deck.py`로 `final/with-text`와 `final/no-text`를 다시 렌더링했다.
  - 최종 카드에서는 검 1자루, 주인공 1명, owl familiar 1마리, 큰 Pi Network 아이콘형 메달이 보인다. 책/글자/추가 원형 도구가 생긴 첫 후보는 폐기했다.
- 최신 추가 반영 완료: `64_pentacles_ace.png`를 새로 생성해 추가했다.
  - 내장 imageGen으로 주인공 1명, sprout mascot 1마리, 정확히 하나의 큰 golden coinseed를 심는 장면을 생성했다.
  - 생성 결과는 세션 JSONL의 `image_generation_call.result` PNG 데이터를 추출해 `assets/tarot-cards-imagegen/attempts/64_pentacles_ace_one-coinseed_pi-icon_attempt.png`로 저장했다.
  - 새 내부 이미지를 `assets/tarot-cards-imagegen/inner/64_pentacles_ace.png`에 반영했고, `tools/render_imagegen_deck.py`로 `final/with-text`와 `final/no-text`를 다시 렌더링했다.
  - 최종 카드에서는 큰 coinseed 1개와 Pi Network 아이콘형 문양이 잘 보인다. 작은 금색 장식은 있으나 pentacle/coinseed로 세어질 만한 추가 금원반은 없다.
- 최신 추가 반영 완료: `65_pentacles_two.png`를 새로 생성해 추가했다.
  - 사용자가 지적한 대로 기존 후보의 우측 문양이 공식 Pi Network 아이콘이 아니라 C자 구멍/링처럼 보였다.
  - Apple App Store의 Pi Network 공식 앱 아이콘 대표 이미지를 내려받아 기준 레퍼런스로 저장했다: `assets/tarot-cards-imagegen/references/pi-network-appstore-icon-512.jpg`.
  - 공식 아이콘 기준: 오른쪽은 원형 구멍/링/C자가 아니라 상단 획 끝이 살짝 위로 솟은 채워진 훅이다.
  - 내장 imageGen으로 주인공 1명, sprout mascot 1마리, 정확히 두 개의 큰 golden coinseed를 든 장면을 다시 생성했다.
  - 생성 결과는 `assets/tarot-cards-imagegen/attempts/65_pentacles_two_official-appstore-icon_attempt.png`로 저장했다.
  - 새 내부 이미지를 `assets/tarot-cards-imagegen/inner/65_pentacles_two.png`에 반영했고, `tools/render_imagegen_deck.py`로 `final/with-text`와 `final/no-text`를 다시 렌더링했다.
  - 최종 카드에서는 코인 2개만 크게 보이고, 두 코인의 문양 모두 C자 구멍 없이 공식 아이콘형의 오른쪽 위로 솟은 훅으로 보인다.
- 최신 추가 반영 완료: `66_pentacles_three.png`를 새로 생성해 추가했다.
  - 내장 imageGen으로 주인공 1명, sprout mascot 1마리, subtle helper hands만 있는 공방 학습 장면을 생성했다.
  - 첫 후보는 구도는 좋았지만 목걸이/도면 원형이 추가 금원반처럼 보일 수 있어 폐기 후보로만 저장했다: `assets/tarot-cards-imagegen/attempts/66_pentacles_three_first_attempt_extra-round-details.png`.
  - 두 번째 후보는 정확히 세 개의 큰 golden medallion이 workbench 위에 분리되어 있고, Pi 문양도 공식 앱 아이콘형의 오른쪽 채워진 upturned hook에 가깝다.
  - 채택 후보는 `assets/tarot-cards-imagegen/attempts/66_pentacles_three_three-medallions_official-icon_attempt.png`로 저장했다.
  - 새 내부 이미지를 `assets/tarot-cards-imagegen/inner/66_pentacles_three.png`에 반영했고, `tools/render_imagegen_deck.py`로 `final/with-text`와 `final/no-text`를 다시 렌더링했다.
  - 최종 카드에서는 세 메달이 하단 네임플레이트에 가려지지 않고, 추가로 세어질 만한 금원반 없이 Three of Pentacles로 읽힌다.
- 최신 추가 반영 완료: `67_pentacles_four.png`를 새로 생성해 추가했다.
  - 내장 imageGen으로 주인공 1명, sprout mascot 1마리, 작은 garden gate/보호된 plot 장면을 생성했다.
  - exactly four golden coinseeds가 shallow wooden seed tray 안에 2x2로 완전히 보이며, 추가로 세어질 만한 금원반은 없다.
  - 생성 결과는 `assets/tarot-cards-imagegen/attempts/67_pentacles_four_four-coinseeds_official-icon_attempt.png`로 저장했다.
  - 새 내부 이미지를 `assets/tarot-cards-imagegen/inner/67_pentacles_four.png`에 반영했고, `tools/render_imagegen_deck.py`로 `final/with-text`와 `final/no-text`를 다시 렌더링했다.
  - 최종 카드에서는 네 coinseed가 네임플레이트에 가려지지 않고, 보호/관리의 Four of Pentacles 톤으로 읽힌다.
- 최신 추가 반영 완료: `68_pentacles_five.png`를 새로 생성해 추가했다.
  - 내장 imageGen으로 비 오는 coinseed garden 가장자리, 주인공 1명, sprout mascot 1마리, 따뜻한 직사각형 workshop window가 보이는 장면을 생성했다.
  - 정확히 다섯 golden coinseed가 전경에 3+2 배열로 크고 선명하게 보이며, 하단 네임플레이트에 가려지지 않는다.
  - 생성 결과는 `assets/tarot-cards-imagegen/attempts/68_pentacles_five_five-coinseeds_rainy-official-icon_attempt.png`로 저장했다.
  - 새 내부 이미지를 `assets/tarot-cards-imagegen/inner/68_pentacles_five.png`에 반영했고, `tools/render_imagegen_deck.py`로 `final/with-text`와 `final/no-text`를 다시 렌더링했다.
  - 최종 카드에서는 비 오는 결핍 분위기지만 따뜻한 창빛과 보호 제스처가 있어 Five of Pentacles가 절망적이지 않고 희망적으로 읽힌다.
- 최신 추가 반영 완료: `69_pentacles_six.png` ~ `77_pentacles_king.png`까지 내장 imageGen으로 생성해 `inner/`에 반영했다.
  - `69_pentacles_six.png`: 나눔/균형 장면, 정확히 여섯 coinseed.
  - `70_pentacles_seven.png`: 이전 C자 구멍형 문양 후보를 폐기하고 4+3 raised bed 버전으로 교체. 현재 코인은 정확히 7개이며 오른쪽 훅은 채워진 형태다.
  - `71_pentacles_eight.png`: 작업대/건조줄 장면, 위 4개 + 아래 4개로 정확히 여덟 medallion.
  - `72_pentacles_nine.png`: 온실 화단 안 3x3 배열로 정확히 아홉 coinseed.
  - `73_pentacles_ten.png`: 첫 후보는 나무의 추가 hanging medallion 때문에 폐기했고, 최종은 raised bed 안 5+5 배열로 정확히 열 coinseed.
  - `74_pentacles_page.png`: 한 개의 큰 coinseed를 배우는 Page 장면, blank notebook.
  - `75_pentacles_knight.png`: 바구니 위 큰 coinseed 2개, 성실한 운반 장면.
  - `76_pentacles_queen.png`: 온실에서 한 개의 sprouting coinseed를 돌보는 Queen 장면.
  - `77_pentacles_king.png`: 첫 후보의 추가 원형 brooch를 폐기했고, 최종은 전경 테이블 위 coinseed 1개만 있는 King 장면.
- 렌더 템플릿의 작은 프레임 코인도 plain π 텍스트가 아니라 Pi Network 아이콘형 도형으로 다시 그리도록 `tools/render_imagegen_deck.py`에 후처리를 추가했다.
- 렌더 템플릿과 `tools/generate_tarot_deck.py`의 Pi Network형 도형 함수도 C자/구멍 형태를 제거하고 공식 아이콘처럼 채워진 오른쪽 upturned hook을 그리도록 수정했다. 현재 두 스크립트에서 `"π"`/`π` 검색 결과 없음.
- `tools/render_imagegen_deck.py`에 PNG 저장 후 즉시 열어 검증하는 `save_png_verified`를 추가했다. `optimize=True` 저장 직후 `final/with-text/20_major_20_judgement.png`가 깨진 적이 있어, 깨진 PNG가 생기면 non-optimized 저장으로 자동 재시도한다.
- 현재 프롬프트 큐는 `Total prompts: 0`이다. 남은 inner 생성 대상 없음.
- `inner`는 78장까지 완성됐다.
- 기존 생성 원본에서 Swords 8~10/Page를 회수해 아래 경로에 저장했다.
  - `assets/tarot-cards-imagegen/inner/57_swords_eight.png`
  - `assets/tarot-cards-imagegen/inner/58_swords_nine.png`
  - `assets/tarot-cards-imagegen/inner/59_swords_ten.png`
  - `assets/tarot-cards-imagegen/inner/60_swords_page.png`
- 번들 Python으로 `tools/render_imagegen_deck.py`를 최종 일괄 실행했다.
- 현재 정상 렌더 상태:
  - `assets/tarot-cards-imagegen/inner`: 78장, 손상 없음, 전부 1024x1536
  - `assets/tarot-cards-imagegen/final/with-text`: 78장, 손상 없음, 전부 1024x1536
  - `assets/tarot-cards-imagegen/final/no-text`: 78장, 손상 없음, 전부 1024x1536
  - `assets/tarot-cards-imagegen/metadata.json`: `generated_count` 78, `missing_inner_images` 빈 배열, `cards` 78
  - contact sheets: `assets/tarot-cards-imagegen/preview/imagegen-with-text-contact-sheet.png`, `assets/tarot-cards-imagegen/preview/imagegen-no-text-contact-sheet.png`
- 현재 누락: 없음.
- Wands 4, Wands 5, Swords Knight, Swords Queen, Swords King, Pentacles Ace~King까지 모두 완료했다. 다음 생성 대상 없음.
- 이번 세션에서 기본 `image_gen`으로 Wands 4 후보를 만들었으나, 이미지가 대화에는 보이고 파일 시스템에는 저장되지 않았다. `/Users/kimhanbin/.codex/generated_images`와 프로젝트 `generated_images`의 파일 수/mtime 모두 증가하지 않았다. 따라서 새 이미지를 실제 자산으로 쓰려면 저장 가능한 imagegen 경로를 먼저 확보해야 한다.
- 기본 `image_gen`이 계속 미저장 상태지만, 사용자가 내장 imageGen 사용을 명시했다. 저장 문제를 우회하려고 다른 생성 경로로 전환하지 말 것.
- 이번 세션에서 내장 `image_gen`으로 Wands 4와 Wands 5 후보를 다시 만들었다. 둘 다 대화 화면에는 보였지만, 파일 시스템에는 저장되지 않았다.
  - 저장 확인: `/Users/kimhanbin/.codex/generated_images`, 프로젝트 `generated_images`, `/private/tmp`, `$TMPDIR`에서 최근 `.png/.jpg/.jpeg/.webp` 없음.
  - 파일 수 확인: 기존 이미지 파일 수 133으로 변화 없음.
- Wands 4 후보: 네 지팡이 아치가 명확하고 금색도 적당했다.
  - Wands 5 후보: 주인공 1명 + 다섯 지팡이는 좋았다. 하지만 일부 코인 문양이 Pi라기보다 로마 숫자 II처럼 보여서 실패 후보로 본다.
- 최신 Pi coin 지시: 무문양 금화도 안 된다. 코인은 반드시 Pi 코인답게 보여야 한다. 작아서 Pi 문양이 무너지면 코인을 더 크게/적게 배치해서라도 연결된 π-like 엠블럼이 읽히게 해야 한다.
- 추가 최신 Pi icon 지시: 금화 위 문양은 수학 기호 π 자체가 아니라 Pi Network 코인/앱 아이콘 형태여야 한다. 두 점, 둥근 블록형 상단 획, 두 세로 줄기, 오른쪽으로 올라가는 팔/꼬리까지 포함한 아이콘형 엠보싱으로 지시한다.
- 내장 imageGen 테스트 결과: 아이콘 단독 테스트는 방향이 좋아졌고, Wands Five 후보도 지팡이/인물 수는 좋아졌지만 작은 배경 장식은 다시 일반 기호처럼 보일 수 있었다. 다음 생성에서는 작은 반복 문양을 많이 쓰기보다 큰 코인/메달 1~2개에 선명한 아이콘형 엠보싱을 우선한다.
- 이어서 내장 imageGen으로 Wands Four를 다시 생성했다.
  - 첫 후보: 분위기와 Pi 아이콘형 메달은 좋았지만, 배경/장식 기둥이 추가 지팡이처럼 보여서 Four of Wands 개수 가독성이 불안했다.
  - 두 번째 후보: 네 지팡이가 왼쪽 기둥, 오른쪽 기둥, 위쪽 교차 지팡이 2개로 비교적 명확했고, 중앙 금색 메달도 수학 π 글자보다는 Pi Network 아이콘형 두 점/블록 상단 획에 가까웠다. 현재까지 Wands Four 후보 중 가장 나은 방향이다.
  - 하지만 두 후보 모두 파일 시스템에는 저장되지 않았다. 확인 위치: `/Users/kimhanbin/.codex/generated_images`, 프로젝트 `generated_images`, `/private/tmp`, `/private/var/folders/lz/wmntg2z57598q8781_xsbd8r0000gn/T` 최근 이미지 없음.
- Swords/Pentacles 프롬프트에 슈트별 discipline을 추가했다.
  - Wands: 추가 기둥/나무/장대가 지팡이처럼 보이지 않게 금지.
  - Swords: 비폭력, 학원/지성 톤, 요청된 검 외 추가 검/무기 더미 금지.
  - Pentacles: 코인씨앗/메달은 작은 금가루나 코인 더미가 아니라 크고 개수 세기 쉬워야 하며, 보이는 코인에는 단순 금원반이 아닌 Pi Network 아이콘형 엠보싱이 있어야 한다.
- 내장 imageGen으로 Knight of Swords 후보를 두 번 생성했다.
  - 두 후보 모두 비폭력 학원 톤, 주인공 1명, 검 1자루 구도는 좋았다.
  - 하지만 금색 메달 문양이 여전히 T자/수학 π/로마자 II처럼 보일 위험이 있어 프로젝트 자산 후보로는 보류한다.
  - 이후 공통 Pi 문양 설명에 `T-shaped mark`, `plus-sign mark` 금지를 추가하고, 오른쪽 꼬리/팔이 오른쪽 줄기에서 위로 말려 올라가야 한다고 더 강하게 명시했다.
- 강화한 프롬프트로 Knight of Swords를 한 번 더 생성했다.
  - 카드 구도, 주인공 1명, 검 1자루, 비폭력 톤은 가장 좋았다.
  - 하지만 중앙 메달이 여전히 두 점 달린 수학 π 글자처럼 보여서 사용자 피드백 기준에는 실패다. `61_swords_knight.png`로 저장/채택하지 말 것.
  - 이 문제는 텍스트 프롬프트만으로 모델이 Pi Network 아이콘 실루엣을 안정적으로 이해하지 못하는 패턴으로 보인다. 다음에는 가능하면 아이콘 참고 이미지를 대화 컨텍스트에 보이게 한 뒤 내장 imageGen에 참조하도록 시도한다. 단, 실제 생성 경로는 여전히 내장 imageGen만 사용한다.
- Pi Network 아이콘을 다시 눈으로 보고 문양 설명을 더 정밀화했다.
  - 단순한 두 줄기+가로획이 아니라, 왼쪽 끝은 살짝 아래로 굽는 어깨가 있고 오른쪽 끝은 공식 앱 아이콘처럼 살짝 위로 솟은 채워진 훅이다.
  - 오른쪽 끝은 C자 구멍/링/루프가 아니다. 원형 구멍을 뚫으면 공식 Pi Network 아이콘과 달라진다.
  - 금화 위 금색 양각만으로는 형태가 뭉개지므로, 음각 홈 또는 은은한 보라색 에나멜 대비를 허용해 금색 표면에서 아이콘 실루엣이 읽히게 한다.
- Pi Network 공식 App Store 아이콘 대표 이미지를 인터넷에서 내려받아 프로젝트에 저장했다.
  - 경로: `assets/tarot-cards-imagegen/references/pi-network-appstore-icon-512.jpg`
  - 출처: Apple lookup API의 `artworkUrl512` / App Store `Pi Network` 앱, developer `SocialChain`.
  - 앞으로 헷갈리면 이 이미지를 `view_image`로 먼저 보고 생성한다.
- 예전에 Pi Network 아이콘 구조를 설명하기 위해 만든 참고용 실루엣 이미지가 프로젝트에 남아 있다.
  - 경로: `assets/tarot-cards-imagegen/references/pi-network-icon-shape-reference.png`
  - 크기: 1024x1024 RGB
  - 이것은 오른쪽을 C형 구멍/링처럼 과장한 문제가 있으므로 더 이상 기준 레퍼런스로 쓰지 말 것. 공식 App Store 아이콘을 우선한다.
  - 이 참고 이미지를 보여준 뒤 Knight of Swords를 다시 생성했더니, 이전보다 메달 문양이 단순 π에서 벗어나고 보라색 음각/에나멜과 오른쪽 곡선 어깨가 살아났다. 검 1자루, 주인공 1명, 비폭력 톤도 맞았다.
  - 그러나 생성된 카드 후보 자체는 여전히 파일 시스템에 저장되지 않았다. 확인 위치: `/Users/kimhanbin/.codex/generated_images`, 프로젝트 `generated_images`, `/private/tmp`, `/private/var/folders/lz/wmntg2z57598q8781_xsbd8r0000gn/T` 최근 이미지 없음. 프로젝트 자산으로는 아직 미반영.
- 추가로 `tools/build_imagegen_prompt_queue.py`를 만들었다. 현재 worktree의 누락 상태를 기준으로 남은 프롬프트를 생성/갱신한다.
- 생성된 큐 파일: `assets/tarot-cards-imagegen/imagegen-prompt-queue.md`
- 큐 검증:
  - 현재 `Total prompts: 0`
  - 남은 항목 없음
  - 공통 금색 문구에서 `coinseeds`가 Wands/Swords에 새어 들어가지 않도록 수정했다.
  - 중복 마침표(`..`) 없음.
- 실제 생성은 내장 imageGen으로만 진행한다. 내장 경로 외 생성 절차는 삭제했다.
- 실제 생성 파일은 `assets/tarot-cards-imagegen/inner/`에 카드 metadata filename 그대로 저장했다.
- 폐기/교체 전 후보는 `assets/tarot-cards-imagegen/attempts/`와 `assets/tarot-cards-imagegen/attempts/replaced-inner/` 아래에 남겨두었다.
- 카드마다 렌더링하지 않고 inner를 우선 채운 뒤, 마지막에 번들 Python으로 `tools/render_imagegen_deck.py`를 일괄 실행했다.
- 최종 contact sheet와 78장/78장 검증을 완료했다.

## 목표

Pi-inspired 타로 서비스용 고퀄리티 카드 이미지 78장을 완성한다.

최종 산출물은 반드시 두 버전이어야 한다.

- 텍스트 있는 버전: `assets/tarot-cards-imagegen/final/with-text/*.png`
- 텍스트 없는 버전: `assets/tarot-cards-imagegen/final/no-text/*.png`

대상 사용자는 해외 사용자이므로 최종 카드에는 한글이 없어야 한다. 텍스트 있는 버전은 영어 카드명과 번호/랭크만 들어가야 한다.

## 절대 유지할 제작 방식

imageGen으로 카드 전체를 만들지 말 것. 이전에 그렇게 했더니 테두리, 네임플레이트, 레이아웃이 카드마다 흔들렸다.

올바른 방식:

1. imageGen은 카드 내부 일러스트만 생성한다.
2. 내부 일러스트 파일을 `assets/tarot-cards-imagegen/inner/`에 카드 metadata filename 그대로 저장한다.
3. 고정 템플릿으로 합성한다.
4. 합성은 `tools/render_imagegen_deck.py`를 사용한다.

중요 파일:

- 템플릿 원본: `assets/tarot-cards-imagegen/template/imagegen-card-template.png`
- 템플릿 오버레이: `assets/tarot-cards-imagegen/template/card-template-overlay.png`
- 아트 슬롯 마스크: `assets/tarot-cards-imagegen/template/art-slot-mask.png`
- 합성 스크립트: `tools/render_imagegen_deck.py`
- 카드 목록/파일명 데이터: `tools/generate_tarot_deck.py`
- 마이너 스토리 바이블: `assets/tarot-cards-imagegen/minor-story-bible.md`
- Pi 공식 앱 아이콘 대표 참고 이미지: `assets/tarot-cards-imagegen/references/pi-network-appstore-icon-512.jpg`

로컬 기본 `python3`에는 PIL이 없었다. 렌더링은 Codex 번들 Python을 쓰면 됐다.

```bash
/Users/kimhanbin/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 tools/render_imagegen_deck.py
```

## 현재 상태 요약

반드시 새 세션에서 실제 worktree를 다시 확인할 것. 아래는 이 문서 작성 시점의 기억/상태다.

- 메이저 22장은 새 Pi coin motif와 절제된 금색 기준으로 재생성되어 `inner/00`~`inner/21`에 들어가 있다.
- 마이너 56장도 슈트별 스토리 방식으로 다시 구성되어 `inner/22`~`inner/77`까지 들어가 있다.
- `assets/tarot-cards-imagegen/inner/`: 78장, 전부 1024x1536, 손상 없음.
- `assets/tarot-cards-imagegen/final/with-text/`: 78장, 전부 1024x1536, 손상 없음.
- `assets/tarot-cards-imagegen/final/no-text/`: 78장, 전부 1024x1536, 손상 없음.
- `assets/tarot-cards-imagegen/imagegen-prompt-queue.md`: `Total prompts: 0`.
- 최종 contact sheet:
  - `assets/tarot-cards-imagegen/preview/imagegen-with-text-contact-sheet.png`
  - `assets/tarot-cards-imagegen/preview/imagegen-no-text-contact-sheet.png`
- `assets/tarot-cards-imagegen/minor-story-bible.md`에 슈트별 스토리 설정을 추가했다.
- 기존 마이너 일부는 백업 폴더에 복사했다: `assets/tarot-cards-imagegen/attempts/replaced-inner/minor-pre-story/`
- Wands Four/Five, Swords court, Pentacles Ace~King까지 문제 지적된 카드는 반영 완료했다. 앞으로는 contact sheet를 기준으로 사용자가 지정한 카드만 개별 재생성하면 된다.

## 사용자의 최신 핵심 피드백

마이너 카드의 경우 각 카드가 너무 다르게 느껴지면 안 된다. 한 슈트 안에서는 하나의 스토리텔링이 있는 것처럼 보여야 한다.

인물 수는 적게 유지한다.

- 기본: 주인공 1명
- 꼭 필요한 경우: 조력자/상대 1명까지
- 동물은 여러 마리 나와도 괜찮다.
- Five of Wands처럼 여러 사람이 우르르 나오면 안 된다.

숫자 카드의 오브젝트 수는 명확해야 한다.

- Wands 4라면 막대 4개가 한눈에 보여야 한다.
- Wands 5라면 다섯 막대가 보이되, 사람이 5명일 필요는 없다.
- Cups/Swords/Pentacles도 마찬가지로 개수 가독성이 중요하다.

## Pi coin / 아이콘 관련 실수와 방지 규칙

큰 실수가 있었다. “Pi-inspired coin charm”을 너무 느슨하게 프롬프트에 넣었더니 어떤 이미지에서 코인이 Pi 문양이 아니라 두 개의 세로 타원 구멍만 있는 이상한 얼굴/스마일 코인처럼 나왔다.

다음 세션에서는 반복하지 말 것.

좋은 Pi coin motif:

- 둥근 금색 코인/메달 형태
- 수학 기호 π를 그대로 얹으면 안 된다. Pi Network 코인/앱 아이콘처럼 보여야 한다.
- 위쪽에 작은 네모 점 두 개
- 두 줄기를 이어주는 두껍고 둥근 블록형 상단 획
- 상단 획은 일직선 가로획이 아니라 연속된 둥근 브리지여야 한다. 왼쪽 어깨는 살짝 아래로 굽고, 오른쪽 끝은 공식 앱 아이콘처럼 살짝 위로 솟은 채워진 훅이어야 한다.
- 오른쪽은 구멍 난 C자/링/원형 루프가 아니다. 공식 아이콘처럼 상단 획 끝이 위로 올라간 굵은 팔이다.
- 오른쪽 훅은 그냥 직선 가로획이면 T자/π 글자처럼 보여서 실패지만, 원형 구멍을 뚫어도 실패다.
- 금화 위에서는 양각/음각 홈이나 은은한 보라색 에나멜 대비를 써서 아이콘 실루엣이 읽혀야 한다.
- 두 개의 세로 줄기와 상단 획이 연결된 아이콘형 엠보싱/각인
- 무문양 금화처럼 보이면 실패다. 모든 보이는 코인/메달은 Pi 코인답게 문양이 있어야 한다.
- 작아서 정확히 표현하기 어렵다면 코인을 더 크게 그리거나 코인 수를 줄여서라도 Pi Network 아이콘 형태가 읽히게 한다.
- 작은 반복 기호를 여러 개 뿌리지 말고, 큰 코인/메달 1~2개 위에 선명하게 새기는 쪽이 낫다.
- 공식 로고를 평면 벡터처럼 정확히 복붙하지 말고, 판타지 장신구/엠보싱 코인처럼 자연스럽게 표현
- Pi 문양이 꼭 금화/코인에만 있어야 하는 것은 아니다. 장면에 자연스럽게 어울리면 배경 부조, 축제 장식, 랜턴, 마법진, 정원 메달리온 같은 곳에도 가능하다.

나쁜 motif:

- 두 개의 세로 타원 구멍만 있는 코인
- 두 개의 세로 막대만 있어서 로마 숫자 II처럼 보이는 코인
- 수학 기호 π 글자를 그대로 얹은 코인
- T자/플러스 기호처럼 보이는 코인 문양
- 직선 가로획과 두 다리만 있는 코인 문양
- 오른쪽이 C자 구멍/링/원형 루프처럼 보이는 코인 문양
- 작은 π/아이콘 문양을 옷이나 배경에 과하게 반복해서 뿌린 장면
- 무문양 금화/메달
- 눈 달린 얼굴처럼 보이는 코인
- 스마일 코인
- 장면을 지배하거나 산만하게 만드는 과한 대형 Pi 로고

중요한 뉘앙스:

- 사용자는 작은 코인 디테일 자체는 좋아한다. 작은 코인을 금지하지 말 것.
- Pi-like emblem은 코인 참/메달/장신구뿐 아니라, 장면에 어울리는 배경 장식에도 사용할 수 있다.
- 배경 Pi는 금지가 아니다. 다만 배경 전체를 덮거나 브랜드 로고처럼 튀면 안 된다.
- 코인 형태는 사용자가 최종 contact sheet를 보고 필요한 카드만 재생성 요청할 예정이라고 했다. 명백한 오류가 아니면 전체 흐름을 멈추고 과도하게 수정하지 말 것.

## 금색 사용 관련 피드백

금색으로 반짝이게 표현한 것은 좋다고 했다. 하지만 너무 많이 쓰면 번잡스럽고 촌스러워 보인다고 했다.

다음 기준을 유지한다.

- 금색은 restrained accent로만 사용한다.
- 허용: coin charms, 얇은 장식선, 작은 별빛, 컵/검/지팡이의 아주 얇은 포인트
- 허용: 적당히 읽히는 황금 오브젝트/장식/문양. 사용자는 적당한 황금그림을 좋아한다.
- 허용: 주인공 옷의 작은 금색 문양도 너무 잘고 촘촘하지 않으면 괜찮다.
- 피하기: 화면을 뒤덮는 금색 체인, 금색 폭죽/컨페티, 큰 금속 면, 과도한 글리터
- 피하기: 사진 전체에 금가루를 뿌린 것처럼 전반적으로 반짝이는 처리, 옷 전체에 아주 자잘하게 반복되는 금가루/금문양
- 보라, 라벤더, 크림, 각 슈트의 원소색이 주색이어야 한다.

## 마이너 슈트별 스토리 방향

이미 `assets/tarot-cards-imagegen/minor-story-bible.md`에 정리되어 있다. 다음 세션은 이 파일을 먼저 읽고 따를 것.

### Wands: The Ember Trail

한 명의 불꽃 견습생이 주인공이다.

고정 요소:

- 짧은 검은 곱슬머리
- 보라 눈
- 보라 여행 망토
- 크림 튜닉
- 주황 스카프
- 별무늬 가방
- 작은 크림색 여우 동료
- 라벤더 산길, Ember Academy, 산속 마을 축제
- 살아있는 나무 지팡이, 잎과 부드러운 주황 불꽃

스토리:

Ace: 첫 지팡이 발견  
Two: 여정 계획  
Three: 멀리 바라봄  
Four: 마을 축제 도착, 정확히 네 지팡이 아치  
Five: 훈련/갈등. 사람을 많이 넣지 말 것. 주인공 1명 + 여우 + 떠오르는 연습 지팡이/동물 친구들로 표현 가능  
Six: 인정/승리  
Seven: 언덕 방어  
Eight: 빠른 전령/날아가는 지팡이  
Nine: 지친 경계  
Ten: 책임을 지고 지팡이 묶음 운반  
Page/Knight/Queen/King: 같은 주인공이 점점 성숙한 창조적 불의 모습으로 변한다.

사용자 피드백:

- Wands 1~3은 제대로 표현됐다.
- Wands 4는 어디가 막대 4개인지 모르겠다고 했다. 다시 만들 때 정확히 네 개의 지팡이가 큰 구조로 보여야 한다.
- Wands 5는 등장인물이 너무 많았다. 여러 사람 대신 주인공 중심으로 갈 것.

### Cups: The Pearlwater Village

물가 마을의 컵 키퍼가 주인공이다.

고정 요소:

- 부드러운 라벤더 브라운 머리
- 진주 머리핀
- 보라/크림 해변 옷
- 작은 물정령 동료
- 달빛 연못, 해변 정원, 분수 마당, 조용한 해안
- 진주빛 컵과 aqua glow

스토리:

감정의 시작, 관계, 축하, 내면화, 상실, 추억, 선택, 떠남, 만족, 공동체 행복, 그리고 Page~King으로 감정적 성숙.

### Swords: The Moonwind Academy

하늘/바람 학원의 학생이 주인공이다.

고정 요소:

- 은빛 검은 bob 머리
- 보라 아카데미 망토
- 크림 스카프
- 작은 올빼미 같은 바람 동료
- 달빛 학원, 안개 낀 해변, 바람 언덕, 조용한 예배당 같은 방, 강 건너기
- 은색 연습검과 푸른 바람빛

톤:

피/공포/폭력 금지. 지성, 갈등, 회복, 명료함으로 표현.

### Pentacles: The Coinseed Garden

코인 정원/공방의 어린 정원사 겸 제작자가 주인공이다.

고정 요소:

- 따뜻한 갈색 머리
- 초록-보라 앞치마
- 크림 셔츠
- 작은 새싹 마스코트
- 계단식 coinseed garden, 아늑한 공방, 마을 시장, 수확 온실
- 금색 코인씨앗/메달이 흙, 잎, 돌, 도구와 함께 있음

주의:

Pentacles는 금색 코인이 슈트 자체라 금색이 늘어나기 쉽다. 반드시 흙색, 초록, 보라, 크림을 넓게 쓰고 금색은 코인씨앗/메달 포인트로만 통제한다.

## 프롬프트 공통 골격

각 카드마다 아래 내용을 반복해서 일관성을 유지한다.

```text
Use case: stylized-concept
Asset type: inner illustration only for a Pi-inspired tarot card; fixed frame and English text will be added later.
Primary request: <CARD NAME> as scene <N> of the <SUIT> suit story, high-quality kawaii fantasy anime-inspired tarot illustration.
Suit continuity: <same protagonist/cast/setting details>.
Scene/backdrop: <specific scene in the suit story>.
Subject: <tarot symbolism with exact suit-object count when numbered>.
Pi motif: Pi-inspired marks may appear as readable shiny golden coin charms, medallions, jewelry, tools, or tasteful background ornaments/reliefs when they fit the scene. The emblem should resemble the Pi Network coin/app icon, not a plain mathematical Greek pi character: two small square dots above, a continuous rounded bridge with a left shoulder bending slightly downward and a right side rising into a solid upturned hook, plus two vertical stems below the bridge. The right side must look like the official app icon's filled upward hook, not a C-shaped loop, ring, or circular hole. Use raised and recessed engraving or subtle purple enamel around the relief so the icon silhouette is readable on gold. If a coin or medallion is visible, it should carry this embossed icon-like mark so it reads as a Pi coin rather than a generic gold disc. The motif must not look like a typed pi glyph, a T-shaped mark, a plus-sign mark, two standalone vertical bars, Roman numeral II, a straight horizontal cap with two legs, or a plain/no-emblem coin. Make the motif larger or use fewer motifs if needed so the icon shape is readable; prefer one or two clear larger coins/medallions over many tiny symbols.
Gold usage: readable golden ornaments/coin charms are welcome, but avoid gold-dust spray, all-over glitter, and tiny dense clothing speckles; suit colors dominate.
Composition: vertical 1024x1536 full-bleed inner art, no border or blank nameplate.
Constraints: inner illustration only; no tarot card frame, no border, no nameplate, no readable text, no words, no numbers, no watermark; Pi Network icon-like ornamental motifs are allowed when they fit the scene.
Avoid: oversized or distracting Pi logos that dominate the background, generic gold discs, plain mathematical Greek pi glyphs, typed pi symbols, T-shaped coin marks, plus-sign coin marks, plain/no-emblem coins, Roman numeral II coin marks, two standalone vertical-bar coin marks, straight-horizontal-cap coin marks, C-shaped right loops, right-side circular holes, many tiny repeated Pi marks, excessive metallic gold dust, all-over glitter, official-logo-perfect flat vector copy, malformed two-oval smiley coins, readable text, clutter.
```

## 다음 세션 권장 작업 순서

1. 이 문서와 `assets/tarot-cards-imagegen/minor-story-bible.md`를 읽는다.
2. 현재 worktree 상태를 확인한다.
3. 먼저 contact sheet 두 장을 열어 사용자가 지정한 카드가 있는지 확인한다.
4. 사용자가 개별 카드 재생성을 요청하면 `assets/tarot-cards-imagegen/references/pi-network-appstore-icon-512.jpg`를 `view_image`로 먼저 띄우고, 내장 imageGen 프롬프트에서 공식 아이콘의 두 점, 둥근 브리지, 두 줄기, 오른쪽 채워진 upturned hook을 참조하라고 지시한다. `pi-network-icon-shape-reference.png`는 C자 구멍처럼 오해될 수 있으니 쓰지 않는다.
5. 재생성은 카드 전체가 아니라 내부 일러스트만 만든다. 채택 후보를 `inner/`에 filename 그대로 넣고, 이전 이미지는 `attempts/replaced-inner/`에 백업한다.
6. 여러 장을 모은 뒤 또는 최종 확인 시 번들 Python으로 `tools/render_imagegen_deck.py`를 실행한다.
7. 최종 검증:
    - `final/with-text` 78장
    - `final/no-text` 78장
    - 전부 1024x1536
    - 한글 없음
    - 생성된 내부 일러스트에는 text/letters/numbers 없음
    - 프레임/네임플레이트/비율 동일
    - contact sheet 육안 확인

## 렌더링/검증 힌트

렌더러는 `final/with-text`와 `final/no-text`를 만든다.

```bash
/Users/kimhanbin/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 tools/render_imagegen_deck.py
```

카드 크기 검증은 Pillow가 있는 번들 Python으로 한다.

중요: 렌더러 스크립트는 이미 폰트 경로 문제를 한 번 고쳤다. 기본 `python3`에서 PIL이 없거나 대체 폰트가 생길 수 있으니 번들 Python을 우선 사용한다.

## 현재까지 배운 것

- 템플릿은 좋다. 전체 카드 생성이 아니라 내부 일러스트 합성이 맞다.
- Pi coin motif는 사용자의 기대보다 더 구체적으로 지시해야 한다.
- 작은 코인 디테일은 좋다. 금지하지 말 것.
- 큰 로고처럼 보이는 Pi 문양은 싫다. 배경 Pi도 가능하지만 장면을 지배하지 않게 하고, 핵심 코인/메달에는 Pi Network 아이콘형 엠보싱을 선명하게 넣을 것.
- 금색 반짝임은 장점이지만 과하면 번잡하다.
- 메이저는 카드별 개성이 강해도 괜찮다.
- 마이너는 슈트별로 같은 세계, 같은 주인공, 같은 감정선이 보여야 한다.
- 숫자 카드는 오브젝트 수가 읽혀야 한다.
- 사람을 많이 넣으면 산만하다. 마이너는 주인공 중심으로 갈 것.
- ImageGen 내장 도구는 `CODEX_HOME=/Users/kakao/.codex`가 잡혀 있으면 기본 생성 파일을 `/Users/kakao/.codex/generated_images/<thread-id>/ig_*.png`에 저장한다. 2026-06-19 테스트에서 현재 스레드는 `/Users/kakao/.codex/generated_images/019ed845-5fee-73c3-8d1e-cc73c9fa5f5c/`에 PNG가 생성되는 것을 확인했다. 프로젝트에서 사용할 이미지는 이 기본 저장 파일을 워크스페이스 후보 디렉토리로 복사해서 사용한다.
