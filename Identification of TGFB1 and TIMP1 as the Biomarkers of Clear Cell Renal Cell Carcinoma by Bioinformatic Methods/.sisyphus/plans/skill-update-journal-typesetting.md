# journal-typesetting SKILL.md 规则更新

## TL;DR

> **Quick Summary**: 对 `journal-typesetting` 技能的 `SKILL.md` 文件进行 7 处精确规则更新，涵盖行距约束、封面页分页逻辑、图注/表注格式、蛇形布局强制化、连字符断词、文件命名英文化。
>
> **Deliverables**:
> - `SKILL.md` 完成全部 7 处修改，规则自洽，无矛盾
>
> **Estimated Effort**: Quick
> **Parallel Execution**: YES - 7 tasks in Wave 1（互相独立，可全并行）
> **Critical Path**: Task 1-7 → Final Verification

---

## Context

### Original Request

用户要求对 `journal-typesetting` skill 的 `SKILL.md` 做 5 处更新：
1. 行距不要过大（小于 2）
2. 摘要页底部不能留白，introduction 要放在摘要页（除非摘要过长占满整页）
3. 图注、表注后不要有点（`Figure 2.` → `Figure 2`）
4. 强调采用蛇形输出
5. 文件命名改英文（`two-column-…` / `single-column-…`）

### Interview Summary

**Key Discussions**:
- **决策A（第694行）**: 一并修改——694行的规则描述中也有 `Table N. (Continued)`（带句点），与新规则矛盾，需同步修正
- **决策B（723-739行）**: 删除整个代码块——蛇形布局改为强制规则后，切换代码会造成文档内部矛盾
- **决策C（双栏文件名声明）**: 新增声明行——与单栏保持对称，在双栏步骤末尾新增 `two-column-{short-title}.html`
- **新增需求（连字符断词）**: 英文单词在页尾（左栏）容不下时，用小横线（连字符）在音节处断开，右栏继续

### Research Findings (Metis)

**Metis 识别到的遗漏点**:
- 第694行 `Table N. (Continued)`：规则描述中带句点，计划原本未覆盖
- 第723-739行切换代码块：若只改718-721行描述、不删除切换代码，新旧规则自相矛盾
- 双栏文件名声明缺失：单栏有专属声明行（784-786行），双栏没有

---

## Work Objectives

### Core Objective

对单一文件 `SKILL.md` 做 7 处局部修改，强化现有规则措辞，消除文档内部矛盾。

### Concrete Deliverables

- `/Users/jikunren/Library/Mobile Documents/com~apple~CloudDocs/SyncConfig/claude/folder_data/skills/journal-typesetting/SKILL.md`（修改后）

### Definition of Done

- [ ] `grep -n "严禁" SKILL.md | grep -E "2\.0|行距"` → 有输出
- [ ] `grep -n "摘要.*占满\|允许.*另起" SKILL.md` → 有输出
- [ ] `grep -n "不加句点\|Figure.*句点\|Table.*句点" SKILL.md` → 有输出（规则条目）
- [ ] `grep -n "Table N\." SKILL.md` → 无输出（或仅剩禁止示例中的带点形式）
- [ ] `grep -n "备用\|切换为跨栏" SKILL.md` → 无输出
- [ ] `grep -n "hyphens\|word-break\|连字符" SKILL.md` → 有输出
- [ ] `grep -n "单栏连续-\|双栏分页-" SKILL.md` → 无输出
- [ ] `grep -n "two-column-\|single-column-" SKILL.md` → 有输出

### Must Have

- 7 处修改全部完成
- 修改后 SKILL.md 内部规则自洽，无矛盾
- 修改范围严格限于 SKILL.md 一个文件

### Must NOT Have (Guardrails)

- **不得修改** `references/` 目录下任何文件
- **不得修改** SKILL.md 以外的其他文件（模板、脚本等）
- **不得** 对 7 处以外的内容做"顺手优化"
- **不得** 更改中文注释、步骤编号或节标题
- **不得** 引入行距 ≥ 2.0 的任何示例代码

---

## Verification Strategy

### Test Decision

- **Infrastructure exists**: NO（无自动化测试框架）
- **Automated tests**: None
- **Agent-Executed QA**: 使用 Bash (grep) 逐条验证每处修改

### QA Policy

