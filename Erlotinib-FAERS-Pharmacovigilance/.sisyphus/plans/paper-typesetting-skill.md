# 历史研究格式排版 Skill 工作计划

## TL;DR

> **Quick Summary**: 基于现有期刊 HTML 模板与本地 Skill 规范，构建一个名为 `历史研究格式排版` 的 Skill，输出符合指定中文学术排版规则的 HTML（单栏连续 + 双栏分页），并固定英文为 `Times New Roman`。
>
> **Deliverables**:
> - `skills/历史研究格式排版/SKILL.md`
> - `skills/历史研究格式排版/assets/template-single-column.html`
> - `skills/历史研究格式排版/assets/template-two-column.html`
> - `skills/历史研究格式排版/references/style-mapping.md`
> - `skills/历史研究格式排版/references/italic-rules-pas.md`
> - `skills/历史研究格式排版/scripts/validate_layout.py`
>
> **Estimated Effort**: Medium
> **Parallel Execution**: YES - 3 waves
> **Critical Path**: Task 1 -> Task 2 -> Task 3/4 -> Task 5 -> Task 7

---

## Context

### Original Request
用户要求构建一个 Skill，对论文按“历史研究格式”进行排版，核心规格包括页面边距、36x35 版芯、字号字体、段落缩进、独立引文、脚注、标题层级，并补充：
- 英文字体固定 `Times New Roman`
- Skill 命名为 `历史研究格式排版`
- 新增 PAS 斜体规则：明确“应斜体/应正体”范围与边界情形

### Interview Summary
**Key Discussions**:
- 用户明确要求“先计划”。
- 排版规则已经明确到具体字号/行距/缩进。
- 新增命名与英文字体要求已确认。

**Research Findings**:
- 现有仓库有两个可复用模板：
  - `单栏连续-Erlotinib-FAERS-Pharmacovigilance.html`
  - `双栏分页-Erlotinib-FAERS-Pharmacovigilance.html`
- 本地 Skill 规范已存在成熟范式：`/Users/jikunren/.config/opencode/skills/journal-typesetting/SKILL.md`
- Skill 最小结构规范可复用：`/Users/jikunren/.config/opencode/skills/skill-creator/SKILL.md`
- 外部风格规范可引用：Chicago / MHRA / Oxford 对斜体边界规则有稳定共识

### Metis Review
**Identified Gaps (addressed)**:
- 输入/输出形态未完全指定 -> 默认输入为“粘贴文本或 Markdown”，默认输出为 HTML。
- 36x35 与双栏冲突风险 -> 采用模式化策略：单栏严格按 36x35 优先，双栏按等效版芯近似并给出校验告警。
- 脚注每页重排实现不清 -> 固定技术路线：Paged Media 能力优先（Paged.js/Prince 兼容层），并保留降级策略说明。

---

## Work Objectives

### Core Objective
创建一个可复用 Skill，使执行代理可将学术正文按“历史研究格式”稳定排版为 HTML，并具备可自动验证的排版规则检查能力。

### Concrete Deliverables
- Skill 元数据与触发说明（`SKILL.md`）
- 单栏连续模板（在线预览）
- 双栏分页模板（导出/PDF 友好）
- 样式映射与字号换算表（中文号数 -> pt）
- PAS 斜体规则文档（include/exclude/edge cases）
- 自动化校验脚本（边距、字号、行距、字体、脚注结构）

### Definition of Done
- [ ] `skills/历史研究格式排版/SKILL.md` 存在且 frontmatter 含 `name` 与 `description`
- [ ] 单栏与双栏模板均能输出目标样式（命令可验证）
- [ ] 正文/标题/摘要/关键词/引文/脚注规则均有机器可检验断言
- [ ] PAS 斜体 include/exclude 规则均有机器可检验断言
- [ ] 至少 1 组成功与 1 组失败 QA 场景可由代理执行并留存证据

