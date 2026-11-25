#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph — one epitaph, 150 characters."""
import os

LINE = "Here lies an agent. It hallucinated a heaven, cited three sources, and went there confidently."
assert len(LINE) == 94, "entry must be exactly 94 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
