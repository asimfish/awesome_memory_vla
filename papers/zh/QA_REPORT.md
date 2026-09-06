# 中文翻译 QA 报告 / Translation QA report

翻译引擎：[SuperTranslate](https://github.com/asimfish/super_translate) `pdf_zh_translator`，后端 DeepSeek `deepseek-v4-pro`，`--preserve-graphics-text`（保留图内文字与数学密集标签）。每篇译后都跑了引擎自带的 `inspect` 逐页视觉比对；通过标准是零 error 级 issue。日期：2026-09-07。

| 论文 | 页数 | inspect 结果 | 处理 |
|---|---|---|---|
| EventVLA_2606.20092_zh.pdf | 23 | 0 issue | 一次通过 |
| TRACE_2606.14551_zh.pdf | 22 | 0 issue（修复后） | 见下 |
| SAI_2606.16490_zh.pdf | 16 | 1 issue，已核实为检测器误报 | 见下 |

## TRACE：两处修复

1. **第 18 页表 14 表头下的横线被译文涂销区盖住**（`table_structure_mismatch`，墨迹覆盖 1.00 → 0.02）。缩小涂销边距（`--margin 0.3`）无效，说明横线落在表头文字的原始包围框内。处理：从原版 PDF 第 18 页的绘图对象里读出这条线的精确几何（x 108.0–504.0，y 398.94，线宽 0.80pt），用 PyMuPDF 在译文同一位置补画。
2. **第 22 页表 17 表头字号缩到 5.76pt**（`font_size_drift`，原文 6.81pt）。处理：以 `--min-font-size 6.2 --skip-overflow` 重放，放不下的表头保留英文原文而不是缩字。

修复后 `inspect` 报告 0 issue。

## SAI：一处误报

`inspect` 报第 4 页图 2 中 x 184–253、y 259–299 的框内文字 "Robot B" 超出框底 5.6pt（`text_outside_frame`）。核实：

- 该标签位于图内，受 `--preserve-graphics-text` 保护，译文未改动它；原版与译文在该区域的文本对象（位置、内容）完全相同；
- 以 5× 放大对 x 170–270、y 245–315 区域做像素级比对：175,000 个像素中 **0** 个不同。

结论：这是检测器对竖排（旋转）文字外接框的误判，原版就是这样排的；译文保留了原版的图形与文字，不做修改。

## 复现

```bash
bash scripts/translate_core.sh EventVLA_2606.20092          # DeepSeek，需 DEEPSEEK_API_KEY
bash scripts/translate_core.sh TRACE_2606.14551 --margin 0.3 --min-font-size 6.2 --skip-overflow
bash scripts/translate_core.sh SAI_2606.16490 --skip-overflow
# TRACE 第 18 页横线补画：见本文件 §TRACE，PyMuPDF page.draw_line((108.0,398.94),(504.02,398.94), width=0.80)
```

翻译缓存（`*.translation-cache.jsonl`）与 inspect 报告（`*.inspect.json`）与 PDF 放在同一目录，可用 `--api-mode cache-only` 零成本重排。此前的 Google 引擎备胎版本已被替换。
