# AGENTS.md — Erlotinib-FAERS-Pharmacovigilance

## 项目概述

本仓库为学术论文期刊排版产物，论文题目：

> **The pharmacovigilance analysis of adverse events of erlotinib based on the open access FAERS database**
> Zhang X, Wang Y — MedBA Medicine

---

## 文件说明

| 文件 | 用途 |
|------|------|
| `双栏分页-Erlotinib-FAERS-Pharmacovigilance.html` | **双栏A4分页版**，用于 PDF 下载打印，共11页 |
| `单栏连续-Erlotinib-FAERS-Pharmacovigilance.html` | **单栏连续版**，用于在线预览，含参考文献元数据链接 |
| `screenshots/` | Playwright 布局验证截图（FAILURE/WARNING 页面） |

---

## 排版规范

- **期刊**：MedBA Medicine（https://medbam.org）
- **主题色**：`#005a8c`
- **DOI 前缀**：`10.65079/`
- **Logo**：`https://medbam.org/assets/logo.png`
- **页面规格**：A4（210mm × 297mm），上边距25mm，下边距20mm，左右各20mm
- **内容区高度**：252mm（约952px @ 96DPI）

---

## 布局验证（Playwright）

验证标准（基于 96DPI，1mm ≈ 3.78px）：

| 状态 | 条件 |
|------|------|
| ✅ PASS | 无溢出 且 留白 < 57px（< 15mm） |
| ⚠️ WARNING | 留白 57–113px（15–30mm） |
| ❌ FAILURE | 溢出 > 0 或 留白 > 113px（> 30mm） |

最新验证结果（全部 PASS）：

| 页码 | 内容 | actualHeight | 留白 | 状态 |
|:---:|------|---:|---:|:---:|
| P1 | 封面 + Introduction 开头 | 945px | 7px | ✅ |
| P2 | Introduction 续 + Methods 2.1 | 922px | 30px | ✅ |
| P3 | Methods 2.2 统计方法 + 公式 | 898px | 54px | ✅ |
| P4 | Results 3.1 描述 + Table 2 | 907px | 45px | ✅ |
| P5 | Results 3.2 + 3.3 | 909px | 43px | ✅ |
| P6 | Table 3（SOC 信号强度） | 940px | 12px | ✅ |
| P7 | Table 4 Part 1（行1–20） | 950px | 2px | ✅ |
| P8 | Table 4 Part 2（行21–27）+ Discussion | 933px | 19px | ✅ |
| P9 | Discussion 续 + Conclusion + Acknowledgments | 923px | 29px | ✅ |
| P10 | Back matter + References [1]–[13] | 945px | 7px | ✅ |
| P11 | References [14]–[33] | 920px | 32px | ✅ |

---

## 参考文献链接

单栏版参考文献包含三类元数据链接（已验证）：
- **PubMed**：优先通过 DOI 或标题查询
- **Google Scholar**：全部文献均有
- **Crossref**：有 DOI 的文献均有

---

## 开发工具

- 排版技能：`journal-typesetting`（OpenCode skill）
- 布局验证：Playwright MCP（`playwright` skill）
- 验证脚本参考：`References/pagination-rules.md § Playwright 自动布局验证`

---

## 操作记录

| 日期 | 操作 |
|------|------|
| 2026-02-23 | 初始生成双栏版 + 单栏版 HTML |
| 2026-02-23 | Playwright 验证发现 P2/P3/P4/P5/P6/P11 共6页问题 |
| 2026-02-23 | 通过调整 `line-height` 修复所有问题，二次验证全部 PASS |
| 2026-02-23 | 创建 GitHub 仓库并推送 |