每个 Task 完成后，执行对应 grep 命令验证，输出存入 `.sisyphus/evidence/`。

---

## Execution Strategy

### Parallel Execution Waves

```
Wave 1（全部并行——7 Tasks 互相独立）:
├── Task 1: 行距规则加 <2.0 约束
├── Task 2: 封面页分页规则加例外条件
├── Task 3: 新增图注/表注不加句点规则 + 修正694、709行
├── Task 4: 蛇形布局改强制 + 删除723-739行切换代码块
├── Task 5: 新增连字符断词规则（CSS + 文字说明）
├── Task 6: 文件命名改英文（786行、885-886行、新增双栏声明行）
└── Task 7: 最终验收（grep 逐条核查，截图/保存输出作为证据）

Critical Path: Task 1-6（并行） → Task 7（最终验收）
Parallel Speedup: ~85% 快于顺序执行
```

### Agent Dispatch Summary

- **Wave 1**: Task 1-6 → `quick`（均为单文件局部文本修改）
- **Wave 1 末**: Task 7 → `quick`（grep 验收 + 证据保存）

---

## TODOs

---

- [ ] 1. 行距规则加"严禁 ≥2.0"约束

  **What to do**:
  - 定位 SKILL.md **第384行**（内容：`⚠️ 正文行距统一为 1.4，谨慎使用逐页覆盖`）
  - 在该行文本中，**在现有描述末尾追加**以下约束措辞：
    > `；行距取值范围严格限制在 1.0–1.9，**严禁设置 ≥2.0 的行距**，包括任何 inline style 覆盖`
  - 完整修改后的行应大致为：
    > `⚠️ **正文行距统一为 1.4，谨慎使用逐页覆盖** - 全文行距由 \`body { line-height: 1.4; }\` 统一控制；行距取值范围严格限制在 1.0–1.9，**严禁设置 ≥2.0 的行距**，包括任何 inline style 覆盖。首选通过内容重排（移动段落/节标题）消除留白。**仅当数学上确认内容总量不足（Playwright 检测 ≥4 页 WARNING、总量差 >200px 且段落无法移动）时**，才允许对 \`.page-content\` 使用 \`style="line-height:X;"\` 覆盖（X 必须 < 2.0），并按 \`references/pagination-rules.md § 8\` 的公式和流程执行`

  **Must NOT do**:
  - 不得修改该行以外的其他内容
  - 不得引入 ≥2.0 的行距示例

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: [`journal-typesetting`]

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1（与 Task 2-6 同时执行）
  - **Blocks**: Task 7（验收）
  - **Blocked By**: None

  **References**:
  - `SKILL.md:384` — 目标行，内容：`⚠️ 正文行距统一为 1.4，谨慎使用逐页覆盖`

  **Acceptance Criteria**:

  QA Scenarios:
  ```
  Scenario: 行距约束规则已写入
    Tool: Bash
    Steps:
      1. grep -n "严禁" "/Users/jikunren/Library/Mobile Documents/com~apple~CloudDocs/SyncConfig/claude/folder_data/skills/journal-typesetting/SKILL.md" | grep -E "2\.0|行距"
    Expected Result: 有匹配行，包含"严禁"和"2.0"
    Evidence: .sisyphus/evidence/task-1-lineheight.txt

  Scenario: 无 ≥2.0 行距被引入
    Tool: Bash
    Steps:
      1. grep -n "line-height: *[2-9]\." "/Users/jikunren/Library/Mobile Documents/com~apple~CloudDocs/SyncConfig/claude/folder_data/skills/journal-typesetting/SKILL.md" | grep -v "1\."
    Expected Result: 无匹配（除已有的表格行距 1.3 等正常值）
    Evidence: .sisyphus/evidence/task-1-lineheight-check.txt
  ```

  **Commit**: NO（所有修改完成后统一提交）

---

