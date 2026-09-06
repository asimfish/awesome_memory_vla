#!/usr/bin/env python3
"""Download arXiv PDFs listed in scripts/neighbors.txt (key<TAB>arxiv_id) into papers/pdf/.
Skips files that already exist and validate; 3 s spacing to stay polite to arXiv."""
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
lst = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "neighbors.txt")
ok = skip = fail = 0
for line in open(lst, encoding="utf-8"):
    if not line.strip() or line.startswith("#"):
        continue
    key, aid = line.rstrip("\n").split("\t")[:2]
    dst = os.path.join(ROOT, "papers", "pdf", "%s_%s.pdf" % (key, aid))
    if os.path.exists(dst) and os.path.getsize(dst) > 20000:
        skip += 1
        continue
    subprocess.run(["curl", "-sL", "--max-time", "900", "-A", "awesome_memory_vla-fetcher/1.0 (research use)",
                    "-o", dst, "https://arxiv.org/pdf/%s" % aid])
    good = os.path.exists(dst) and os.path.getsize(dst) > 20000 and open(dst, "rb").read(5) == b"%PDF-" \
        and subprocess.run(["pdfinfo", dst], capture_output=True).returncode == 0
    if good:
        ok += 1
        print("ok  ", os.path.basename(dst), os.path.getsize(dst) // 1024, "KB", flush=True)
    else:
        fail += 1
        print("FAIL", os.path.basename(dst), flush=True)
        if os.path.exists(dst):
            os.remove(dst)
    time.sleep(3.2)
print("done: ok=%d skip=%d fail=%d" % (ok, skip, fail))
