# Harden journal-typesetting for WebKit and integrity

## TL;DR

> **Quick Summary**: Strengthen `journal-typesetting` so two-column output is robust in WebKit/Comet, while keeping DOCX-to-HTML content integrity and stable pagination.
>
> **Deliverables**:
> - WebKit-safe two-column rendering guardrails
> - Automated content-integrity diff gate
> - Automated overflow/whitespace balancing gate
> - Browser parity verification (Chromium + WebKit)
> - Updated skill workflow and troubleshooting docs
>
> **Estimated Effort**: Medium
> **Parallel Execution**: YES - 3 waves
> **Critical Path**: Baseline fixtures -> rendering rules -> verification gates -> docs

---

## Context

### Original Request
Optimize the `journal-typesetting` skill based on this real typesetting iteration, especially the missing-text issue in section 2.2 seen in Comet/WebKit.

### Interview + Evidence Summary
- Real production symptom: paragraph content appears "missing" in two-column mode.
- Root cause class: WebKit multi-column rendering edge cases + clipping behavior.
- Existing checks are strong on visual balance in Chromium but weak on WebKit parity.
- One-off manual edits solved pages, but the skill itself needs reusable prevention and verification.

### Metis Review (addressed)
- Add explicit WebKit-safe rules; do not rely on `break-inside` alone.
- Do not depend on CSS `orphans/widows` for WebKit multicol correctness.
- Add deterministic integrity + pagination checks as mandatory gates.

---

## Work Objectives

### Core Objective
Convert current ad-hoc fixes into repeatable skill-level behavior that prevents hidden text, preserves template fidelity, and catches regressions before delivery.

### Concrete Deliverables
- Updated process spec in `~/.config/opencode/skills/journal-typesetting/SKILL.md`
- Updated two-column template rules in `~/.config/opencode/skills/journal-typesetting/assets/template-two-column.html`
- Added/updated verification scripts under `~/.config/opencode/skills/journal-typesetting/scripts/`
- Updated troubleshooting guidance in `~/.config/opencode/skills/journal-typesetting/references/troubleshooting.md`

### Definition of Done
- All regression fixtures pass integrity, overflow, and browser parity checks with zero manual inspection required.
- No paragraph text loss in two-column pages under WebKit verification.

### Must Have
- Deterministic integrity gate (source DOCX/markdown vs rendered HTML text sequence)
- WebKit-aware column-break protection strategy
- Automated evidence artifacts for every verification stage

### Must NOT Have (Guardrails)
- No global random CSS changes that deviate from template baseline
- No human-only acceptance criteria
- No Chromium-only "pass" considered final

---

## Verification Strategy (MANDATORY)

### Test Decision
- **Infrastructure exists**: YES (Python scripts and style validation tools already exist)
- **Automated tests**: Tests-after (script-based validation gates)
- **Framework**: Python CLI + Playwright browser automation

### Agent-Executed QA Scenarios (applies to all tasks)

Scenario: Integrity gate catches dropped sentence
  Tool: Bash (python)
  Preconditions: fixture source text and generated HTML exist
  Steps:
    1. Run integrity checker on fixture pair
    2. Assert checker exits non-zero for intentionally corrupted sample
    3. Assert report includes missing token span and page/section hint
  Expected Result: missing content is detected deterministically
  Evidence: `.sisyphus/evidence/integrity-gate-negative.json`

Scenario: Two-column WebKit render has no hidden text
  Tool: Playwright (webkit)
  Preconditions: generated two-column HTML exists
  Steps:
    1. Open generated HTML in WebKit context
    2. Capture per-page screenshots and computed page metrics
    3. Run OCR/text extraction on screenshot regions for target sections
    4. Assert expected phrases (including long 2.2 sentence) are present
  Expected Result: no section text disappears at column transitions
  Evidence: `.sisyphus/evidence/webkit-pages/` and `.sisyphus/evidence/webkit-text-check.json`