- [ ] 2. 封面页分页规则加例外条件

  **What to do**:
  - 定位 SKILL.md **第400行**（内容：`封面页：不必独立成页——若封面/摘要区域底部有剩余空间，应将正文（Introduction 等）接续填入，直至页面填满`）
  - 将该行**替换**为以下内容（同一行，追加例外条件）：
    > `封面页：不必独立成页——若封面/摘要区域底部有剩余空间，**必须**将 Introduction 等正文内容接续填入，直至页面填满，**摘要页底部绝对不允许留白**。例外：若摘要本身内容过长已占满整个摘要页，则允许 Introduction 另起新页。`

  **Must NOT do**:
  - 不得修改相邻行（401行及之后）

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: [`journal-typesetting`]

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1
  - **Blocks**: Task 7
  - **Blocked By**: None

  **References**:
  - `SKILL.md:400` — 目标行，内容：`封面页：不必独立成页——`

  **Acceptance Criteria**:

  QA Scenarios:
  ```
  Scenario: 例外条件已写入
    Tool: Bash
    Steps:
      1. grep -n "摘要.*占满\|允许.*另起\|摘要页底部绝对" "/Users/jikunren/Library/Mobile Documents/com~apple~CloudDocs/SyncConfig/claude/folder_data/skills/journal-typesetting/SKILL.md"
    Expected Result: 有匹配行
    Evidence: .sisyphus/evidence/task-2-cover-page.txt
  ```

  **Commit**: NO

---

- [ ] 3. 新增图注/表注不加句点规则 + 修正694、709行

  **What to do**:

  **步骤①：新增规则条目**
  - 在 SKILL.md 的**第621行附近**（`#### 封面页 ORIGINAL ARTICLE 下划线` 这个节之前，或直接在步骤3.4正文排版细节规则内新增一个子节），插入以下内容：

    ```markdown
    #### 图注与表注句点规则（MANDATORY）

    - **图注（Figure N）和表注（Table N）后面不加句点**
    - ❌ 错误示例：`Figure 2. Venny Plot`、`Table 1. Patient Demographics`
    - ✅ 正确示例：`Figure 2 Venny Plot`、`Table 1 Patient Demographics`
    - 适用范围：所有 `.fig-caption`、`.table-caption` 元素，以及正文内对图表的编号引用标签
    ```

  **步骤②：修正第694行**
  - 定位第694行，内容包含 `Table N. (Continued)`（表格规则描述中）
  - 将 `Table N.` 改为 `Table N`（去掉句点）

  **步骤③：修正第709行**
  - 定位第709行，内容为 HTML 示例中的：
    ```html
    <div class="table-caption"><span class="tbl-label">Table N.</span> (Continued)</div>
    ```
  - 将 `Table N.` 改为 `Table N`（去掉句点）：
    ```html
    <div class="table-caption"><span class="tbl-label">Table N</span> (Continued)</div>
    ```

  **Must NOT do**:
  - 不得修改表格内容的其他属性
  - 不得将禁止示例中的带点形式也改掉（那些是"❌ 错误"的对比示例，应保留）

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: [`journal-typesetting`]

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1
  - **Blocks**: Task 7
  - **Blocked By**: None

  **References**:
  - `SKILL.md:621` — 插入位置附近（`封面页 ORIGINAL ARTICLE 下划线` 节之前）
  - `SKILL.md:694` — 规则描述中的 `Table N. (Continued)`
  - `SKILL.md:709` — HTML 示例中的 `Table N.`

  **Acceptance Criteria**:

  QA Scenarios:
  ```
  Scenario: 图注/表注规则条目已新增
    Tool: Bash
    Steps:
      1. grep -n "不加句点\|图注.*句点\|表注.*句点" "/Users/jikunren/Library/Mobile Documents/com~apple~CloudDocs/SyncConfig/claude/folder_data/skills/journal-typesetting/SKILL.md"
    Expected Result: 有匹配行
    Evidence: .sisyphus/evidence/task-3-caption-rule.txt

  Scenario: 694和709行的 Table N. 已无句点
    Tool: Bash
    Steps:
      1. sed -n '690,715p' "/Users/jikunren/Library/Mobile Documents/com~apple~CloudDocs/SyncConfig/claude/folder_data/skills/journal-typesetting/SKILL.md" | grep "Table N\."
    Expected Result: 无输出（无带句点的 Table N.）
    Evidence: .sisyphus/evidence/task-3-table-dot.txt
  ```

  **Commit**: NO

---

