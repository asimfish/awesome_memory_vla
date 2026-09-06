# Contributing to awesome_memory_vla

Thanks for helping keep this list useful. The repository is generated from a small set of source files, so please edit those rather than the generated outputs.

## Adding a paper

1. Add one line to `scripts/curated_ids.tsv` (tab-separated): `group<TAB>ShortKey<TAB>arxiv_id<TAB>venue year`.
   - `group` is one of `survey`, `bench`, `event`, `dense`, `latent`, `agentic`, `world`, `multi`, `background` (see `scripts/taxonomy.json`; `core` is reserved for the three deep-dive papers).
   - `ShortKey` is a CamelCase name without spaces (it becomes the file prefix of the note and the PDF).
   - `venue year` is optional; leave empty for arXiv preprints.
2. Add a one-line Chinese positioning for the paper to `scripts/oneliners_cn.json` under the same `ShortKey`. State what the paper does and, when it applies, the single number worth remembering. Only use numbers that appear in the paper or its abstract.
3. Regenerate everything:

```bash
python3 scripts/build_manifest.py   # fetches arXiv metadata (cached under translations/.cache_arxiv/)
python3 scripts/make_notes.py
python3 scripts/make_bib.py
python3 scripts/make_readme.py
python3 scripts/make_timeline.py
```

4. Open a pull request. Please do not hand-edit `README.md`, `README_en.md`, `notes/`, `awesome_memory_vla.bib` or `assets/timeline.svg`; they are overwritten by the scripts.

## Writing conventions

- Chinese first, English second for prose; both READMEs are generated from the same data.
- Entry format follows [awesome-ml4co](https://github.com/Thinklab-SJTU/awesome-ml4co): `**Title.** Venue Year. [paper] [pdf] [zh] [report] [note]`, then the author list in italics.
- Reports (`reports/`) lead with the claim, give every number with its source table, and keep limitations in one place instead of scattering caveats. Numbers from different papers are never compared as if they shared a protocol.
- Scripts stay ASCII-only; user-facing strings live in the JSON files under `scripts/` (the editor tooling used to build this repo is not UTF-8 safe for new files).

## Translations and PDFs

- `scripts/translate_core.sh <ShortKey>` runs SuperTranslate with the DeepSeek backend (needs `DEEPSEEK_API_KEY`); `scripts/translate_fallback_google.sh` is the key-free fallback.
- `python3 scripts/build_pdfs.py` rebuilds `reports/pdf/` and the consolidated `report/` HTML/PDF via headless Chrome.
- `cd slides && xelatex -interaction=nonstopmode awesome_memory_vla_deck.tex` (twice) rebuilds the Beamer deck; it needs the PingFang SC font (macOS) or another CJK font set in the preamble.

## Reporting problems

Open an issue with the arXiv id and what is wrong (wrong number, wrong group, broken link). Corrections to numbers should quote the table or sentence in the paper.
