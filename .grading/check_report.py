#!/usr/bin/env python3
"""
check_report.py — Validate the completeness of report.md.

Checks:
  1. Student name/ID fields are filled (not placeholder text)
  2. Truth tables are present (markdown table rows)
  3. Questions Q1, Q2, Q3 (Lab01) or Q1–Q4 (Lab02) have substantive answers
  4. Summary/reflection meets minimum word count
  5. (Lab02 only) Embedded images are present

Usage:
    python3 check_report.py lab01
    python3 check_report.py lab02
"""

import os
import re
import sys
import json

LAB = sys.argv[1] if len(sys.argv) > 1 else "lab01"

REPORT_PATH = "report.md"
QUESTIONS   = ["Q1", "Q2", "Q3"] if LAB == "lab01" else ["Q1", "Q2", "Q3", "Q4"]
MIN_WORDS   = 50  if LAB == "lab01" else 100
MAX_SCORE   = 15

# ── Load file ─────────────────────────────────────────────────────────────────

score   = 0.0
results = {}

if not os.path.isfile(REPORT_PATH):
    print(json.dumps({"error": "report.md not found"}))
    print(f"REPORT_SCORE: 0")
    sys.exit(0)

with open(REPORT_PATH, "r", encoding="utf-8", errors="replace") as fh:
    content = fh.read()

# ── Check 1: Student name / ID filled in ─────────────────────────────────────

PLACEHOLDER_PATTERNS = [
    r"\*\(enter your full name\)\*",
    r"\*\(enter your ID number\)\*",
    r"\*Your Full Name\*",
    r"\*Your ID\*",
]
has_placeholder = any(re.search(p, content, re.IGNORECASE)
                      for p in PLACEHOLDER_PATTERNS)

# Name line present and not still a placeholder
name_match = re.search(r"\*\*Full Name\*\*.*?[|:]\s*(.+)", content, re.IGNORECASE)
name_filled = (name_match is not None
               and len(name_match.group(1).strip()) > 3
               and not has_placeholder)

results["student_name_filled"] = name_filled
if name_filled:
    score += 2

# ── Check 2: Truth tables present ────────────────────────────────────────────

# Count markdown table data rows (line with | x | y | z | pattern)
table_rows = re.findall(r"^\|[\s\d]+\|[\s\d]+\|[\s\d*]+\|", content, re.MULTILINE)
num_table_rows = len(table_rows)

# Lab01 needs at least 12 rows (4 per gate × 3 gates)
required_rows = 12 if LAB == "lab01" else 8
tables_ok = num_table_rows >= required_rows

results["truth_table_rows_found"] = num_table_rows
results["truth_tables_complete"]  = tables_ok
if tables_ok:
    score += 3
elif num_table_rows >= 4:
    score += 1   # partial credit

# ── Check 3: Q&A answers present and substantive ─────────────────────────────

q_scores = {}
for q in QUESTIONS:
    # Find the question label and capture text until the next Q or section
    pattern = rf"(?i){re.escape(q)}\b[:\s\*]+(.*?)(?=\n#{1,3}|\bQ[1-4]\b|\Z)"
    match = re.search(pattern, content, re.DOTALL)
    if match:
        answer_text  = match.group(1).strip()
        # Strip markdown formatting for word count
        clean_answer = re.sub(r"[*_`#\[\]()>]", "", answer_text)
        word_count   = len(clean_answer.split())
        answered     = word_count >= 15  # at least 15 substantive words
    else:
        word_count = 0
        answered   = False

    q_scores[q] = {"word_count": word_count, "answered": answered}
    if answered:
        score += 2

results["question_answers"] = q_scores

# ── Check 4: Summary / reflection word count ─────────────────────────────────

# Look for the summary/reflection section
summary_match = re.search(
    r"(?i)(summary|reflection|conclusion)(.*)",
    content,
    re.DOTALL
)
if summary_match:
    summary_text  = summary_match.group(2)
    clean_summary = re.sub(r"[*_`#\[\]()>|]", "", summary_text)
    summary_words = len(clean_summary.split())
else:
    summary_words = len(content.split())   # fallback: whole document

results["summary_word_count"]   = summary_words
results["summary_min_required"] = MIN_WORDS
word_count_ok = summary_words >= MIN_WORDS

if word_count_ok:
    score += 3
elif summary_words >= MIN_WORDS // 2:
    score += 1  # partial credit

# ── Check 5: Embedded images (Lab02 only) ────────────────────────────────────

if LAB == "lab02":
    img_refs = re.findall(r"!\[.*?\]\(.*?\)", content)
    results["embedded_images"] = len(img_refs)
    if len(img_refs) >= 2:
        score += 3

# ── Final score ───────────────────────────────────────────────────────────────

score = round(min(score, MAX_SCORE))

print(json.dumps(results, indent=2))
print(f"\nREPORT_SCORE: {score}")