### Must Have
- 边距：上 3.3cm、下 2.7cm、左 2.4cm、右 2.3cm
- 正文：小四宋体、首行 2 字符缩进、17.9pt 行距
- 英文：`Times New Roman`
- 脚注：页下脚注、每页单独排序、五号楷体、14.5pt
- PAS 斜体规则：
  - 斜体：独立著作/期刊报纸名/艺术品与长篇史诗/出版文集标题；未归化外语术语；法律案件名；船名；`ibid.`、`et al.`
  - 正体：文章与章节标题（引号内）；未出版档案与手稿描述；机构/地名/人名；已英语化外来词

### Must NOT Have (Guardrails)
- 不实现文献 DOI/PubMed/Crossref 自动补链（超出当前范围）
- 不引入大体积字体文件内嵌（仅使用字体栈与系统字体）
- 不把“人工目测”写成验收条件（必须命令/自动化可验）
- 不在实现阶段临时决定脚注策略（方案在计划中先锁定）
- 不使用纯启发式直接改写全部斜体（低置信度必须标记人工复核）

---

## Verification Strategy (MANDATORY)

> **UNIVERSAL RULE: ZERO HUMAN INTERVENTION**
>
> 本计划所有任务都必须由代理自动验证；禁止“用户手动检查/肉眼确认”。

### Test Decision
- **Infrastructure exists**: NO（仓库当前无现成测试框架）
- **Automated tests**: None（本次默认不先搭完整单元测试框架）
- **Framework**: `none`（使用脚本断言 + Agent-Executed QA 为主）

### Agent-Executed QA Scenarios (全任务通用要求)
- 前端/HTML：Playwright 打开输出，检查 DOM/CSS 计算值并截图
- CLI/脚本：`python3` 运行校验器，断言返回码与关键输出
- API 不涉及

统一证据目录：`.sisyphus/evidence/`

---

## Execution Strategy

### Parallel Execution Waves

Wave 1 (Start Immediately):
- Task 1: Skill 骨架与元数据
- Task 2: 规则映射表与配置层

Wave 2 (After Wave 1):
- Task 3: 单栏模板实现
- Task 4: 双栏模板实现

Wave 3 (After Wave 2):
- Task 5: 脚注每页编号策略
- Task 6: 渲染入口与模式切换

Wave 4 (After Wave 3):
- Task 7: 自动化校验与证据采集
- Task 8: Skill 文档收口与交付验收

Critical Path: Task 1 -> Task 2 -> Task 3/4 -> Task 5 -> Task 7

### Dependency Matrix

| Task | Depends On | Blocks | Can Parallelize With |
|------|------------|--------|----------------------|
| 1 | None | 3, 4, 6 | 2 |
| 2 | None | 3, 4, 5 | 1 |
| 3 | 1, 2 | 5, 6 | 4 |
| 4 | 1, 2 | 5, 6 | 3 |
| 5 | 3, 4 | 7 | 6 |
| 6 | 3, 4 | 7 | 5 |
| 7 | 5, 6 | 8 | None |
| 8 | 7 | None | None |

---

## TODOs