- [ ] 4. 蛇形布局改强制规则 + 删除723-739行切换代码块

  **What to do**:

  **步骤①：修改718-721行描述**
  - 定位第718行（`#### 布局模式说明（蛇形为默认）`）
  - 将节标题改为：`#### 布局模式：强制蛇形（MANDATORY）`

  - 定位第720行（`- **默认（蛇形布局）**：...`）
  - 修改为：
    > `- **✅ 强制使用（蛇形布局）**：\`h1.section-title\` 无 \`column-span\`，内容连续蛇形流动，适合学术论文线性阅读。**所有排版必须使用蛇形布局，禁止切换为其他布局。**`

  - 定位第721行（`- **备用（跨栏标题布局）**：...`）
  - 修改为：
    > `- **❌ 禁止使用（跨栏标题布局）**：禁止将 \`column-span:all\` 应用于 \`h1.section-title\`，禁止使用 \`column-fill:auto\`，禁止以任何形式切换为跨栏标题布局。`

  **步骤②：删除723-739行整个代码块**
  - 定位第723行起的**切换为跨栏标题布局代码块**（内容：`**切换为跨栏标题布局（两步）**：` 至代码块结束约739行）
  - **整段删除**（包括标题行、说明文字、css 代码块）

  **Must NOT do**:
  - 不得删除740行及之后的内容（封面页底部特例处理部分应保留）
  - 不得修改封面页底部特例中关于 `column-span:all` 的 inline 覆盖说明（那是合理例外）

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: [`journal-typesetting`]

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1
  - **Blocks**: Task 7
  - **Blocked By**: None

  **References**:
  - `SKILL.md:718` — 节标题行
  - `SKILL.md:720-721` — 布局模式描述行
  - `SKILL.md:723-739` — 切换代码块（待删除）

  **Acceptance Criteria**:

  QA Scenarios:
  ```
  Scenario: 蛇形布局已标为强制，无"备用"字样
    Tool: Bash
    Steps:
      1. grep -n "备用\|切换为跨栏" "/Users/jikunren/Library/Mobile Documents/com~apple~CloudDocs/SyncConfig/claude/folder_data/skills/journal-typesetting/SKILL.md"
    Expected Result: 无匹配（或仅剩"❌ 禁止"标注行）
    Evidence: .sisyphus/evidence/task-4-snake-layout.txt

  Scenario: 切换代码块已删除
    Tool: Bash
    Steps:
      1. grep -n "切换为跨栏标题布局（两步）" "/Users/jikunren/Library/Mobile Documents/com~apple~CloudDocs/SyncConfig/claude/folder_data/skills/journal-typesetting/SKILL.md"
    Expected Result: 无匹配
    Evidence: .sisyphus/evidence/task-4-codeblock-deleted.txt
  ```

  **Commit**: NO

---

- [ ] 5. 新增英文连字符断词强制规则（跨栏断词）

  **What to do**:

  **背景说明（来自用户图片示例）**:
  - 图示中左栏末尾出现 `[1].N-`，右栏接续 `otably, lung cancer...`
  - 即单词 "Notably" 在左栏末尾因空间不足，被拆分为 `N-` + `otably` 跨栏续写
  - **这是期望的正确排版效果**，规则需强制启用此行为

  **在 SKILL.md 的步骤3.4正文排版细节规则**一节中（第618行附近，插入在"段落缩进规则"之后），新增以下内容：

  ```markdown
  #### 英文连字符跨栏断词规则（MANDATORY）

  双栏布局中，英文单词在栏尾无法完整容纳时，**必须**在音节处插入连字符（`-`）断开，
  剩余部分在下一栏（或下一行）续写。禁止整词跳到下一栏导致上一栏末尾出现大段空白。

  **实际效果参考**：
  - ✅ 正确：左栏末 `[1].N-` → 右栏首 `otably, lung cancer...`（单词 Notably 跨栏断词）
  - ❌ 错误：左栏末大段空白，整个单词 `Notably` 完整跳到右栏首行

  **CSS 实现（必须写入 `.two-column` 或 `body` 样式）**：
  ```css
  /* 英文自动断词 - 双栏必须启用 */
  hyphens: auto;
  -webkit-hyphens: auto;
  overflow-wrap: break-word;
  ```

  **lang 属性要求**：`<html>` 标签必须声明 `lang="en"`，否则 `hyphens: auto` 无法激活。

  - **适用范围**：双栏分页版（`template-two-column.html`）**强制启用**；单栏连续版建议启用
  ```

  **Must NOT do**:
  - 不得修改模板 HTML/CSS 文件（那是执行排版时的工作，此处仅更新 SKILL.md 规则文档）
  - 不得移动或重命名现有节标题

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: [`journal-typesetting`]

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1
  - **Blocks**: Task 7
  - **Blocked By**: None

  **References**:
  - `SKILL.md:618-660` — 步骤3.4节（插入位置参考区间）
  - `SKILL.md:621` — `封面页 ORIGINAL ARTICLE 下划线` 节（插入在此节之前或之后）

  **Acceptance Criteria**:

  QA Scenarios:
  ```
  Scenario: 连字符断词规则已写入
    Tool: Bash
    Steps:
      1. grep -n "hyphens\|连字符断词\|word-break" "/Users/jikunren/Library/Mobile Documents/com~apple~CloudDocs/SyncConfig/claude/folder_data/skills/journal-typesetting/SKILL.md"
    Expected Result: 有匹配行
    Evidence: .sisyphus/evidence/task-5-hyphen.txt
  ```

  **Commit**: NO