Scenario: Pagination gate enforces overflow thresholds
  Tool: Bash (node/python)
  Preconditions: page measurement script available
  Steps:
    1. Run page measurement for all pages
    2. Assert non-cover/non-last pages have no hard overflow
    3. Assert configured whitespace bounds are met
  Expected Result: balanced pages without clipped content
  Evidence: `.sisyphus/evidence/pagination-metrics.json`

---

## Execution Strategy

### Parallel Execution Waves

Wave 1 (start immediately)
- Task 1: Build regression fixture set
- Task 2: Define integrity-check contract

Wave 2 (after Wave 1)
- Task 3: Implement WebKit-safe rendering rules
- Task 4: Implement integrity checker
- Task 5: Implement browser parity verifier

Wave 3 (after Wave 2)
- Task 6: Implement pagination balancer gate
- Task 7: Update SKILL workflow and troubleshooting docs
- Task 8: End-to-end dry run and release checklist

Critical Path: 1 -> 3 -> 5 -> 8

### Dependency Matrix

| Task | Depends On | Blocks | Can Parallelize With |
|---|---|---|---|
| 1 | None | 3,4,5 | 2 |
| 2 | None | 4 | 1 |
| 3 | 1 | 8 | 4,5 |
| 4 | 1,2 | 8 | 3,5 |
| 5 | 1 | 8 | 3,4 |
| 6 | 3,5 | 8 | 7 |
| 7 | 3,4,5 | 8 | 6 |
| 8 | 3,4,5,6,7 | None | None |

---

## TODOs