- [ ] 1. 建立 `历史研究格式排版` Skill 最小骨架

  **What to do**:
  - 创建目录：`skills/历史研究格式排版/`
  - 创建 `SKILL.md` frontmatter（`name`, `description`）
  - 创建子目录：`assets/`, `references/`, `scripts/`

  **Must NOT do**:
  - 不额外创建无关 README/变更日志（遵循 skill-creator 最小原则）

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: 结构搭建、低复杂度、规则明确
  - **Skills**: [`skill-creator`]
    - `skill-creator`: 确保目录与 SKILL.md 规范一致
  - **Skills Evaluated but Omitted**:
    - `journal-typesetting`: 本任务不涉及排版细节实现，仅建骨架

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Task 2)
  - **Blocks**: 3, 4, 6
  - **Blocked By**: None

  **References**:
  - `/Users/jikunren/.config/opencode/skills/skill-creator/SKILL.md:49` - Skill 必备结构（SKILL.md + 可选资源目录）
  - `/Users/jikunren/.config/opencode/skills/skill-creator/SKILL.md:68` - frontmatter 必填字段定义
  - `/Users/jikunren/.config/opencode/skills/journal-typesetting/SKILL.md:1` - 可参考的真实 Skill 头部写法

  **Acceptance Criteria**:
  - [ ] `skills/历史研究格式排版/SKILL.md` 存在
  - [ ] `SKILL.md` 包含 `name: 历史研究格式排版`
  - [ ] `assets/ references/ scripts/` 目录存在

  **Agent-Executed QA Scenarios**:
  ```text
  Scenario: Skill 骨架创建成功
    Tool: Bash
    Preconditions: 仓库可写
    Steps:
      1. 运行: ls "skills/历史研究格式排版"
      2. 断言输出包含: SKILL.md assets references scripts
      3. 运行: grep -n "^name:" "skills/历史研究格式排版/SKILL.md"
    Expected Result: 返回包含 name 字段且目录完整
    Evidence: .sisyphus/evidence/task-1-structure.txt

  Scenario: 缺少必填 frontmatter 被识别
    Tool: Bash
    Preconditions: 临时去除 description 字段（在测试副本）
    Steps:
      1. 对测试副本执行 frontmatter 检查脚本
      2. 断言脚本返回非 0
      3. 断言输出包含 "description missing"
    Expected Result: 失败被正确拦截
    Evidence: .sisyphus/evidence/task-1-frontmatter-fail.txt
  ```

  **Commit**: YES
  - Message: `feat(skill): scaffold 历史研究格式排版 skill`

---

- [ ] 2. 建立排版规则映射与配置常量

  **What to do**:
  - 在 `references/style-mapping.md` 固化规则：
    - 边距与版芯
    - 字体族（中英分离）
    - 中文号数字号到 pt 的映射（1号/小2/3号/小4/5号）
  - 新建 `references/italic-rules-pas.md`：
    - include/exclude 规则表
    - 例外词典（已英语化外来词、档案描述模板词）
    - 边界规则（首次外语词、重复出现、低置信度人工复核标记）
  - 明确 36x35 实施策略：单栏严格优先、双栏近似并告警

  **Must NOT do**:
  - 不把“经验值”写死在模板而不记录来源

  **Recommended Agent Profile**:
  - **Category**: `unspecified-low`
    - Reason: 规则设计 + 文档化，需严谨但不重算法
  - **Skills**: [`journal-typesetting`, `skill-creator`]
    - `journal-typesetting`: 可复用排版映射思路
    - `skill-creator`: 保持 SKILL 内外文档分层
  - **Skills Evaluated but Omitted**:
    - `pdf`: 本任务不做 PDF 文件处理实现

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Task 1)
  - **Blocks**: 3, 4, 5
  - **Blocked By**: None

  **References**:
  - `单栏连续-Erlotinib-FAERS-Pharmacovigilance.html:21` - `@page` 基础结构参考
  - `单栏连续-Erlotinib-FAERS-Pharmacovigilance.html:126` - 当前正文字体/行高写法（需替换为新规格）
  - `双栏分页-Erlotinib-FAERS-Pharmacovigilance.html:106` - 双栏布局关键属性 `column-count`
  - `双栏分页-Erlotinib-FAERS-Pharmacovigilance.html:284` - 双栏模板的 `@page` 位置
  - `https://developer.mozilla.org/en-US/docs/Web/CSS/@page` - `@page` 规范实现参考
  - `https://drafts.csswg.org/css-page-3/` - Paged Media 官方规范
  - `https://www.chicagomanualofstyle.org/` - 历史写作斜体边界权威来源
  - `https://www.mhra.org.uk/style/chapter3.html` - MHRA 斜体与标题规范

  **Acceptance Criteria**:
  - [ ] `style-mapping.md` 包含全部用户规格字段
  - [ ] 字号映射表至少覆盖：1号、小2、3号、小4、5号
  - [ ] 明确写出英文字体 `Times New Roman`
  - [ ] `italic-rules-pas.md` 覆盖 include/exclude/edge cases 三部分

  **Agent-Executed QA Scenarios**:
  ```text
  Scenario: 规则映射完整性校验
    Tool: Bash
    Preconditions: style-mapping.md 已生成
    Steps:
      1. grep -n "Times New Roman" "skills/历史研究格式排版/references/style-mapping.md"
      2. grep -n "36.*35" "skills/历史研究格式排版/references/style-mapping.md"
      3. grep -n "小4\|5号\|3号\|小2\|1号" "skills/历史研究格式排版/references/style-mapping.md"
      4. grep -n "独立出版\|法律案件\|船名\|未出版档案\|已英语化" "skills/历史研究格式排版/references/italic-rules-pas.md"
    Expected Result: 四条命令均匹配成功
    Evidence: .sisyphus/evidence/task-2-mapping-check.txt

  Scenario: 规则缺失触发失败
    Tool: Bash
    Preconditions: 测试副本移除“小4”映射
    Steps:
      1. 运行: python3 skills/历史研究格式排版/scripts/validate_layout.py --check-mapping test.md
      2. 断言退出码非 0
      3. 断言输出含 "missing size mapping"
    Expected Result: 缺失被准确报告
    Evidence: .sisyphus/evidence/task-2-mapping-fail.txt
  ```

  **Commit**: YES
  - Message: `docs(skill): add style mapping for 历史研究格式排版`

