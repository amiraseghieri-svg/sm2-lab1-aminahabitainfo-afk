#!/usr/bin/env python3
"""
check_files.py — Verify all required files exist and are non-empty.

Usage:
    python3 check_files.py lab01
    python3 check_files.py lab02
"""

import os
import sys
import json

LAB = sys.argv[1] if len(sys.argv) > 1 else "lab01"

# ── Required file definitions ─────────────────────────────────────────────────

LAB01_REQUIRED = {
    "circuits": [
        "circuits/AND_Gate.circ",
        "circuits/OR_Gate.circ",
        "circuits/XOR_Gate.circ",
    ],
    "screenshots": (
        [f"screenshots/{gate}_{bits}.png"
         for gate in ["AND", "OR", "XOR"]
         for bits in ["00", "01", "10", "11"]]
        + ["screenshots/task1_1_installation.png",
           "screenshots/task1_1_interface_labeled.png"]
    ),
    "report": ["report.md"],
}

LAB02_REQUIRED = {
    "circuits": [
        "circuits/Half_Adder.circ",
        "circuits/Full_Adder.circ",
        "circuits/Adder_Subtractor_4bit.circ",
        "circuits/Multiplier_4bit.circ",
        "circuits/Logic_Unit_4bit.circ",
        "circuits/ALU_4bit.circ",
    ],
    "report": ["report.md"],
}

REQUIRED = LAB01_REQUIRED if LAB == "lab01" else LAB02_REQUIRED

# ── Points per category ───────────────────────────────────────────────────────
POINTS = {
    "circuits":    10,   # per circuit file
    "screenshots": 1.5,  # per screenshot (capped at 20 for lab01)
    "report":      5,    # for report.md existing
}

# ── Checks ────────────────────────────────────────────────────────────────────
score = 0.0
details = {}

for category, files in REQUIRED.items():
    cat_score = 0.0
    cat_details = {}

    for filepath in files:
        exists     = os.path.isfile(filepath)
        size_ok    = (os.path.getsize(filepath) > 200) if exists else False
        status     = "PASS" if (exists and size_ok) else (
                     "EMPTY" if exists else "MISSING")
        cat_details[filepath] = status

        if status == "PASS":
            pts = POINTS.get(category, 3)
            cat_score += pts

    # Cap screenshots at 20 pts total
    if category == "screenshots":
        cat_score = min(cat_score, 20)

    details[category] = {"files": cat_details, "category_score": round(cat_score, 1)}
    score += cat_score

# ── Bonus: extra screenshot folder count ─────────────────────────────────────
ss_dir = "screenshots"
if os.path.isdir(ss_dir):
    all_pngs = [f for f in os.listdir(ss_dir) if f.lower().endswith(".png")]
    big_pngs = [f for f in all_pngs
                if os.path.getsize(os.path.join(ss_dir, f)) > 10_240]
    details["screenshot_summary"] = {
        "total_png_files":    len(all_pngs),
        "non_empty_png_files": len(big_pngs),
    }

score = min(round(score), 50)  # cap file check at 50 pts

# ── Output ────────────────────────────────────────────────────────────────────
print(json.dumps(details, indent=2))
print(f"\nFILE_SCORE: {score}")
