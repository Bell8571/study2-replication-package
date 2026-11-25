#!/usr/bin/env python3
"""Verify every file listed in SHA256SUMS. Exit 0 if all match."""
import hashlib, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
bad = 0
for line in open(os.path.join(ROOT, "SHA256SUMS")):
    h, name = line.rstrip("\n").split("  ", 1)
    got = hashlib.sha256(open(os.path.join(ROOT, name), "rb").read()).hexdigest()
    if got != h:
        bad += 1; print("MISMATCH", name)
print(f"{bad} mismatch(es)"); sys.exit(1 if bad else 0)
