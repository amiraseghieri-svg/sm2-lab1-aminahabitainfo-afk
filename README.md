# 🔬 Lab 01 — Getting Started with Logic Simulation
### Course: Computer Organization & Digital Design
### Lab Title: Tool Setup + Basic Logic Gates (AND, OR, XOR)

---

> **👋 Welcome!**
> This is your very first hands-on lab in digital design. Don't worry if you have
> never built a circuit before — this lab walks you through everything step by step,
> from installing the software to building and testing your first logic gates.
> Take it one step at a time, and you'll do great!

---

## 📋 Table of Contents
1. [Objectives](#-objectives)
2. [Theory — Logic Gates Explained](#-theory--logic-gates-explained)
3. [Task 1.1 — Install & Configure Logisim-Evolution](#️-task-11--install--configure-logisim-evolution)
4. [Task 1.2 — AND Gate Circuit](#️-task-12--build-and-simulate-the-and-gate)
5. [Task 1.3 — OR Gate Circuit](#️-task-13--build-and-simulate-the-or-gate)
6. [Task 1.4 — XOR Gate Circuit](#️-task-14--build-and-simulate-the-xor-gate)
7. [Task 1.5 — Lab Report](#-task-15--lab-report)
8. [Repository File Structure](#-repository-file-structure)
9. [Grading Rubric](#-grading-rubric)
10. [Submission Instructions](#-submission-instructions)
11. [Common Problems & Solutions](#-common-problems--solutions)

---

## 🎯 Objectives

By the end of this lab, you will be able to:

1. Download, install, and configure **Logisim-Evolution** on your computer
2. Create a new circuit project inside Logisim
3. Build and simulate **three fundamental logic gate circuits** (AND, OR, XOR)
4. Read and interpret simulation output (wire colours, signal values)
5. Capture screenshots as evidence of your working circuits
6. Submit your work through **GitHub Classroom**

---

## 📖 Theory — Logic Gates Explained

### What Is a Logic Gate?

A **logic gate** is the most basic building block of every digital computer.
It is an electronic component that takes one or more binary inputs and produces
a single binary output based on a fixed logical rule.

Everything a computer does — adding numbers, storing data, running programs —
ultimately comes down to millions of these tiny gates working together.

### Binary Inputs: What Do 0 and 1 Mean?

In digital electronics, every signal is either:
- **0 (LOW)** — represents OFF, False, or approximately 0 volts
- **1 (HIGH)** — represents ON, True, or approximately 3.3–5 volts

We use two states because electronic switches (transistors) are either fully
ON or fully OFF — making binary the natural language of hardware.

---

### The Three Fundamental Gates

#### 🔵 AND Gate
> "Output is 1 **only when BOTH** inputs are 1"

**Real-world analogy:** Two light switches wired **in series** — the lamp turns
on only when BOTH switches are ON.

**Boolean expression:** `Y = A · B`

| A | B | Y = A AND B |
|:-:|:-:|:-----------:|
| 0 | 0 |      0      |
| 0 | 1 |      0      |
| 1 | 0 |      0      |
| 1 | 1 |  **1**  |

---

#### 🟢 OR Gate
> "Output is 1 when **at least one** input is 1"

**Real-world analogy:** Two light switches wired **in parallel** — the lamp turns
on when EITHER switch is ON.

**Boolean expression:** `Y = A + B`

| A | B | Y = A OR B |
|:-:|:-:|:----------:|
| 0 | 0 |     0      |
| 0 | 1 |   **1**  |
| 1 | 0 |   **1**  |
| 1 | 1 |   **1**  |

---

#### 🟡 XOR Gate (Exclusive OR)
> "Output is 1 when the inputs are **different**"

**Real-world analogy:** A hallway light controlled by two switches — flipping
either switch *toggles* the light; flipping both returns it to its original state.

**Boolean expression:** `Y = A ⊕ B`

| A | B | Y = A XOR B |
|:-:|:-:|:-----------:|
| 0 | 0 |      0      |
| 0 | 1 |   **1**  |
| 1 | 0 |   **1**  |
| 1 | 1 |      0      |

> 💡 **Key difference between OR and XOR:**  
> OR outputs 1 when A=1 **and** B=1.  
> XOR outputs **0** in that case — it only fires when inputs *disagree*.

---

## 🛠️ Task 1.1 — Install & Configure Logisim-Evolution

### What is Logisim-Evolution?

**Logisim-Evolution** is a free, open-source digital logic simulator. It lets you
draw circuit diagrams on screen and immediately simulate them — no physical
components needed. It is used in universities worldwide to teach digital design.

---

### STEP 1 — Download

Go to the official releases page:
```
https://github.com/logisim-evolution/logisim-evolution/releases
```

Download the file matching your operating system:

| OS | File |
|----|------|
| **Windows** | `logisim-evolution-X.X.X-win.exe` |
| **macOS** | `logisim-evolution-X.X.X-mac.dmg` |
| **Linux** | `logisim-evolution-X.X.X-all.jar` |

> ⚠️ **Java Requirement:** Logisim-Evolution needs **Java JDK 11 or later**.  
> Check: open a terminal and run `java -version`  
> Install if missing: https://adoptium.net → choose **Temurin 17 LTS** (free)

---

### STEP 2 — Install

**Windows:**
1. Double-click the `.exe` installer
2. Click **Yes** when prompted by Windows security
3. Follow the wizard: Next → Next → Install → Finish
4. Launch from Start Menu

**macOS:**
1. Open the `.dmg` and drag Logisim-Evolution to **Applications**
2. First launch: System Preferences → Security & Privacy → **"Open Anyway"**

**Linux:**
```bash
sudo apt install default-jdk            # Install Java (Ubuntu/Debian)
java -jar logisim-evolution-X.X.X-all.jar   # Run Logisim
```

---

### STEP 3 — Understand the Interface

```
┌──────────────────────────────────────────────────────────────┐
│  Menu: File | Edit | Project | Simulate | Window | Help     │
├────────────────────────────────────────────────────────────  │
│  [Toolbar: Select ▶ | Poke 👋 | Edit | Wiring tools]        │
├──────────────┬───────────────────────────────────────────── │
│  Component   │                                              │
│  Explorer    │         CANVAS  (Drawing Area)              │
│  (left panel)│     ← Build your circuits here →           │
│              │                                              │
│  • Gates     │                                              │
│  • Wiring    │                                              │
│  • Plexers   │                                              │
│  • Memory    │                                              │
└──────────────┴─────────────────────────────────────────────┘
```

| Area | Purpose |
|------|---------|
| **Component Explorer** (left) | Library: Gates, Wiring, I/O, Plexers… |
| **Canvas** (centre) | Where you draw circuits |
| **Poke Tool** 👋 | Click to toggle input values during simulation |
| **Edit Tool** ▶ | Place and move components |

### STEP 4 — Configure

- `View` → check **Show Grid** ✓
- `Simulate` → check **Auto-Propagate** ✓ *(simulation updates instantly)*
- Zoom: `Ctrl +` / `Ctrl –`

### How to Add Pins & Labels
- Component Explorer → **Wiring** → **Pin**
- Click canvas to place; right-click → Properties
  - **Output? = No** → Input pin (label: `A` or `B`)
  - **Output? = Yes** → Output pin (label: `Y`)
- **Wire:** hover a pin until a green dot appears, then drag to another pin

### How to Use the Poke Tool
- Click the **👋 hand icon** in the toolbar
- Click any input pin on the canvas → toggles 0 ↔ 1
- Wire colours: 🟢 bright green = **1**, 🔵 dark = **0**, 🔴 red = error

---

### ✅ Deliverable 1.1 — Two Screenshots

| Filename | Content |
|----------|---------|
| `screenshots/task1_1_installation.png` | Logisim-Evolution fully open on your screen |
| `screenshots/task1_1_interface_labeled.png` | Same window with arrows labelling: Canvas, Component Explorer, Toolbar, Poke Tool |

---

## ⚙️ Task 1.2 — Build and Simulate the AND Gate

### Steps

1. `Project` → `Add Circuit` → name: **`AND_Gate`**
2. Place **two input pins**: label `A` and `B` (Data Bits = 1, Output? = No)
3. Place one **AND Gate**: Component Explorer → Gates → AND Gate
4. Place **one output pin**: label `Y` (Output? = Yes)
5. Wire:
   ```
   A ──┐
       ├─[AND]─── Y
   B ──┘
   ```
6. Click **Poke Tool 👋**, then test all four combinations:

| Test | A | B | Expected Y |
|:----:|:-:|:-:|:----------:|
| 1 | 0 | 0 | **0** |
| 2 | 0 | 1 | **0** |
| 3 | 1 | 0 | **0** |
| 4 | 1 | 1 | **1** |

7. Take **one screenshot per test** (wire colours must be visible).
8. `File` → `Save As` → `circuits/AND_Gate.circ`

### ✅ Deliverable 1.2

```
circuits/AND_Gate.circ
screenshots/AND_00.png
screenshots/AND_01.png
screenshots/AND_10.png
screenshots/AND_11.png
```

---

## ⚙️ Task 1.3 — Build and Simulate the OR Gate

Repeat Task 1.2 steps using an **OR Gate**. Circuit name: `OR_Gate`.

| Test | A | B | Expected Y |
|:----:|:-:|:-:|:----------:|
| 1 | 0 | 0 | **0** |
| 2 | 0 | 1 | **1** |
| 3 | 1 | 0 | **1** |
| 4 | 1 | 1 | **1** |

### ✅ Deliverable 1.3

```
circuits/OR_Gate.circ
screenshots/OR_00.png
screenshots/OR_01.png
screenshots/OR_10.png
screenshots/OR_11.png
```

---

## ⚙️ Task 1.4 — Build and Simulate the XOR Gate

Repeat using an **XOR Gate**. Circuit name: `XOR_Gate`.

| Test | A | B | Expected Y |
|:----:|:-:|:-:|:----------:|
| 1 | 0 | 0 | **0** |
| 2 | 0 | 1 | **1** |
| 3 | 1 | 0 | **1** |
| 4 | 1 | 1 | **0** |

### 🌟 Bonus (+10 pts) — XOR from Basic Gates Only

Implement XOR using **only AND, OR, NOT** gates (no XOR primitive).

**Boolean expression:** `A ⊕ B = (A · B̄) + (Ā · B)`

```
A ──┬──[NOT]──┐
    │          ├──[AND]──┐
    │    ┌─────┘          │
    │    │                ├──[OR]── Y
    │    └─────┐          │
    │          ├──[AND]──┘
B ──┴──[NOT]──┘
```

Save bonus circuit as: `circuits/XOR_from_basic_gates.circ`

### ✅ Deliverable 1.4

```
circuits/XOR_Gate.circ
screenshots/XOR_00.png
screenshots/XOR_01.png
screenshots/XOR_10.png
screenshots/XOR_11.png
circuits/XOR_from_basic_gates.circ   ← (optional bonus)
```

---

## 📝 Task 1.5 — Lab Report

Edit the file **`report.md`** already in your repository. Fill in every section.

> The template is pre-loaded for you — just complete it!

---

## 📁 Repository File Structure

After completing all tasks, your repository **must** look exactly like this:

```
lab01-[your-username]/
├── README.md                          ← This file (do not delete)
├── report.md                          ← YOUR completed report
├── circuits/
│   ├── AND_Gate.circ                  ← YOUR circuits
│   ├── OR_Gate.circ
│   ├── XOR_Gate.circ
│   └── XOR_from_basic_gates.circ      ← (optional bonus)
└── screenshots/
    ├── task1_1_installation.png
    ├── task1_1_interface_labeled.png
    ├── AND_00.png
    ├── AND_01.png
    ├── AND_10.png
    ├── AND_11.png
    ├── OR_00.png
    ├── OR_01.png
    ├── OR_10.png
    ├── OR_11.png
    ├── XOR_00.png
    ├── XOR_01.png
    ├── XOR_10.png
    └── XOR_11.png
```

---

## 📊 Grading Rubric

| Item | Points |
|------|:------:|
| Task 1.1 — Installation screenshots present & non-empty | 10 |
| Task 1.2 — AND gate: `.circ` file + 4 screenshots | 25 |
| Task 1.3 — OR gate: `.circ` file + 4 screenshots | 25 |
| Task 1.4 — XOR gate: `.circ` file + 4 screenshots | 25 |
| Task 1.5 — `report.md`: truth tables + Q&A + summary ≥50 words | 15 |
| **Total** | **100** |
| 🌟 Bonus — XOR from basic gates (correct `.circ`) | +10 |

> Grading is **automated** via GitHub Actions. Push your work and check the
> **Actions** tab for your score within ~60 seconds.

---

## 📤 Submission Instructions

### 1 · Accept the Assignment
Click the invitation link your instructor shared → **Accept this assignment**.
GitHub creates your personal repo: `lab01-[your-username]`.

### 2 · Clone Your Repo
```bash
git clone https://github.com/[classroom-org]/lab01-[your-username].git
cd lab01-[your-username]
```

### 3 · Add Your Files
Copy circuits and screenshots into the correct folders.

### 4 · Commit & Push
```bash
git add .
git commit -m "Lab01 complete: AND, OR, XOR gates"
git push origin main
```

### 5 · Check Your Score
Go to your repo on GitHub → **Actions** tab → latest run → look for:
```
SCORE: XX/100
```

You may push multiple times; only the last push before the deadline is graded.

---

## 🆘 Common Problems & Solutions

| Problem | Solution |
|---------|---------|
| Logisim won't open | Install Java 11+: `java -version` in terminal |
| Wires show red/orange | Wire not connected — click and re-attach both ends |
| Output not changing | `Simulate` → enable **Auto-Propagate** |
| Screenshot is too small | Zoom in (`Ctrl +`) before taking the screenshot |
| `.circ` won't save | `File` → `Save` first, then copy the file to `circuits/` |
| GitHub Actions shows ❌ | Read the error, fix the issue, push again |

---

*Good luck! 🚀 Remember — every hardware engineer started exactly where you are now.*

> **Lab 01** | Computer Organization & Digital Design  
> Simulator: Logisim-Evolution (open-source) | Graded via GitHub Actions