---

- [ ] 3. 实现单栏连续模板（历史研究格式）

  **What to do**:
  - 创建 `assets/template-single-column.html`
  - 应用目标边距、正文字体、缩进、行距
  - 定义标题层级与摘要/关键词块样式

  **Must NOT do**:
  - 不沿用英文模板的 Arial 标题/uppercase 样式

  **Recommended Agent Profile**:
  - **Category**: `visual-engineering`
    - Reason: CSS 版式与打印样式为核心
  - **Skills**: [`journal-typesetting`, `frontend-design`]
    - `journal-typesetting`: 复用论文排版结构经验
    - `frontend-design`: 高质量 CSS 结构化实现
  - **Skills Evaluated but Omitted**:
    - `ui-ux-pro-max`: 本任务偏印刷规范，不需要复杂交互动效

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Task 4)
  - **Blocks**: 5, 6
  - **Blocked By**: 1, 2

  **References**:
  - `单栏连续-Erlotinib-FAERS-Pharmacovigilance.html:28` - `@media print` 结构参考
  - `单栏连续-Erlotinib-FAERS-Pharmacovigilance.html:75` - 分页控制写法参考
  - `单栏连续-Erlotinib-FAERS-Pharmacovigilance.html:189` - 标题节点组织参考（仅结构复用）
  - `单栏连续-Erlotinib-FAERS-Pharmacovigilance.html:403` - 参考文献区域排版组织参考

  **Acceptance Criteria**:
  - [ ] `@page` 边距值等于 3.3/2.3/2.7/2.4cm（上右下左）
  - [ ] 正文 `font-family` 包含宋体栈，且英文回退 `Times New Roman`
  - [ ] 正文 `line-height: 17.9pt` 且 `text-indent: 2em`
  - [ ] 摘要/关键词标签与内容字体区分正确

  **Agent-Executed QA Scenarios**:
  ```text
  Scenario: 单栏样式正确生效
    Tool: Playwright (playwright skill)
    Preconditions: 本地可打开 template-single-column.html
    Steps:
      1. 打开 file://.../template-single-column.html
      2. 获取正文首段计算样式: fontFamily, lineHeight, textIndent
      3. 断言 fontFamily 包含 "SimSun" 或 "宋体"
      4. 断言 lineHeight 接近 "17.9pt"
      5. 截图 .sisyphus/evidence/task-3-single-style.png
    Expected Result: 样式计算值符合规则
    Evidence: .sisyphus/evidence/task-3-single-style.png

  Scenario: 标题误用英文字体被拦截
    Tool: Bash
    Preconditions: 模板中故意将 h1 改为 Arial（测试副本）
    Steps:
      1. grep -n "h1.*Arial" test-single.html
      2. 运行校验脚本
      3. 断言输出包含 "invalid title font"
    Expected Result: 违规被报告
    Evidence: .sisyphus/evidence/task-3-title-font-fail.txt
  ```

  **Commit**: YES
  - Message: `feat(template): add single-column history format layout`