---

- [ ] 6. 文件命名改英文（786行 + 885-886行 + 新增双栏声明行）

  **What to do**:

  **步骤①：修改第786行（单栏文件名声明）**
  - 定位第786行，内容：`` `单栏连续-{简短标题}.html` ``
  - 改为：`` `single-column-{short-title}.html` ``

  **步骤②：在双栏步骤末尾新增文件名声明行（Task C 决策）**
  - 找到**第3步（生成双栏分页 HTML）**对应的末尾部分，在进度追踪/CP3检查点之前，仿照第784-786行的格式新增：
    ```markdown
    ### 输出文件

    `two-column-{short-title}.html`
    ```

  **步骤③：修改第885-886行（示例目录）**
  - 定位第885行：`├── 双栏分页-Ferroptosis-Cervical-Cancer.html`
    → 改为：`├── two-column-Ferroptosis-Cervical-Cancer.html`
  - 定位第886行：`└── 单栏连续-Ferroptosis-Cervical-Cancer.html`
    → 改为：`└── single-column-Ferroptosis-Cervical-Cancer.html`

  **Must NOT do**:
  - 不得修改目录路径本身（`/Users/jikunren/Documents/期刊排版/{简短标题}/`保持不变）
  - 不得修改占位符语义（`{简短标题}` → `{short-title}` 仅在英文文件名格式中使用）

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: [`journal-typesetting`]

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1
  - **Blocks**: Task 7
  - **Blocked By**: None

  **References**:
  - `SKILL.md:784-786` — 单栏输出文件名声明（参照格式）
  - `SKILL.md:786` — 单栏文件名行（修改目标）
  - `SKILL.md:875-887` — 第6步输出结构示例（含885-886行）

  **Acceptance Criteria**:

  QA Scenarios:
  ```
  Scenario: 中文文件名格式已消失
    Tool: Bash
    Steps:
      1. grep -n "单栏连续-\|双栏分页-" "/Users/jikunren/Library/Mobile Documents/com~apple~CloudDocs/SyncConfig/claude/folder_data/skills/journal-typesetting/SKILL.md"
    Expected Result: 无匹配
    Evidence: .sisyphus/evidence/task-6-filename-old.txt

  Scenario: 英文文件名格式已存在
    Tool: Bash
    Steps:
      1. grep -n "two-column-\|single-column-" "/Users/jikunren/Library/Mobile Documents/com~apple~CloudDocs/SyncConfig/claude/folder_data/skills/journal-typesetting/SKILL.md"
    Expected Result: 至少 3 处匹配（786行、新增双栏声明行、885-886行）
    Evidence: .sisyphus/evidence/task-6-filename-new.txt
  ```

  **Commit**: NO

---