- [ ] 1. Build regression fixture corpus (real failure patterns)

  **What to do**:
  - Create fixtures representing: 2.2 long paragraph split, long SOC/PT paragraphs, table-near-column breaks, page-end transitions.
  - Store expected phrase markers for each fixture.

  **Must NOT do**:
  - Do not use only synthetic toy text.

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high` (cross-cutting quality infrastructure)
  - **Skills**: `journal-typesetting`, `webapp-testing`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Task 2)

  **References**:
  - `~/.config/opencode/skills/journal-typesetting/SKILL.md` - current workflow checkpoints
  - `~/.config/opencode/skills/journal-typesetting/references/troubleshooting.md` - known failure classes

  **Acceptance Criteria**:
  - Fixture manifest exists with section-level expected phrases.
  - Negative fixture intentionally fails integrity check.

- [ ] 2. Define deterministic integrity-check contract

  **What to do**:
  - Specify normalization rules (spaces, punctuation, HTML entities) and what counts as loss.
  - Define pass/fail schema and machine-readable report format.

  **Must NOT do**:
  - No fuzzy manual judgment.

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: `journal-typesetting`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Task 1)

  **References**:
  - `~/.config/opencode/skills/journal-typesetting/SKILL.md`
  - `~/.config/opencode/skills/journal-typesetting/references/style-mapping.md`

  **Acceptance Criteria**:
  - Contract doc section added to SKILL workflow.
  - Example pass/fail report JSON schema documented.

- [ ] 3. Add WebKit-safe two-column rendering rules

  **What to do**:
  - Add WebKit-aware break rules for long paragraph blocks.
  - Introduce safe handling for column-spanning elements at transitions.
  - Add feature-checked overflow fallback (`clip/visible` when supported, deterministic fallback when not).
  - Keep template fidelity while reducing hidden-text risk.

  **Must NOT do**:
  - No broad visual redesign.

  **Recommended Agent Profile**:
  - **Category**: `visual-engineering`
  - **Skills**: `journal-typesetting`, `frontend-ui-ux`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 4,5)

  **References**:
  - `~/.config/opencode/skills/journal-typesetting/assets/template-two-column.html`
  - `~/.config/opencode/skills/journal-typesetting/references/style-mapping.md`

  **Acceptance Criteria**:
  - Long paragraphs crossing columns render complete text in WebKit fixture runs.
  - Fallback path is automatically selected when target engine lacks required overflow behavior.
  - No new hard overflow introduced in baseline fixtures.

- [ ] 4. Implement integrity checker script and gate

  **What to do**:
  - Add script under `scripts/` to compare normalized source text vs rendered text order.
  - Fail on dropped spans, duplicated spans, or section-order violations.

  **Must NOT do**:
  - Do not silently pass partial comparisons.

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
  - **Skills**: `journal-typesetting`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 3,5)

  **References**:
  - `~/.config/opencode/skills/journal-typesetting/scripts/style_validator.py`
  - `~/.config/opencode/skills/journal-typesetting/scripts/html_generator.py`

  **Acceptance Criteria**:
  - `python scripts/integrity_validator.py --fixture <name>` returns structured pass/fail.
  - Corrupted fixture fails with exact missing span output.

- [ ] 5. Implement browser parity verifier (Chromium + WebKit)

  **What to do**:
  - Add verification runner that renders both engines and compares expected section phrases.
  - Save screenshots and extracted text evidence.

  **Must NOT do**:
  - No single-engine success acceptance.

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
  - **Skills**: `playwright`, `journal-typesetting`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 3,4)

  **References**:
  - `~/.config/opencode/skills/journal-typesetting/SKILL.md`
  - `~/.config/opencode/skills/journal-typesetting/references/troubleshooting.md`

  **Acceptance Criteria**:
  - Command produces engine-specific artifacts for each fixture.
  - Any engine-specific missing phrase causes failure.

- [ ] 6. Add pagination balancer + thresholds

  **What to do**:
  - Define explicit thresholds for normal pages, cover page, and last page.
  - Add balancing iteration limits and deterministic move strategy.

  **Must NOT do**:
  - No unbounded loop or manual-only balancing.

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
  - **Skills**: `journal-typesetting`

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Wave 3

  **References**:
  - `~/.config/opencode/skills/journal-typesetting/assets/template-two-column.html`
  - `~/.config/opencode/skills/journal-typesetting/SKILL.md`

  **Acceptance Criteria**:
  - Metrics report flags only allowed exceptions (cover/last).
  - No hard overflow on normal content pages.

- [ ] 7. Update skill workflow and troubleshooting docs

  **What to do**:
  - Add mandatory gate order: integrity -> browser parity -> pagination -> delivery.
  - Add explicit WebKit failure signatures and remediation tree.

  **Must NOT do**:
  - No ambiguous “manual check as needed” wording.

  **Recommended Agent Profile**:
  - **Category**: `writing`
  - **Skills**: `journal-typesetting`, `doc-coauthoring`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3 (with Task 6)

  **References**:
  - `~/.config/opencode/skills/journal-typesetting/SKILL.md`
  - `~/.config/opencode/skills/journal-typesetting/README.md`
  - `~/.config/opencode/skills/journal-typesetting/references/troubleshooting.md`

  **Acceptance Criteria**:
  - Docs include deterministic gate commands and failure outcomes.
  - WebKit-specific checklist is explicit and reproducible.

- [ ] 8. End-to-end regression run and release gate

  **What to do**:
  - Run full fixture matrix through new gates.
  - Produce final machine-readable summary and human-readable release note.

  **Must NOT do**:
  - No release if any gate has critical failures.

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: `journal-typesetting`

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Final sequential

  **References**:
  - `~/.config/opencode/skills/journal-typesetting/scripts/`
  - `~/.config/opencode/skills/journal-typesetting/README.md`

  **Acceptance Criteria**:
  - Final report shows 100% pass on configured fixtures.
  - Evidence bundle path documented for audit.

---

## Success Criteria

### Verification Commands

```bash
python scripts/style_validator.py <two-column-output.html> --type two-column
python scripts/integrity_validator.py --fixture all
python scripts/browser_parity_check.py --engines chromium,webkit --fixture all
python scripts/pagination_metrics.py --fixture all
```

### Final Checklist
- [ ] WebKit hidden-text regression case is prevented
- [ ] Integrity checker detects injected drops and passes clean outputs
- [ ] Pagination gate has no hard overflow on normal pages
- [ ] SKILL docs encode new mandatory gate order
- [ ] Evidence artifacts are generated automatically
