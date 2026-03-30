# 🎓 Instructor Notes — Lab 01

> This file is for **instructors only**. Remove or move it before distributing
> the template to students via GitHub Classroom.

---

## Deploying This Template

### Step 1 — Create the GitHub Classroom Assignment

1. Go to https://classroom.github.com and sign in with your org account
2. Click **"New Assignment"** → **"Individual Assignment"**
3. Title: `Lab 01 – Logic Gates`
4. Repository prefix: `lab01-`
5. **Visibility:** Private (recommended for student repos)
6. **Template repository:** select this repo
7. Enable **"Add a supported editor"** → optional
8. Enable **"Enable feedback pull requests"** → recommended
9. Set deadline
10. Click **"Create Assignment"** → copy the invitation link for students

### Step 2 — Share the Link

Distribute the invitation link via your LMS (Moodle, Blackboard, Canvas, etc.).
Each student clicks once; GitHub Classroom automatically forks this template
into a private repo named `lab01-[github-username]`.

### Step 3 — Autograding is Ready

The `.github/workflows/autograding_lab01.yml` workflow runs automatically
on every `git push` to `main`. Students see ✅ / ❌ on their commits.

---

## Grading Workflow Breakdown

| Stage | Script | What it checks | Max pts |
|-------|--------|----------------|:-------:|
| Check 1 | `check_files.py` | All .circ files present & non-empty; 12+ screenshots present | 30 |
| Check 2 | `check_circ_xml.py` | Each .circ contains the correct gate type, pins, and wiring | 45 |
| Check 3 | `check_report.py` | Name/ID filled; truth tables; Q1–Q3 answered; ≥50-word summary | 15 |
| **Remaining 10 pts** | Manual | Screenshot visual inspection (optional spot-check) | 10 |

### Collecting Grades from All 350 Repos

Install dependencies:
```bash
pip install PyGithub requests
```

Set your token:
```bash
export GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxx
```

Run the collector:
```bash
python3 .grading/collect_grades.py \
  --org  your-classroom-org-name \
  --assignment lab01 \
  --output lab01_grades.csv
```

Output: `lab01_grades.csv` with columns:
`username, repo_url, total_score, file_score, xml_score, report_score, last_push`

---

## Adjusting the Rubric

All point values are defined as Python constants at the top of each grading script:

| Script | Constant | Default |
|--------|----------|---------|
| `check_files.py` | `POINTS["circuits"]` | 10 per file |
| `check_files.py` | `POINTS["screenshots"]` | 1.5 per file |
| `check_circ_xml.py` | `max_pts` per circuit | 15 |
| `check_report.py` | `MAX_SCORE` | 15 |

Edit `.grading/*.py` in the **template repo** before the assignment opens.
Changes apply to all future student repos automatically.

---

## Common Student Issues

| Issue | Advice |
|-------|--------|
| Java not installed | Direct to https://adoptium.net — Temurin 17 LTS |
| .circ file missing from push | Student forgot `git add circuits/` |
| Screenshots too small / dark | Ask student to zoom in Logisim before screenshotting |
| report.md still has placeholder text | Autograder detects placeholder patterns and deducts |
| Autograder shows red ❌ | Student can push again after fixing; last push is graded |

---

## MOSS Plagiarism Check (optional)

```bash
# 1. Clone all repos
for u in $(cat roster.txt); do
  git clone https://github.com/YOUR_ORG/lab01-${u}.git repos/lab01-${u}
done

# 2. Run MOSS on .circ files
perl mossnet -l cc repos/lab01-*/circuits/*.circ

# 3. Run MOSS on report.md files
perl mossnet -l cc repos/lab01-*/report.md
```
MOSS user ID registration: email `moss@moss.stanford.edu`

---

*Lab 01 — Instructor Notes | Computer Organization & Digital Design*