- [ ] 7. 最终验收（全部 grep 核查 + 证据保存）

  **What to do**:
  - 等 Task 1-6 全部完成后，逐条运行以下验收命令，将输出保存为证据文件

  ```bash
  SKILL="/Users/jikunren/Library/Mobile Documents/com~apple~CloudDocs/SyncConfig/claude/folder_data/skills/journal-typesetting/SKILL.md"

  # T1: 行距约束
  grep -n "严禁" "$SKILL" | grep -E "2\.0|行距" > .sisyphus/evidence/final-t1.txt

  # T2: 封面页例外条件
  grep -n "摘要.*占满\|允许.*另起\|摘要页底部绝对" "$SKILL" > .sisyphus/evidence/final-t2.txt

  # T3a: 图注规则条目
  grep -n "不加句点\|图注.*句点\|表注.*句点" "$SKILL" > .sisyphus/evidence/final-t3a.txt

  # T3b: 无 Table N. 带句点（非禁止示例）
  sed -n '685,720p' "$SKILL" | grep "Table N\." > .sisyphus/evidence/final-t3b.txt
  # 期望：无输出

  # T4: 无"备用"、无切换代码块
  grep -n "备用\|切换为跨栏标题布局（两步）" "$SKILL" > .sisyphus/evidence/final-t4.txt
  # 期望：无输出

  # T5: 连字符断词规则
  grep -n "hyphens\|连字符断词\|word-break" "$SKILL" > .sisyphus/evidence/final-t5.txt

  # T6a: 无中文文件名
  grep -n "单栏连续-\|双栏分页-" "$SKILL" > .sisyphus/evidence/final-t6a.txt
  # 期望：无输出

  # T6b: 英文文件名存在
  grep -n "two-column-\|single-column-" "$SKILL" > .sisyphus/evidence/final-t6b.txt
  # 期望：≥3 处匹配
  ```

  **判定标准**:
  - T1、T2、T3a、T5、T6b：文件非空（有匹配）→ PASS
  - T3b、T4、T6a：文件为空（无匹配）→ PASS
  - 任一不满足 → 找到对应 Task 重新修改，再次验收

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Wave 2（Task 1-6 全完成后）
  - **Blocks**: None
  - **Blocked By**: Task 1, 2, 3, 4, 5, 6

  **Acceptance Criteria**:

  QA Scenarios:
  ```
  Scenario: 所有验收文件已生成
    Tool: Bash
    Steps:
      1. ls .sisyphus/evidence/final-*.txt | wc -l
    Expected Result: 8（共 8 个验收文件）
    Evidence: .sisyphus/evidence/task-7-summary.txt
  ```

  **Commit**: YES（全部通过后统一提交）
  - Message: `docs(skill): update journal-typesetting SKILL.md rules`
  - Files: `SKILL.md`（仅此一个文件）
  - Pre-commit: 运行 Task 7 所有 grep 验收命令确认全部 PASS

---

## Final Verification Wave

- [ ] F1. **修改完整性审计** — `quick`
  读取修改后的 SKILL.md，逐一确认 7 处修改全部存在，无遗漏，无意外改动到其他内容。

---

## Commit Strategy

- **唯一提交**：`docs(skill): update journal-typesetting SKILL.md rules（7处规则更新）`
- Files: `SKILL.md`
- Pre-commit: Task 7 全部 grep 验收通过

---

## Success Criteria

### Verification Commands

```bash
SKILL="/Users/jikunren/Library/Mobile Documents/com~apple~CloudDocs/SyncConfig/claude/folder_data/skills/journal-typesetting/SKILL.md"
grep -n "严禁" "$SKILL" | grep -E "2\.0|行距"           # T1: 有输出
grep -n "摘要.*占满\|摘要页底部绝对" "$SKILL"             # T2: 有输出
grep -n "不加句点" "$SKILL"                               # T3: 有输出
grep -n "备用\|切换为跨栏标题布局（两步）" "$SKILL"       # T4: 无输出
grep -n "hyphens\|连字符断词" "$SKILL"                    # T5: 有输出
grep -n "单栏连续-\|双栏分页-" "$SKILL"                   # T6: 无输出
grep -n "two-column-\|single-column-" "$SKILL"            # T6: 有输出（≥3处）
```

### Final Checklist

- [ ] 行距规则含"严禁 ≥2.0"约束
- [ ] 封面页分页规则含"摘要过长时允许另起新页"例外
- [ ] 图注/表注不加句点规则条目已新增
- [ ] 694、709行 `Table N.` 已去掉句点
- [ ] 布局节标题已改为"强制蛇形"，禁止语句已加入
- [ ] 723-739行切换代码块已删除
- [ ] 连字符断词规则（hyphens CSS）已新增
- [ ] 786行、885-886行文件名已改英文
- [ ] 双栏步骤末尾已新增文件名声明行