---

- [ ] 4. 实现双栏分页模板（历史研究格式）

  **What to do**:
  - 创建 `assets/template-two-column.html`
  - 保留 `.page` 分页容器方案
  - 设置双栏规则与跨栏标题策略

  **Must NOT do**:
  - 不将 36x35 规则误写为“双栏每栏 36 字”

  **Recommended Agent Profile**:
  - **Category**: `visual-engineering`
    - Reason: 分栏 + 打印分页 + 页眉页脚样式
  - **Skills**: [`journal-typesetting`]
    - `journal-typesetting`: 双栏分页现成经验最贴近
  - **Skills Evaluated but Omitted**:
    - `frontend-ui-ux`: 不涉及交互式产品界面

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Task 3)
  - **Blocks**: 5, 6
  - **Blocked By**: 1, 2

  **References**:
  - `双栏分页-Erlotinib-FAERS-Pharmacovigilance.html:54` - `.page` 页面容器结构
  - `双栏分页-Erlotinib-FAERS-Pharmacovigilance.html:98` - `.page-content` 内容区结构
  - `双栏分页-Erlotinib-FAERS-Pharmacovigilance.html:106` - `column-count: 2` 双栏核心
  - `双栏分页-Erlotinib-FAERS-Pharmacovigilance.html:113` - `column-span: all` 跨栏元素策略
  - `双栏分页-Erlotinib-FAERS-Pharmacovigilance.html:268` - `page-break-after` 分页策略

  **Acceptance Criteria**:
  - [ ] 模板包含 `.page`、`.page-content.two-column`、页脚页码区域
  - [ ] 双栏列间距为可配置变量，不硬编码
  - [ ] 二级标题样式符合 3 号宋体要求

  **Agent-Executed QA Scenarios**:
  ```text
  Scenario: 双栏分页结构存在且可渲染
    Tool: Playwright (playwright skill)
    Preconditions: template-two-column.html 已生成
    Steps:
      1. 打开 file://.../template-two-column.html
      2. 断言存在 .page 元素数量 >= 1
      3. 断言 .page-content.two-column 的 columnCount 为 "2"
      4. 截图 .sisyphus/evidence/task-4-two-column.png
    Expected Result: 双栏结构和样式正确
    Evidence: .sisyphus/evidence/task-4-two-column.png

  Scenario: 缺失跨栏标题导致布局异常被检测
    Tool: Playwright (playwright skill)
    Preconditions: 测试副本移除 column-span
    Steps:
      1. 打开测试副本
      2. 检查首个 h1 是否被切入左栏
      3. 断言触发布局校验失败标记
    Expected Result: 报告“标题未跨栏”
    Evidence: .sisyphus/evidence/task-4-span-fail.png
  ```

  **Commit**: YES
  - Message: `feat(template): add two-column paged history format layout`

---

