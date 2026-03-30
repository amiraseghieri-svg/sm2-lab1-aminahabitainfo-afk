#!/usr/bin/env python3
"""
check_circ_xml.py — Parse Logisim-Evolution .circ files (XML) and verify
that required circuit components are present.

Logisim .circ files are standard XML. Key elements we look for:
  <comp lib="..." name="AND Gate" .../>   ← gate components
  <comp name="Pin" .../>                  ← input/output pins
  <wire from="(x,y)" to="(x,y)"/>        ← wiring connections

Usage:
    python3 check_circ_xml.py lab01
    python3 check_circ_xml.py lab02
"""

import xml.etree.ElementTree as ET
import os
import sys
import json

LAB = sys.argv[1] if len(sys.argv) > 1 else "lab01"

# ── Helper ────────────────────────────────────────────────────────────────────

def parse_circ(filepath):
    """Return (xml_string_upper, tree) or (None, None) on failure."""
    if not os.path.isfile(filepath):
        return None, None
    try:
        tree = ET.parse(filepath)
        xml_str = ET.tostring(tree.getroot(), encoding="unicode").upper()
        return xml_str, tree
    except ET.ParseError as exc:
        return f"PARSE_ERROR: {exc}", None


def count_component(xml_str, name):
    """Count occurrences of a named component (case-insensitive)."""
    return xml_str.count(f'NAME="{name.upper()}"')


def has_wires(xml_str):
    return "<WIRE " in xml_str and xml_str.count("<WIRE ") >= 2


def has_pins(xml_str, min_count=2):
    return xml_str.count('NAME="PIN"') >= min_count

# ── Lab-specific checks ───────────────────────────────────────────────────────

LAB01_CHECKS = {
    "circuits/AND_Gate.circ": {
        "required_gates": ["AND Gate"],
        "min_pins": 2,
        "label": "AND Gate circuit",
        "max_pts": 15,
    },
    "circuits/OR_Gate.circ": {
        "required_gates": ["OR Gate"],
        "min_pins": 2,
        "label": "OR Gate circuit",
        "max_pts": 15,
    },
    "circuits/XOR_Gate.circ": {
        "required_gates": ["XOR Gate"],
        "min_pins": 2,
        "label": "XOR Gate circuit",
        "max_pts": 15,
    },
}

LAB02_CHECKS = {
    "circuits/Half_Adder.circ": {
        "required_gates": ["XOR Gate", "AND Gate"],
        "min_pins": 2,
        "label": "Half Adder",
        "max_pts": 8,
    },
    "circuits/Full_Adder.circ": {
        "required_gates": ["XOR Gate"],
        "min_pins": 2,
        "label": "Full Adder",
        "max_pts": 8,
    },
    "circuits/Adder_Subtractor_4bit.circ": {
        "required_gates": ["XOR Gate"],
        "min_pins": 2,
        "label": "4-bit Adder/Subtractor",
        "max_pts": 8,
    },
    "circuits/Logic_Unit_4bit.circ": {
        "required_gates": ["AND Gate", "OR Gate", "XOR Gate"],
        "min_pins": 2,
        "label": "4-bit Logic Unit",
        "max_pts": 8,
    },
    "circuits/ALU_4bit.circ": {
        "required_gates": [],
        "special": ["MUX"],
        "min_pins": 2,
        "label": "Complete 4-bit ALU",
        "max_pts": 13,
    },
}

CHECKS = LAB01_CHECKS if LAB == "lab01" else LAB02_CHECKS

# ── Run checks ────────────────────────────────────────────────────────────────

total_score = 0.0
all_results = {}

for filepath, spec in CHECKS.items():
    xml_str, tree = parse_circ(filepath)
    file_result   = {"label": spec["label"], "checks": {}, "score": 0}

    if xml_str is None:
        file_result["error"] = "File not found"
        all_results[filepath] = file_result
        continue

    if xml_str.startswith("PARSE_ERROR"):
        file_result["error"] = xml_str
        all_results[filepath] = file_result
        continue

    pts = 0
    max_pts = spec.get("max_pts", 10)

    # Check required gates
    for gate in spec.get("required_gates", []):
        found = count_component(xml_str, gate) > 0
        file_result["checks"][f"has_{gate.replace(' ', '_')}"] = found
        if found:
            pts += max_pts / (len(spec.get("required_gates", [gate])) + 2)

    # Check special components (MUX, etc.)
    for special in spec.get("special", []):
        found = special.upper() in xml_str
        file_result["checks"][f"has_{special}"] = found
        if found:
            pts += max_pts * 0.3

    # Check pins
    pins_ok = has_pins(xml_str, spec.get("min_pins", 2))
    file_result["checks"]["has_input_output_pins"] = pins_ok
    if pins_ok:
        pts += max_pts * 0.2

    # Check wiring
    wired = has_wires(xml_str)
    file_result["checks"]["has_wiring"] = wired
    if wired:
        pts += max_pts * 0.15

    file_result["score"] = round(min(pts, max_pts), 1)
    total_score += file_result["score"]
    all_results[filepath] = file_result

# ── Output ────────────────────────────────────────────────────────────────────

total_score = round(total_score)
print(json.dumps(all_results, indent=2))
print(f"\nXML_SCORE: {total_score}")
