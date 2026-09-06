#!/usr/bin/env python3
"""Start translation lanes detached from the calling terminal (new session / process group), so they
survive when the editor's terminal registry is reset. Usage:
    python3 scripts/launch_detached.py scripts/lane_e.txt scripts/lane_f.txt ...
Each lane logs to translations/logs/<lane>.out; poll those files to follow progress."""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for lane in sys.argv[1:]:
    name = os.path.splitext(os.path.basename(lane))[0]
    out = open(os.path.join(ROOT, "translations", "logs", name + ".out"), "a")
    p = subprocess.Popen(["bash", os.path.join(ROOT, "scripts", "translate_queue.sh"), lane],
                         cwd=ROOT, stdout=out, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,
                         start_new_session=True)
    print("started %s pid=%d -> translations/logs/%s.out" % (name, p.pid, name))
