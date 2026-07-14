# TDD Skill 업데이트 계획

## 배경 (출처: AI_TDD.pdf 34~35페이지)

"Agentic Engineering TDD 리뷰" — human-in-the-loop을 강조한 Agent 기반 TDD 진행 방식.

**3단계 사이클**
1. **RED**
   - 목표를 정확히 설정
   - `Plan.md` 생성을 요청하고, 사람 파트너가 검토
2. **GREEN**
   - RED에서 생성된 goal을 달성하도록 구현
   - 테스트가 실제로 통과하는지 체크
3. **Review**
   - GREEN의 코드를 리뷰
   - Plan 외의 사항이 구현되었는지 확인
   - 리팩토링이 필요하다면 요청

**커밋 포인트** (agentic engineering 수행 체크용, 단계별 커밋 생성)
- RED 단계에서 생성된 `Plan.md` → 커밋
- GREEN 단계의 코드를 검토 후 → 커밋

## 현재 tdd-skill(SKILL.md)과의 갭

- 현재 스킬은 순수 **Red → Green → Refactor** 3단계만 정의하고 있고, Plan.md 생성/검토 단계가 없음.
- "테스트 작성"이 RED의 전부이며, 그 앞에 오는 "목표 설정 + 계획 문서화 + 사람 검토" 단계가 빠져 있음.
- 별도의 **Review** 단계(Plan 대비 초과 구현 여부 확인)가 없고, Refactor에 흡수되어 있어 human-in-the-loop 검토 지점이 약함.
- 커밋 타이밍(언제, 무엇을 커밋할지)에 대한 가이드가 전혀 없음.
- 검증 체크리스트에 "Plan.md 범위를 벗어난 구현이 없는지" 항목이 없음.

## 변경 제안

1. **RED 단계 확장**
   - 실패하는 테스트를 쓰기 전에, 다음을 선행 단계로 추가:
     - 이번 증분의 목표를 정확히 정의
     - `Plan.md`(또는 해당 증분 계획) 생성 요청
     - 사람 파트너의 계획 검토를 거친 뒤에만 테스트 작성으로 진행
   - `Plan.md` 커밋 시점을 RED 단계 완료 지점으로 명시

2. **GREEN 단계**
   - 기존 내용 유지: Plan.md의 goal을 달성하는 최소한의 구현, 테스트 통과 확인
   - "Plan에 없는 기능/설계를 추가하지 않는다"는 제약을 명시적으로 추가

3. **Review 단계 신설** (Refactor 앞에 별도 단계로 삽입)
   - GREEN에서 나온 코드를 리뷰
   - Plan.md 범위를 벗어나 구현된 것이 있는지 체크 (있다면 되돌리거나 별도 승인)
   - 리팩토링 필요 여부 판단 → 필요 시 사람 파트너에게 요청
   - 리뷰 완료 후 코드 커밋

4. **커밋 체크리스트 추가** (새 섹션)
   - RED 완료 → `Plan.md` 커밋
   - GREEN 코드 Review 완료 → 구현 코드 커밋
   - 커밋 메시지에 어느 단계(RED/GREEN/Review)의 산출물인지 드러나게 작성

5. **사이클 다이어그램 업데이트**
   - 기존: RED → GREEN → REFACTOR
   - 신규: RED(목표설정+Plan.md 생성/검토) → GREEN(구현+테스트통과) → REVIEW(Plan 대비 검토+커밋) → REFACTOR(필요시) → 다음 RED

6. **검증 체크리스트 항목 추가**
   - [ ] Plan.md가 RED 단계에서 생성되고 사람 파트너 검토를 거쳤다
   - [ ] GREEN 코드가 Plan.md 범위를 벗어나지 않았다 (벗어났다면 별도로 식별/승인됨)
   - [ ] RED(Plan.md)와 GREEN(Review 후 코드) 각각 커밋되었다

## 적용 범위 (SKILL.md 내 수정 대상 섹션)

- `## Red-Green-Refactor` 다이어그램 및 하위 RED/GREEN/REFACTOR 서술
- `## 반복` 직전에 `## Review` 섹션 신설
- `## 검증 체크리스트`
- 신규 섹션: `## 커밋 시점` (Plan.md 커밋 / 코드 커밋 규칙)
- 예시(Good/Bad) 섹션에 Plan.md 예시 1개 추가 검토

## 다음 단계

1. 이 계획에 대해 사람 파트너(사용자) 승인
2. 승인 후 `.claude/skills/tdd-skill/SKILL.md` 실제 수정
3. 수정된 스킬을 적용해 bowling kata 재구현 진행 (RED에서 Plan.md 생성/검토 → GREEN → Review → 커밋 순으로)