- [ ] 5. 锁定脚注“每页单独排序”实现策略

  **What to do**:
  - 采用 Paged Media 能力优先方案（Paged.js/兼容引擎）
  - 实现脚注样式：五号楷体，14.5pt，标号前后 1 字符空位
  - 设计降级行为：不支持每页重排时输出告警

  **Must NOT do**:
  - 不承诺在所有浏览器原生打印都可无差异实现“每页重排”

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
    - Reason: 涉及排版引擎差异与降级策略
  - **Skills**: [`journal-typesetting`, `pdf`]
    - `journal-typesetting`: 学术脚注语义与分页场景
    - `pdf`: HTML->PDF 约束理解
  - **Skills Evaluated but Omitted**:
    - `webapp-testing`: 非业务页面测试，重点在打印排版规则

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3 (with Task 6)
  - **Blocks**: 7
  - **Blocked By**: 3, 4

  **References**:
  - `https://www.princexml.com/howcome/2022/guides/footnotes/` - 每页脚注计数与 footnote 浮动实践
  - `https://drafts.csswg.org/css-page-3/` - Paged Media 规范依据
  - `双栏分页-Erlotinib-FAERS-Pharmacovigilance.html:284` - 当前 `@page` 组织位置

  **Acceptance Criteria**:
  - [ ] 脚注 CSS 指定楷体字体栈与 14.5pt 行距
  - [ ] 支持分页重置计数或明确降级提示
  - [ ] 校验脚本可识别脚注编号连续性/重置策略

  **Agent-Executed QA Scenarios**:
  ```text
  Scenario: 脚注按页重置生效
    Tool: Playwright (playwright skill)
    Preconditions: 启用 paged 模式并生成至少 2 页示例
    Steps:
      1. 加载示例并触发分页
      2. 读取第1页脚注标号末值（如 3）
      3. 读取第2页首个脚注标号（应为 1）
      4. 截图 .sisyphus/evidence/task-5-footnote-reset.png
    Expected Result: 第二页脚注从 1 开始
    Evidence: .sisyphus/evidence/task-5-footnote-reset.png

  Scenario: 运行环境不支持分页脚注时给出告警
    Tool: Bash
    Preconditions: 在不支持脚注浮动的渲染器上运行
    Steps:
      1. 执行渲染命令
      2. 断言 stdout/stderr 含 "footnote reset fallback"
      3. 断言退出码为 0（可降级但不中断）
    Expected Result: 明确降级提示，无静默失败
    Evidence: .sisyphus/evidence/task-5-footnote-fallback.txt
  ```

  **Commit**: YES
  - Message: `feat(layout): implement per-page footnote strategy`

---

- [ ] 6. 构建 Skill 渲染入口与模式切换

  **What to do**:
  - 在 `SKILL.md` 写清调用流程与输入格式
  - 提供渲染入口（脚本或指令约定）支持 `single` / `two-column`
  - 入口脚本固定为 `skills/历史研究格式排版/scripts/render.py`
  - 将字体、边距、字号映射为集中配置

  **Must NOT do**:
  - 不把模式切换分散在多个互不一致的硬编码开关

  **Recommended Agent Profile**:
  - **Category**: `unspecified-low`
    - Reason: 流程编排 + 配置落地
  - **Skills**: [`skill-creator`, `journal-typesetting`]
    - `skill-creator`: 技能触发与说明组织
    - `journal-typesetting`: 排版流程文档模板可复用
  - **Skills Evaluated but Omitted**:
    - `mcp-builder`: 本任务不新增 MCP server

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3 (with Task 5)
  - **Blocks**: 7
  - **Blocked By**: 3, 4

  **References**:
  - `/Users/jikunren/.config/opencode/skills/journal-typesetting/SKILL.md:66` - 复杂技能工作流写法参考
  - `/Users/jikunren/.config/opencode/skills/journal-typesetting/SKILL.md:74` - 进度追踪格式可复用
  - `/Users/jikunren/.config/opencode/skills/skill-creator/SKILL.md:202` - Skill 创建流程规范

  **Acceptance Criteria**:
  - [ ] `SKILL.md` 包含触发词、输入输出、模式选择
  - [ ] 单栏/双栏模式都可由同一入口触发
  - [ ] 英文字体规则在两种模式下一致生效

  **Agent-Executed QA Scenarios**:
  ```text
  Scenario: 单入口切换单栏成功
    Tool: Bash
    Preconditions: 渲染入口可执行
    Steps:
      1. 执行: python3 skills/历史研究格式排版/scripts/render.py --mode single --input skills/历史研究格式排版/references/sample.md --output .sisyphus/evidence/task-6-single.html
      2. 断言输出文件名包含 single
      3. grep -n "Times New Roman" .sisyphus/evidence/task-6-single.html
    Expected Result: single 模式文件生成且英文字体正确
    Evidence: .sisyphus/evidence/task-6-mode-single.txt

  Scenario: 非法模式参数被拒绝
    Tool: Bash
    Preconditions: 入口脚本存在参数校验
    Steps:
      1. 执行: python3 skills/历史研究格式排版/scripts/render.py --mode invalid --input skills/历史研究格式排版/references/sample.md --output .sisyphus/evidence/task-6-invalid.html
      2. 断言退出码非 0
      3. 断言输出含 "supported modes: single,two-column"
    Expected Result: 错误参数被准确拦截
    Evidence: .sisyphus/evidence/task-6-mode-fail.txt
  ```

  **Commit**: YES
  - Message: `feat(skill): add rendering entry and mode switch`

