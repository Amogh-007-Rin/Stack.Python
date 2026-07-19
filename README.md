# Stack.Python 🐍

**A 0–100, linear, project-based Python learning sandbox for absolute beginners.**  
101 modules. 11 milestone projects. Zero assumed knowledge. One clear path from zero to deploy.

Stack.Python is a complete, self-contained curriculum that takes a learner with **no programming experience** from writing their first `print()` statement in Module 002 to building a full-stack FastAPI application with SQLAlchemy, Jinja2 templates, and data pipelines in Module 099. Every module assumes only what was taught in the modules before it — no gaps, no leaps, no forward references.

## Table of Contents

- [Who Is This For](#who-is-this-for)
- [What Makes Stack.Python Different](#what-makes-stackpython-different)
- [Learning Path (11 Phases)](#learning-path-11-phases)
- [Milestone Projects](#milestone-projects)
- [Module Format](#module-format)
- [Quickstart](#quickstart)
- [How to Use This Repo](#how-to-use-this-repo)
- [Prerequisites](#prerequisites)
- [Scripts & Tooling](#scripts--tooling)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Who Is This For

- **Complete beginners** — no programming background assumed or required
- **Self-learners** — structured, linear curriculum you can follow on your own
- **Bootcamp students** — supplemental reference to fill in knowledge gaps
- **Instructors** — fork-ready curriculum you can teach from or adapt
- **Career switchers** — learn modern Python with real-world applied projects

## What Makes Stack.Python Different

- **101 strictly linear modules** (000–100). No branching, no "choose your own adventure" confusion.
- **Applied from day one.** Concepts are taught, then immediately used to build something tangible. Milestone projects appear roughly every 10 modules — you never go more than a few lessons without building.
- **Full content, not stubs.** Every module includes a complete lesson, runnable Jupyter notebook, practice exercises, worked solutions, and a quiz — all generated and ready to use.
- **Pedagogically intentional.** Code style conventions (PEP 8, Google-style docstrings, type hints) are introduced progressively. No forward references. Visual diagrams and ASCII art explain structural concepts.
- **Python 3.12+.** Uses modern Python features: f-strings, union typing syntax, match statements (briefly), dataclasses, and more.

## Learning Path (11 Phases)

| Phase | Modules | Topics Covered | Milestone Project |
|---|---|---|---|
| **0. Orientation** | 000–001 | Python history & philosophy, environment setup | — |
| **1. Fundamentals** | 002–010 | Print, variables, types, type conversion, I/O, operators, strings, string formatting, numbers | Calculator CLI |
| **2. Control Flow & Data** | 011–020 | Booleans, conditionals, while/for loops, nested loops, lists, list comprehensions | To-Do List CLI |
| **3. Data Structures** | 021–030 | Tuples, sets, dicts, collections (itertools, zip, enumerate), unpacking, shallow/deep copy | Contact Book |
| **4. Functions** | 031–040 | Function arguments, scope (LEGB), lambdas, recursion, higher-order functions, decorators, generators, iterators | Text Adventure |
| **5. OOP** | 041–050 | Classes, attributes, methods, inheritance, polymorphism, dunder methods, abstract base classes | Library System |
| **6. Advanced OOP & Errors** | 051–060 | Composition, class/static methods, properties, dataclasses, enums, operator overloading, error handling, custom exceptions, file I/O, CSV | Expense Tracker |
| **7. Modules, Stdlib & Testing** | 061–070 | JSON, context managers, modules/packages, venv/pip, stdlib (os, sys, datetime, random), regex, dates/times, logging | Log File Analyzer |
| **8. Data, Web & APIs** | 071–080 | Functional patterns, comprehensions deep dive, type hints (mypy), unittest, pytest & TDD, requests (APIs), BeautifulSoup (scraping), pandas | Weather Dashboard |
| **9. Databases & Web Apps** | 081–090 | matplotlib, SQLite, SQL, SQLAlchemy, Flask, FastAPI, Jinja2, automation (shutil) | Finance DB App + Automation Bot |
| **10. Concurrency & Internals** | 091–098 | Threading, multiprocessing, asyncio, memory management/GC, metaclasses, ML intro (numpy, scikit-learn), packaging, profiling | — |
| **11. Capstone** | 099–100 | Full-stack application (FastAPI + SQLAlchemy + Jinja2), career next steps | Full-Stack App |

## Milestone Projects

| Module | Project | Concepts Applied |
|---|---|---|
| 010 | [Command-Line Calculator](modules/module-010-mini-project-calculator/project/README.md) | Variables, I/O, operators, type conversion, conditionals |
| 020 | [To-Do List CLI](modules/module-020-mini-project-todo-cli/project/README.md) | Lists, loops, functions, menu-driven UI |
| 030 | [Contact Book](modules/module-030-mini-project-contact-book/project/README.md) | Dictionaries, nested data, search/CRUD operations |
| 040 | [Text Adventure Game](modules/module-040-mini-project-text-adventure/project/README.md) | Functions, dict-based world map, game loop, state management |
| 050 | [Library Management System](modules/module-050-mini-project-library-system/project/README.md) | OOP, inheritance, class design, polymorphism |
| 060 | [Expense Tracker](modules/module-060-mini-project-expense-tracker/project/README.md) | CSV persistence, error handling, file I/O, OOP design |
| 070 | [Log File Analyzer](modules/module-070-mini-project-log-analyzer/project/README.md) | Regex, sys.argv, file parsing, summary statistics |
| 080 | [Weather Dashboard](modules/module-080-mini-project-weather-dashboard/project/README.md) | requests (REST API), JSON parsing, API keys |
| 085 | [Finance Database App](modules/module-085-mini-project-finance-database-app/project/README.md) | SQLAlchemy, SQLite, CRUD, data aggregation |
| 090 | [Automation Bot / Mini API](modules/module-090-mini-project-automation-bot/project/README.md) | FastAPI, file automation, scheduling |
| 099 | [Capstone: Full-Stack Application](modules/module-099-capstone-project/project/README.md) | FastAPI, SQLAlchemy, Jinja2, Pydantic, logging, deployment |

Each project includes a `README.md` with numbered requirements and stretch goals, `starter_code.py` with TODO markers, and a complete reference `solution/` implementation.

## Module Format

Every module (000–100) follows a consistent structure:

| File | Purpose |
|---|---|
| `README.md` | Full lesson: prerequisites, learning objectives, concept explanation (with analogies, diagrams, code examples), common pitfalls, hands-on walkthrough, key takeaways, further reading, next module link |
| `notebook.ipynb` | Runnable Jupyter notebook mirroring the lesson — markdown explanations and executable code cells |
| `exercises.md` | 4–6 exercises per module, ordered Warm-up → Core → Challenge → Stretch, with starter signatures and expected output |
| `solutions.md` / `solutions.py` | Clearly labeled worked solutions for all exercises (`.py` for milestone modules) |
| `quiz.md` | 5–8 questions: multiple-choice, "what does this output?", short answer, debugging — answer key under `## Answers` |
| `project/` (milestones only) | Project brief, starter code, and full reference solution |

### Code Style Progression

- Modules 002–030: Basic PEP 8 conventions
- Modules 031+: Google-style docstrings on all functions
- Modules 073+: Type hints on all code (enforced with mypy conventions)

## Quickstart

### Prerequisites

- **Python 3.12+** — [Download](https://www.python.org/downloads/) | [Setup Guide](SETUP.md)
- **Git** — [Download](https://git-scm.com/downloads)
- **VS Code** (recommended) — [Download](https://code.visualstudio.com/)

### One-Line Install

```bash
git clone https://github.com/your-org/Stack.Python.git && cd Stack.Python && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt
```

### Step by Step

```bash
# 1. Clone the repository
git clone https://github.com/your-org/Stack.Python.git
cd Stack.Python

# 2. Create and activate a virtual environment
# macOS/Linux:
python3.12 -m venv venv
source venv/bin/activate

# Windows (Command Prompt):
python -m venv venv
venv\Scripts\activate

# Windows (PowerShell):
python -m venv venv
.\venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4. Start learning!
open modules/module-000-introduction-to-python/README.md
```

### Verify Installation

```bash
python -c "import jupyter, pytest, requests, pandas; print('All dependencies installed!')"
```

## How to Use This Repo

### For Learners

1. **Go in order.** Each module assumes all prior knowledge. Skipping ahead will leave you lost.
2. **Read the lesson first.** Start with `README.md` — it contains the full explanation.
3. **Run the notebook.** Open `notebook.ipynb` and execute every cell. Experiment by changing values.
4. **Do the exercises.** Open `exercises.md` and attempt every problem **before** looking at solutions.
5. **Check your work.** Compare with `solutions.md` (or `solutions.py` for milestone modules).
6. **Take the quiz.** `quiz.md` reinforces key concepts. Cover the answer key at the bottom.
7. **Build the projects.** For milestone modules, the `project/` folder contains a real-world build.
8. **Track your progress.** Run `python scripts/check_progress.py --completed 0 1 2 ...` to see your completion status.

### For Instructors

- Fork the repository and adapt any module to your teaching style.
- Use modules as-is for a semester-long course (roughly 1 module per day).
- Assign milestone projects as midterms or final projects.
- Run `python scripts/run_all_notebooks.py` to verify all notebooks execute correctly.

### Tips

- **Code along.** Typing the examples yourself (rather than copy-pasting) builds muscle memory.
- **Break things.** Modify code examples to see what happens. Errors are learning opportunities.
- **Use the quizzes.** Each quiz is designed to reveal gaps in understanding — don't skip them.
- **Compare solutions.** Your solution doesn't need to match exactly, but understand why approaches differ.
- **Revisit modules.** If you're stuck on a later concept, the problem is often in a prerequisite module.

## Scripts & Tooling

| Script | Purpose |
|---|---|
| `scripts/new_module.py` | Scaffold a new module folder from the standard template |
| `scripts/check_progress.py` | CLI progress tracker — shows completed/total modules by phase |
| `scripts/run_all_notebooks.py` | Dev utility — executes all notebooks via papermill |

```bash
# Create a new module scaffold
python scripts/new_module.py --number 42 --title "My Module" --phase "My Phase"

# Check progress (mark modules 0, 1, 2, 3 as complete)
python scripts/check_progress.py --completed 0 1 2 3

# Run all notebooks (CI use-case)
python scripts/run_all_notebooks.py

# Run notebooks in parallel
python scripts/run_all_notebooks.py --parallel

# Run a range
python scripts/run_all_notebooks.py --start 0 --end 10
```

### CI/CD

This repository includes GitHub Actions workflows:

- **notebook-check.yml** — Executes all notebooks headlessly via papermill on every push/PR
- **link-check.yml** — Validates all internal markdown links resolve correctly

## Project Structure

```
Stack.Python/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CURRICULUM.md           # Full linked table of contents (all 101 modules)
├── SETUP.md                # Environment setup guide (Windows/macOS/Linux)
├── requirements.txt        # 17 base dependencies
├── pyproject.toml          # Black, ruff, mypy configuration
├── .gitignore
├── .github/workflows/
│   ├── notebook-check.yml
│   └── link-check.yml
├── scripts/
│   ├── new_module.py
│   ├── check_progress.py
│   └── run_all_notebooks.py
├── assets/diagrams/
└── modules/
    ├── module-000-introduction-to-python/
    ├── module-001-setting-up-your-environment/
    ├── ...
    └── module-100-where-to-go-next/
```

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.

Quick summary:
- **Issues:** Report bugs, content errors, or suggestions via GitHub Issues
- **PRs:** Fork, create a feature branch, make changes, run quality checks (`black . && ruff check .`), submit a PR
- **Content:** All code must be valid Python 3.12+, follow PEP 8, use Google-style docstrings (modules 031+), and include type hints (modules 073+)
- **No forward references:** Never introduce a concept in module N that won't be taught until module N+X

## License

MIT — see [LICENSE](LICENSE). Free to use, modify, and distribute for teaching, learning, or commercial purposes.
