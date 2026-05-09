# 🐍 Python Learning Journey — DevOps Path 2026

> **Goal:** Become a DevOps / LLMOps Engineer by April 2027
> **Started:** April 2026 · **Current:** Day 20 of 660 · **Phase:** 0.5 — Practical Python

---

## 📍 Where I Am Right Now

| | |
|---|---|
| **Phase** | 0.5 — Practical Python |
| **Day** | 20 of 660 |
| **Current topic** | List comprehensions · map · filter · lambda |
| **Next** | OOP — Classes and objects |
| **Target** | First DevOps job — April 2027 |

---

## 🗺️ Full Roadmap

```
Phase 0.5  →  Python Foundations         (Days 1–75)      ← YOU ARE HERE
Phase 1    →  Linux & Bash               (Days 76–145)
Phase 2    →  Docker & Observability     (Days 146–215)
Phase 3    →  Programming Deep Dive      (Days 216–345)
Phase 4    →  IaC · CI/CD · GitOps       (Days 346–415)
Phase 5    →  Cloud + FinOps             (Days 416–480)
Phase 6    →  Kubernetes & Security      (Days 481–555)
Phase 7    →  LLMOps & AI Infrastructure (Days 556–640)
Phase 8    →  Job Hunt                   (Days 641–660)
```

---

## ✅ Topics Completed

### Week 1–2 — Python Basics
- [x] Variables, data types — strings, integers, floats, booleans
- [x] Lists, tuples, dictionaries, sets
- [x] Control flow — if/elif/else, for loops, while loops
- [x] Functions — defining, calling, arguments, return values

### Week 3 — JSON & APIs
- [x] `json.loads()` and `json.dumps()`
- [x] Reading and writing JSON files
- [x] Fetching real API data with `requests`
- [x] Saving API responses as JSON

### Week 4 — Modules & Imports (Day 18–19)
- [x] File I/O — `open()` with r, w, a modes · `read()` · `readlines()`
- [x] Error handling — `try` / `except` / `finally` · custom exceptions
- [x] `os` — `getcwd()`, `listdir()`, `makedirs()`, `path.exists()`
- [x] `sys` — `argv`, `exit()`
- [x] `pathlib` — `Path()`, `.exists()`, `.glob()`, `.read_text()`, `.write_text()`
- [x] `datetime` — `now()`, `strftime()`, `timedelta`, date math
- [x] `csv` — `DictWriter`, `DictReader`, reading and writing structured data

### Week 5 — Comprehensions & Functional Tools (Day 20) ← IN PROGRESS
- [ ] List comprehensions — `[x for x in list if condition]`
- [ ] Dict and set comprehensions
- [ ] `map()` — transform every item in a list
- [ ] `filter()` — keep only matching items
- [ ] `lambda` — small anonymous functions

---

## 📦 Projects Built

| # | Project | Topics Used | Status |
|---|---------|------------|--------|
| 1 | JSON File Parser | json, file I/O | ✅ Done |
| 2 | Weather API Fetcher | requests, json, datetime | ✅ Done |
| 3 | Log File Analyzer | file I/O, error handling | ✅ Done |
| 4 | DevOps Study Tracker CLI | csv, datetime, pathlib, os, sys | 🔨 Building |

---

## 🔨 Current Project — DevOps Study Tracker CLI

A command-line tool to track daily study sessions, built using everything learned so far.

### Usage

```bash
# Log a study session
python tracker.py log "List comprehensions" 2

# View all sessions and total hours
python tracker.py report

# Check days until April 2027 job goal
python tracker.py goal
```

### Example Output

```
$ python tracker.py report
📊 Study Report
────────────────────────────────
2026-05-09 | List comprehensions | 2h
2026-05-08 | Modules and imports | 3h
2026-05-07 | JSON and APIs       | 2h
────────────────────────────────
Total: 7 hours studied

$ python tracker.py goal
🎯 328 days until your DevOps job goal — April 2027!
```

### Tech Stack
- `sys` — CLI argument handling
- `csv` — reading and writing study log
- `datetime` — timestamps and goal countdown
- `pathlib` — safe file path handling
- `os` — checking file/folder existence
- `json` — saving summary stats
- List comprehensions — filtering and totalling sessions
- `map()` / `filter()` — formatting and filtering output

---

## 📚 What's Coming Next

| Topic | When | Why It Matters |
|---|---|---|
| OOP — Classes and objects | Day 21 | Every Python tool is built with classes |
| pytest — writing tests | Day 22 | Top 1% engineers test their code |
| Linux basics | Day 26+ | Foundation of all DevOps |
| Docker | Day 46+ | Run anything, anywhere |
| Kubernetes | Day 76+ | Production container orchestration |
| Terraform | Day 100+ | Infrastructure as code |
| AWS / Azure | Day 110+ | Cloud is where everything runs |

---

## 🧠 Key Things I Have Learned

**Comprehensions beat for loops when building lists**
```python
# Old way
names = []
for server in servers:
    if server['status'] == 'online':
        names.append(server['name'])

# Better way
names = [s['name'] for s in servers if s['status'] == 'online']
```

**pathlib beats os.path for file handling**
```python
# Old way
import os
path = os.path.join('data', 'log.csv')
if os.path.exists(path):
    with open(path) as f: ...

# Better way
from pathlib import Path
path = Path('data') / 'log.csv'
if path.exists():
    content = path.read_text()
```

**Always handle errors — never let scripts crash silently**
```python
try:
    data = json.loads(response.text)
except json.JSONDecodeError as e:
    print(f"❌ Invalid JSON: {e}")
    sys.exit(1)
```

---

## 📈 Progress Stats

```
Days completed : 20 / 660
Hours studied  : ~80 hours
Projects built : 3 complete + 1 in progress
Blog posts     : 0  ← start writing!
GitHub commits : building streak...
Days to goal   : ~328 days
```

---

## 🎯 Daily Habit

- **Weekdays:** 3–4 hours minimum
- **Weekends:** 5–7 hours
- **Rule:** Never zero. Worst day = minimum 1 hour.
- **Every project goes on GitHub** — no exceptions
- **Weekly review:** every Sunday — what did I build, what do I know now

---

## 🔗 Links

- 📁 [GitHub Profile](https://github.com/) — all projects here
- 💼 [LinkedIn](https://linkedin.com/) — weekly learning posts
- 📝 Blog — coming soon

---

*Day 20 of 660 · Started April 2026 · Target April 2027 · DevOps + LLMOps + FinOps Engineer*
