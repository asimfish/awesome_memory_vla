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

## 14 篇邻居论文

逐篇的页数、体积与 inspect 结果见自动生成的 [QA_SUMMARY.md](QA_SUMMARY.md)。所有邻居论文都以 `--preserve-graphics-text --skip-overflow` 翻译。处理方式分三类：

**打了补丁（`scripts/zh_patches.json`，`apply_zh_patches.py` 可重放）**

| 论文 | 页 | 问题 | 处理 |
|---|---|---|---|
| MemoryVLA | 28 | 真机任务表最后几行被排成重叠乱码（`text_outside_frame` ×3） | 删除该区域的错排文本对象，叠回原版英文表行（x 100–512，y 561–671.5） |
| RoboMME | 1 | 第一作者姓名被翻成中文，上标 `1†` 掉到下一行（`preserved_ink_mismatch`） | 叠回原版作者行（y 142–169） |
| μVLA | 18 | 6 行方法对比表被排成一段散文（`table_cells_reflowed`） | 删除错排文本，叠回原版表格（y 335.8–389.5） |

**核实为误报或良性（不改）**

| 论文 | 页 | 报告 | 核实 |
|---|---|---|---|
| UniMem | 1 | 图内标签 "UniMem" 超框 8.7pt | 图内文字受保护未改动；与原版同区域 4× 放大像素比对 160,000 像素 0 差异 |
| Present but Not Remembered | 19 | 表头保留区墨迹 0.83 | 表头完好；检测窗口包含了上一行正文，中文比英文短所以墨迹变少 |
| MemoryVLA | 4 | 图 3 中 "Add & Norm" 标签越界 2.6pt ×2 | 图内标签，未改动 |

**接受的残留（可读，不值得再调 API）**

| 论文 | 页 | 残留 |
|---|---|---|
| Chronos | 18 | 致谢一行字号 8.25pt（原 9.96pt） |
| MemER | 22 | 附录提示词块字号 8.37pt（原 9.96pt） |
| MemoryVLA | 33, 34, 36 | 图内子图题保留英文（`--preserve-graphics-text` 的设计行为） |
| AGM | 3, 19, 20 | 图内任务指令文字保留英文；图 2 标签 "Observation" 越界 2.8pt |
| RoboMemArena | 19–21 | 附录任务表两行丢失列结构但中文内容完整可读；表内任务指令保留英文；两处标签越界 ≤ 7.9pt |

其余（KEMO、MEM、RMBench、HyMeS、AutoIntervene）一次通过，0 issue。

## 复现

```bash
bash scripts/translate_core.sh EventVLA_2606.20092          # DeepSeek，需 DEEPSEEK_API_KEY
bash scripts/translate_core.sh TRACE_2606.14551 --margin 0.3 --min-font-size 6.2 --skip-overflow
bash scripts/translate_core.sh SAI_2606.16490 --skip-overflow
python3 scripts/fetch_pdfs.py                               # 下载 scripts/neighbors.txt 的英文 PDF
python3 scripts/launch_detached.py scripts/lane_e.txt ...   # 邻居论文批量翻译（脱离终端）
python3 scripts/apply_zh_patches.py                         # 重放版式补丁（TRACE 横线、MemoryVLA / RoboMME / μVLA 叠回原版）
python3 scripts/make_zh_qa.py                               # 汇总 inspect 报告 → QA_SUMMARY.md
```

翻译缓存（`*.translation-cache.jsonl`）与 inspect 报告（`*.inspect.json`）与 PDF 放在同一目录，可用 `--api-mode cache-only` 零成本重排（注意：引擎逐条重试过的块不会进缓存，缺块时改用 API 模式加同一 `--cache-file`，只补翻缺失块）。此前的 Google 引擎备胎版本已被替换。