---

- [ ] 7. 实现自动化校验器与证据采集

  **What to do**:
  - 在 `scripts/validate_layout.py` 增加规则检查：
    - 边距（3.3/2.7/2.4/2.3cm）
    - 正文字体、英文字体、标题层级字号
    - 正文 17.9pt、脚注 14.5pt
    - PAS 斜体规则（应斜体命中、应正体误斜体拦截）
  - 输出机器可读报告（pass/fail + 原因）

  **Must NOT do**:
  - 不把失败仅打印 warning 后继续通过

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: 规则断言脚本，逻辑集中
  - **Skills**: [`journal-typesetting`]
    - `journal-typesetting`: 已有 style validator 思路可借鉴
  - **Skills Evaluated but Omitted**:
    - `ultrabrain`: 不涉及超高复杂推理

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Sequential
  - **Blocks**: 8
  - **Blocked By**: 5, 6

  **References**:
  - `/Users/jikunren/.config/opencode/skills/journal-typesetting/SKILL.md:38` - `style_validator.py` 参考存在性
  - `单栏连续-Erlotinib-FAERS-Pharmacovigilance.html:206` - `break-inside` 等可校验结构示例
  - `双栏分页-Erlotinib-FAERS-Pharmacovigilance.html:268` - 分页规则字段示例

  **Acceptance Criteria**:
  - [ ] `python3 skills/历史研究格式排版/scripts/validate_layout.py .sisyphus/evidence/task-6-single.html` 返回 0（规则全通过）
  - [ ] 至少 12 条规则断言（含 PAS 斜体 4 条以上）
  - [ ] 失败报告可定位到具体规则名

  **Agent-Executed QA Scenarios**:
  ```text
  Scenario: 合规样例通过全部校验
    Tool: Bash
    Preconditions: 生成合规 output.html
    Steps:
      1. python3 skills/历史研究格式排版/scripts/validate_layout.py output.html
      2. 断言退出码 0
      3. 断言输出含 "PASS: body_line_height_17_9pt"
    Expected Result: 所有规则通过
    Evidence: .sisyphus/evidence/task-7-validator-pass.txt

  Scenario: 边距错误触发失败
    Tool: Bash
    Preconditions: 构造 margin-top 非 3.3cm 的测试文件
    Steps:
      1. 运行校验器
      2. 断言退出码非 0
      3. 断言输出含 "FAIL: page_margin_top"
    Expected Result: 错误被精准识别
    Evidence: .sisyphus/evidence/task-7-validator-fail.txt

  Scenario: 应正体项目被误斜体时触发失败
    Tool: Bash
    Preconditions: 构造包含文章标题引号项且被 <em> 包裹的测试文件
    Steps:
      1. 运行校验器
      2. 断言退出码非 0
      3. 断言输出含 "FAIL: italic_overreach_article_title"
    Expected Result: 误斜体被精准拦截
    Evidence: .sisyphus/evidence/task-7-italic-overreach-fail.txt
  ```

  **Commit**: YES
  - Message: `test(skill): add automated layout validator`

---

