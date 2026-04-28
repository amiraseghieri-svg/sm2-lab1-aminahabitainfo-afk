# Lab 01 Report — Logic Gates

> **Instructions:** Fill in every section below. Delete the placeholder text and
> replace it with your own answers. Submit this file as part of your repository.

---

## Student Information

| Field | Value |
|-------|-------|
| **Full Name** | *(Seghieri Amira )* |
| **Student ID** | *( 39408009 )* |
| **Section / Group** | *( Group 02 )* |
| **Submission Date** | *(enter date: 2026-04-28 )* |

---

## Part 1 — Truth Tables

Fill in the output column (Y) for each gate based on your simulation results.

### AND Gate — `Y = A · B`

| A | B | Y = A AND B |
|:-:|:-:|:-----------:|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

### OR Gate — `Y = A + B`

| A | B | Y = A OR B |
|:-:|:-:|:----------:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

### XOR Gate — `Y = A ⊕ B`

| A | B | Y = A XOR B |
|:-:|:-:|:-----------:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

---

## Part 2 — Questions

**Q1:** What happens to the AND gate output if one input is always 0?
Explain *why* this occurs.

> *(Your answer here — minimum 2 sentences)*

The output of the AND gate will always be 0, regardless of the value of the other input. This occurs because the AND gate performs a logical conjunction (logical multiplication), which requires both inputs to be 1 to produce an output of 1. If any input is 0, the condition is not met, forcing the output to be 0.
---

**Q2:** How is XOR different from OR? Give a specific numerical example
showing a case where they produce different outputs.

> *(Your answer here — minimum 2 sentences)*


An OR gate outputs 1 if at least one of its inputs is 1, whereas an XOR (exclusive OR) gate outputs 1 only when the inputs are different from each other.

A clear example is when both inputs are 1: The OR gate outputs 1 (since at least one input is 1), while the XOR gate outputs 0 (because the inputs are the same, not different).---

**Q3:** Which gate would you use to check if two 1-bit values are equal?
Explain your reasoning.

> *(Your answer here — minimum 2 sentences)*

I would use an XNOR gate. The reasoning is that the XNOR gate is the logical complement of the XOR gate; it outputs 1 only when both inputs are identical (either both 0 or both 1), which effectively serves as a comparison to check if two values are equal.---

## Part 3 — Summary

Write a paragraph (minimum **50 words**) describing what you learned from
this lab. What was new to you? What was challenging? What surprised you?

> *(Your summary here — at least 50 words)*

In this lab, I learned how to implement basic logic gates like AND, OR, and XOR using Logisim-evolution. Building the XOR gate using only basic gates was a new experience, as it required careful thinking about Boolean expressions. The most challenging part was ensuring that the circuit wiring was correct and that all screenshots were named exactly as required by the lab instructions. I was surprised by how effectively simple gates can be combined to perform complex logical operations, which gave me a better understanding of how digital systems are built from the ground up.---

## Part 4 — Circuit Screenshots

Include screenshots of your completed circuits below.
*(Add more as needed — right-click an image in your file manager and copy the
relative path, e.g. `screenshots/AND_11.png`)*

### AND Gate — Input A=1, B=1 (Y should be 1)
![AND gate A=1 B=1](screenshots/AND_11.png)

### OR Gate — Input A=1, B=0 (Y should be 1)
![OR gate A=1 B=0](screenshots/OR_10.png)

### XOR Gate — Input A=1, B=1 (Y should be 0)
![XOR gate A=1 B=1](screenshots/XOR_11.png)

---

*Lab 01 | Computer Organization & Digital Design*