- [ ] 8. 交付收口：Skill 文档完善与最终验收

  **What to do**:
  - 在 `SKILL.md` 完成完整工作流、限制说明、降级说明
  - 提供最小输入样例与双模式输出样例
  - 汇总验证命令与证据路径

  **Must NOT do**:
  - 不遗漏“脚注每页重排的兼容性限制”说明

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: 文档准确性和执行可操作性为核心
  - **Skills**: [`skill-creator`, `journal-typesetting`]
    - `skill-creator`: 避免无关文档膨胀，保持可触发性
    - `journal-typesetting`: 保持排版领域术语一致
  - **Skills Evaluated but Omitted**:
    - `doc-coauthoring`: 本任务为技能操作文档，不是跨团队协作文档项目

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Sequential (final)
  - **Blocks**: None
  - **Blocked By**: 7

  **References**:
  - `/Users/jikunren/.config/opencode/skills/skill-creator/SKILL.md:102` - 避免冗余文档的边界
  - `/Users/jikunren/.config/opencode/skills/skill-creator/SKILL.md:124` - 渐进加载与引用文件组织
  - `/Users/jikunren/.config/opencode/skills/journal-typesetting/SKILL.md:66` - 可执行流程段落组织示例

  **Acceptance Criteria**:
  - [ ] `SKILL.md` 可独立指导代理完成排版
  - [ ] 验证命令清单完整且均可执行
  - [ ] 双模式样例输出可由 QA 场景覆盖

  **Agent-Executed QA Scenarios**:
  ```text
  Scenario: 按 SKILL.md 运行成功产出双模式文件
    Tool: Bash
    Preconditions: 样例输入存在
    Steps:
      1. 按 SKILL.md 指令执行 single 模式
      2. 按 SKILL.md 指令执行 two-column 模式
      3. 断言两个输出文件都存在
    Expected Result: 文档可执行且不含歧义
    Evidence: .sisyphus/evidence/task-8-runbook-pass.txt

  Scenario: 缺失前置条件时文档能指导恢复
    Tool: Bash
    Preconditions: 临时移除输入样例
    Steps:
      1. 执行命令触发错误
      2. 按 SKILL.md 故障段落修复
      3. 再执行并成功
    Expected Result: 文档具备可操作排错能力
    Evidence: .sisyphus/evidence/task-8-runbook-recover.txt
  ```

  **Commit**: YES
  - Message: `docs(skill): finalize 历史研究格式排版 execution guide`

---

## Commit Strategy

| After Task | Message | Files | Verification |
|------------|---------|-------|--------------|
| 1 | `feat(skill): scaffold 历史研究格式排版 skill` | `skills/历史研究格式排版/*` | `ls skills/历史研究格式排版` |
| 2 | `docs(skill): add style mapping for 历史研究格式排版` | `references/style-mapping.md`, `references/italic-rules-pas.md` | `grep` 校验规则字段 |
| 3-4 | `feat(template): add history format templates` | `assets/template-*.html` | Playwright + grep |
| 5-6 | `feat(layout): footnote strategy and mode switch` | `SKILL.md` + 入口脚本 | 运行两种模式 |
| 7 | `test(skill): add automated layout validator` | `scripts/validate_layout.py` | `python3 validate_layout.py` |
| 8 | `docs(skill): finalize execution guide` | `SKILL.md` | 全流程 smoke run |

---

## Success Criteria

### Verification Commands

```bash
python3 "skills/历史研究格式排版/scripts/validate_layout.py" "skills/历史研究格式排版/assets/template-single-column.html"
# Expected: exit code 0 and PASS summary

python3 "skills/历史研究格式排版/scripts/validate_layout.py" "skills/历史研究格式排版/assets/template-two-column.html"
# Expected: exit code 0 and PASS summary

grep -n "Times New Roman" "skills/历史研究格式排版/assets/template-single-column.html"
# Expected: at least one match

grep -n "line-height:\s*17.9pt" "skills/历史研究格式排版/assets/template-single-column.html"
# Expected: match exists

python3 "skills/历史研究格式排版/scripts/validate_layout.py" --check-italics "skills/历史研究格式排版/assets/template-single-column.html"
# Expected: PASS for PAS include/exclude rules
```

### Final Checklist
- [ ] 所有 Must Have 均被规则化并可验证
- [ ] 所有 Must NOT Have 均未出现
- [ ] 双模式模板可生成
- [ ] 脚注策略有明确支持与降级说明
- [ ] 证据文件全部落在 `.sisyphus/evidence/`
