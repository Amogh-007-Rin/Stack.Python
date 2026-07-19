# Project Specification: Stack.Python

**A 0–100, linear, project-based Python learning sandbox for absolute beginners.**

This document is a complete build specification. A coding agent reading this file should be able to generate the entire repository — folder structure, all 101 modules with full lesson content, notebooks, exercises, solutions, quizzes, and milestone mini-projects — in a single pass, with no additional clarification needed.

---

## 1. Project Overview

**Repository name:** `Stack.Python`

**Goal:** Take a learner with zero programming experience from Module 0 to Module 100, ending with them capable of building real, deployable Python applications (CLI tools, APIs, data pipelines, automation scripts) and understanding how Python works under the hood.

**Format:** Strictly linear. Module `N` assumes everything taught in modules `0` through `N-1` and nothing more. No forward references to unlearned concepts.

**Pedagogical style:** Applied-first. Every phase of the curriculum weaves in small, hands-on mini-projects rather than saving all application until the end — concepts are taught, then immediately used to build something tangible.

**Target audience:** Complete beginners (no assumed programming background), self-learners, bootcamp supplement users, and instructors who want a ready-made curriculum they can teach from or fork.

**License:** MIT (see §9).

---

## 2. Content Generation Scope (Agent Instructions)

The agent must generate **full content for all 101 modules (module-000 through module-100)** in this initial pass — not stubs, not placeholders. Every module must be complete and usable on its own the moment the repo is generated. Use the Full Curriculum Table in §6 as the authoritative source of truth for what each module covers — do not invent, skip, reorder, or merge topics.

Each module must include, at minimum:
1. A full lesson (`README.md`)
2. A runnable Jupyter notebook (`notebook.ipynb`)
3. Practice exercises (`exercises.md`)
4. Worked solutions (`solutions.py` or `solutions.md`)
5. A short quiz (`quiz.md`)

Modules flagged **"Milestone Project"** in §6 additionally require a `project/` subfolder with a larger applied build.

---

## 3. Repository Structure

```
Stack.Python/
├── README.md                          # Landing page, learning path map, how to use this repo
├── LICENSE
├── CONTRIBUTING.md
├── CURRICULUM.md                      # Full linked table of contents (all 101 modules)
├── SETUP.md                           # Environment setup guide (all OSes)
├── requirements.txt                   # Base dependencies (jupyter, pytest, etc.)
├── pyproject.toml                     # Project metadata, tool config (black, ruff, mypy)
├── .gitignore
├── .github/
│   └── workflows/
│       ├── notebook-check.yml         # Executes all notebooks headlessly, fails on error
│       └── link-check.yml             # Validates internal markdown links
├── scripts/
│   ├── new_module.py                  # Scaffolds a new module folder from the template
│   ├── check_progress.py              # CLI: prints learner's completion checklist
│   └── run_all_notebooks.py           # Dev utility: executes every notebook via papermill
├── assets/
│   └── diagrams/                      # Shared images/diagrams referenced by modules
└── modules/
    ├── module-000-introduction-to-python/
    │   ├── README.md
    │   ├── notebook.ipynb
    │   ├── exercises.md
    │   ├── solutions.md
    │   └── quiz.md
    ├── module-001-setting-up-your-environment/
    │   └── ...
    ├── ...
    ├── module-010-mini-project-calculator/
    │   ├── README.md
    │   ├── notebook.ipynb
    │   ├── exercises.md
    │   ├── solutions.py
    │   ├── quiz.md
    │   └── project/
    │       ├── README.md              # Project brief, requirements, stretch goals
    │       ├── starter_code.py
    │       └── solution/
    │           └── calculator.py
    ├── ...
    └── module-100-where-to-go-next/
        ├── README.md
        └── quiz.md
```

### Naming convention
- Folder: `module-XXX-kebab-case-title` where `XXX` is **zero-padded to 3 digits** (`000`–`100`) so directory listings sort correctly.
- Every module folder name must exactly match the "Folder Slug" column in §6.
- File names inside a module folder are always identical across modules (`README.md`, `notebook.ipynb`, `exercises.md`, etc.) — never renamed per-topic.

---

## 4. Per-Module Content Template

Every module's `README.md` must follow this exact section structure:

```markdown
# Module XXX: <Title>

> **Phase:** <Phase name>  |  **Estimated time:** <X hours>  |  **Milestone Project:** Yes/No

## Prerequisites
- Links to the specific prior modules whose concepts are required.

## Learning Objectives
By the end of this module, you will be able to:
- 3–6 concrete, testable objectives (action verbs: "write", "explain", "debug", "build").

## Why This Matters
- 2–4 sentences connecting the topic to real-world use — what you can build once you know this.

## Concept Explanation
- Plain-language explanation, building from analogy where useful.
- At least one diagram description or ASCII diagram for structural/flow topics (loops, OOP, memory model, etc.).
- Multiple small, runnable code examples with output shown.

## Common Pitfalls
- 3–5 mistakes beginners make with this topic, and how to spot/fix them.

## Hands-On Walkthrough
- A step-by-step guided example, building a small piece of working code live in the lesson (separate from the bigger exercises/project).

## Key Takeaways
- Bullet summary (5–8 bullets).

## Further Reading
- 2–4 links to official Python docs / PEPs relevant to the topic (no invented links).

## Next Module
- One-line teaser + link to the next module.
```

### `notebook.ipynb` requirements
- Mirrors the "Concept Explanation" and "Hands-On Walkthrough" sections as **runnable** cells (markdown cells for explanation, code cells for examples).
- Every code cell must execute top-to-bottom with no errors on a clean kernel.
- No hidden dependency on files outside the module folder unless explicitly provided in that folder.

### `exercises.md` requirements
- 4–6 exercises per module, ordered by increasing difficulty: **Warm-up → Core → Challenge → Stretch**.
- Each exercise states its goal, any starter code/signature, and expected input/output examples.
- No solutions in this file.

### `solutions.py` / `solutions.md` requirements
- One clearly labeled solution per exercise, matching exercise numbering.
- Solutions must run and produce the stated expected output.
- Include a one-line comment explaining *why* the approach was chosen where non-obvious.

### `quiz.md` requirements
- 5–8 questions: mix of multiple-choice, "what does this code output?", and short-answer/debugging questions.
- Answer key at the bottom under a `## Answers` header (so it's easy to visually hide/collapse in a rendered viewer).

### Milestone `project/` requirements (only for flagged modules)
- `README.md`: project brief, functional requirements (numbered), constraints, and 2–3 stretch goals for advanced learners.
- `starter_code.py`: skeleton with function/class signatures and `# TODO` markers, no implementation.
- `solution/`: a complete, working reference implementation.
- Project scope must only use concepts introduced up through that module — no forward-borrowing.

---

## 5. Curriculum Design Principles

- **101 modules total** (`000`–`100`), fully linear, no branching paths.
- **9 phases**, each ending in a milestone mini-project that consolidates the phase.
- Applied mini-projects are **woven throughout**, not backloaded — see the milestone modules spaced roughly every 10 modules.
- Standard library and applied-domain topics (web, data, automation, ML) are introduced progressively from the mid-curriculum onward, always framed as "here's a real thing you can now build," never as an abstract survey.
- Code style taught and enforced throughout: PEP 8, type hints introduced at Module 073 and used in all subsequent modules' examples, docstrings (Google style) used from Module 031 onward.
- Python version target: **Python 3.12+**. `SETUP.md` must cover Windows, macOS, and Linux installation plus `venv` creation.

---

## 6. Full Curriculum Table (Authoritative — 101 Modules)

| # | Folder Slug | Title | Phase | Milestone Project |
|---|---|---|---|---|
| 000 | module-000-introduction-to-python | Introduction to Python: History, Philosophy & Applications | 0. Orientation | No |
| 001 | module-001-setting-up-your-environment | Setting Up Your Dev Environment (Python, VS Code, Terminal) | 0. Orientation | No |
| 002 | module-002-your-first-python-program | Your First Python Program | 1. Fundamentals | No |
| 003 | module-003-variables-and-data-types | Variables and Data Types | 1. Fundamentals | No |
| 004 | module-004-type-conversion-and-casting | Type Conversion and Casting | 1. Fundamentals | No |
| 005 | module-005-basic-input-and-output | Basic Input and Output | 1. Fundamentals | No |
| 006 | module-006-operators | Operators (Arithmetic, Comparison, Logical, Assignment) | 1. Fundamentals | No |
| 007 | module-007-strings-deep-dive | Strings Deep Dive (Indexing, Slicing, Methods) | 1. Fundamentals | No |
| 008 | module-008-string-formatting | String Formatting (f-strings, format, %) | 1. Fundamentals | No |
| 009 | module-009-numbers-deep-dive | Numbers Deep Dive (Precision, the `math` module) | 1. Fundamentals | No |
| 010 | module-010-mini-project-calculator | Milestone Project: Command-Line Calculator | 1. Fundamentals | **Yes** |
| 011 | module-011-booleans-and-truthiness | Booleans and Truthiness | 2. Control Flow & Data | No |
| 012 | module-012-conditional-statements | Conditional Statements (if / elif / else) | 2. Control Flow & Data | No |
| 013 | module-013-comparison-chaining-and-logic | Comparison Chaining & Logical Operators Deep Dive | 2. Control Flow & Data | No |
| 014 | module-014-while-loops | Loops: `while` | 2. Control Flow & Data | No |
| 015 | module-015-for-loops | Loops: `for` | 2. Control Flow & Data | No |
| 016 | module-016-loop-control | Loop Control (`break`, `continue`, loop `else`) | 2. Control Flow & Data | No |
| 017 | module-017-nested-loops-and-patterns | Nested Loops and Pattern Printing | 2. Control Flow & Data | No |
| 018 | module-018-lists-basics | Lists: Basics | 2. Control Flow & Data | No |
| 019 | module-019-lists-methods-and-comprehensions | Lists: Methods & Comprehensions | 2. Control Flow & Data | No |
| 020 | module-020-mini-project-todo-cli | Milestone Project: To-Do List CLI App | 2. Control Flow & Data | **Yes** |
| 021 | module-021-tuples | Tuples | 3. Data Structures | No |
| 022 | module-022-sets | Sets | 3. Data Structures | No |
| 023 | module-023-dictionaries-basics | Dictionaries: Basics | 3. Data Structures | No |
| 024 | module-024-dictionaries-advanced | Dictionaries: Advanced (Nesting, Methods, Comprehensions) | 3. Data Structures | No |
| 025 | module-025-mutability-vs-immutability | Mutability vs Immutability | 3. Data Structures | No |
| 026 | module-026-working-with-collections | Working with Collections (`itertools`, `zip`, `enumerate`) | 3. Data Structures | No |
| 027 | module-027-unpacking-and-multiple-assignment | Unpacking and Multiple Assignment | 3. Data Structures | No |
| 028 | module-028-copying-objects | Copying Objects (Shallow vs Deep Copy) | 3. Data Structures | No |
| 029 | module-029-choosing-the-right-data-structure | Choosing the Right Data Structure | 3. Data Structures | No |
| 030 | module-030-mini-project-contact-book | Milestone Project: Contact Book Application | 3. Data Structures | **Yes** |
| 031 | module-031-functions-basics | Functions: Basics (`def`, `return`, Parameters) | 4. Functions | No |
| 032 | module-032-function-arguments | Function Arguments (Default, Keyword, `*args`, `**kwargs`) | 4. Functions | No |
| 033 | module-033-scope-and-namespaces | Scope and Namespaces (the LEGB Rule) | 4. Functions | No |
| 034 | module-034-lambda-functions | Lambda Functions | 4. Functions | No |
| 035 | module-035-recursion | Recursion | 4. Functions | No |
| 036 | module-036-higher-order-functions | Higher-Order Functions (`map`, `filter`, `reduce`) | 4. Functions | No |
| 037 | module-037-decorators-basics | Decorators: Basics | 4. Functions | No |
| 038 | module-038-generators-and-yield | Generators and `yield` | 4. Functions | No |
| 039 | module-039-iterators-and-the-iterator-protocol | Iterators and the Iterator Protocol | 4. Functions | No |
| 040 | module-040-mini-project-text-adventure | Milestone Project: Text-Based Adventure Game Engine | 4. Functions | **Yes** |
| 041 | module-041-introduction-to-oop | Introduction to OOP: Classes and Objects | 5. OOP | No |
| 042 | module-042-attributes-and-methods | Attributes and Methods | 5. OOP | No |
| 043 | module-043-constructors-and-self | Constructors (`__init__`) and `self` | 5. OOP | No |
| 044 | module-044-class-vs-instance-variables | Class Variables vs Instance Variables | 5. OOP | No |
| 045 | module-045-encapsulation | Encapsulation | 5. OOP | No |
| 046 | module-046-inheritance | Inheritance | 5. OOP | No |
| 047 | module-047-polymorphism | Polymorphism | 5. OOP | No |
| 048 | module-048-dunder-methods | Dunder/Magic Methods (`__str__`, `__repr__`, `__eq__`) | 5. OOP | No |
| 049 | module-049-abstract-base-classes | Abstract Base Classes and Interfaces | 5. OOP | No |
| 050 | module-050-mini-project-library-system | Milestone Project: Library/Inventory Management System | 5. OOP | **Yes** |
| 051 | module-051-composition-vs-inheritance | Composition vs Inheritance | 6. Advanced OOP & Errors | No |
| 052 | module-052-classmethods-staticmethods-properties | Class Methods, Static Methods, Properties | 6. Advanced OOP & Errors | No |
| 053 | module-053-dataclasses | Dataclasses | 6. Advanced OOP & Errors | No |
| 054 | module-054-enums | Enums | 6. Advanced OOP & Errors | No |
| 055 | module-055-operator-overloading | Operator Overloading | 6. Advanced OOP & Errors | No |
| 056 | module-056-error-handling | Error Handling: `try` / `except` / `finally` | 6. Advanced OOP & Errors | No |
| 057 | module-057-custom-exceptions | Custom Exceptions | 6. Advanced OOP & Errors | No |
| 058 | module-058-reading-and-writing-text-files | Working with Files: Reading & Writing Text Files | 6. Advanced OOP & Errors | No |
| 059 | module-059-working-with-csv-files | Working with Files: CSV | 6. Advanced OOP & Errors | No |
| 060 | module-060-mini-project-expense-tracker | Milestone Project: Personal Expense Tracker (CSV-backed) | 6. Advanced OOP & Errors | **Yes** |
| 061 | module-061-working-with-json | Working with JSON | 7. Modules, Stdlib & Testing | No |
| 062 | module-062-context-managers | Context Managers and the `with` Statement | 7. Modules, Stdlib & Testing | No |
| 063 | module-063-modules-and-imports | Modules and Imports | 7. Modules, Stdlib & Testing | No |
| 064 | module-064-packages-and-init | Packages and `__init__.py` | 7. Modules, Stdlib & Testing | No |
| 065 | module-065-virtual-environments-and-pip | Virtual Environments and `pip` | 7. Modules, Stdlib & Testing | No |
| 066 | module-066-standard-library-tour | The Python Standard Library Tour (`os`, `sys`, `datetime`, `random`) | 7. Modules, Stdlib & Testing | No |
| 067 | module-067-regular-expressions | Regular Expressions | 7. Modules, Stdlib & Testing | No |
| 068 | module-068-working-with-dates-and-times | Working with Dates and Times | 7. Modules, Stdlib & Testing | No |
| 069 | module-069-logging | Logging | 7. Modules, Stdlib & Testing | No |
| 070 | module-070-mini-project-log-analyzer | Milestone Project: Log File Analyzer | 7. Modules, Stdlib & Testing | **Yes** |
| 071 | module-071-functional-programming-patterns | Functional Programming Patterns in Python | 8. Data, Web & APIs | No |
| 072 | module-072-comprehensions-deep-dive | Comprehensions Deep Dive (List/Dict/Set/Generator) | 8. Data, Web & APIs | No |
| 073 | module-073-type-hints-and-static-typing | Type Hints and Static Typing (`mypy`) | 8. Data, Web & APIs | No |
| 074 | module-074-testing-basics-unittest | Testing Basics: `unittest` | 8. Data, Web & APIs | No |
| 075 | module-075-testing-with-pytest-and-tdd | Testing with `pytest` and Test-Driven Development | 8. Data, Web & APIs | No |
| 076 | module-076-working-with-apis-requests | Working with APIs: the `requests` Library | 8. Data, Web & APIs | No |
| 077 | module-077-web-scraping-basics | Web Scraping Basics: `BeautifulSoup` | 8. Data, Web & APIs | No |
| 078 | module-078-introduction-to-pandas | Introduction to Data with `pandas` | 8. Data, Web & APIs | No |
| 079 | module-079-data-cleaning-and-analysis | Data Cleaning & Analysis with `pandas` | 8. Data, Web & APIs | No |
| 080 | module-080-mini-project-weather-dashboard | Milestone Project: Weather Dashboard CLI (Public API) | 8. Data, Web & APIs | **Yes** |
| 081 | module-081-data-visualization-matplotlib | Data Visualization with `matplotlib` | 9. Databases & Web Apps | No |
| 082 | module-082-databases-sqlite | Working with Databases: SQLite (`sqlite3`) | 9. Databases & Web Apps | No |
| 083 | module-083-introduction-to-sql-from-python | Introduction to SQL from Python | 9. Databases & Web Apps | No |
| 084 | module-084-orms-sqlalchemy | ORMs: Introduction to SQLAlchemy | 9. Databases & Web Apps | No |
| 085 | module-085-mini-project-finance-database-app | Milestone Project: Personal Finance Database App | 9. Databases & Web Apps | **Yes** |
| 086 | module-086-flask-basics | Introduction to Web Development: Flask Basics | 9. Databases & Web Apps | No |
| 087 | module-087-building-rest-apis-fastapi | Building REST APIs with FastAPI | 9. Databases & Web Apps | No |
| 088 | module-088-templating-with-jinja2 | Templating and Simple Web Frontends (Jinja2) | 9. Databases & Web Apps | No |
| 089 | module-089-automation-and-scripting | Automation & Scripting (`shutil`, Scheduling, File Automation) | 9. Databases & Web Apps | No |
| 090 | module-090-mini-project-automation-bot | Milestone Project: Personal Automation Bot / Mini API | 9. Databases & Web Apps | **Yes** |
| 091 | module-091-concurrency-threading | Concurrency: Threading | 10. Concurrency & Internals | No |
| 092 | module-092-concurrency-multiprocessing | Concurrency: Multiprocessing | 10. Concurrency & Internals | No |
| 093 | module-093-asynchronous-python-asyncio | Asynchronous Python: `asyncio` | 10. Concurrency & Internals | No |
| 094 | module-094-memory-management-and-gc | Memory Management & Garbage Collection in CPython | 10. Concurrency & Internals | No |
| 095 | module-095-advanced-decorators-and-metaprogramming | Advanced Decorators & Metaprogramming | 10. Concurrency & Internals | No |
| 096 | module-096-intro-to-machine-learning | Introduction to Machine Learning with Python (`numpy`, `scikit-learn`) | 10. Concurrency & Internals | No |
| 097 | module-097-packaging-and-distribution | Packaging and Distributing Python Projects (PyPI) | 10. Concurrency & Internals | No |
| 098 | module-098-performance-optimization-and-profiling | Performance Optimization & Profiling | 10. Concurrency & Internals | No |
| 099 | module-099-capstone-project | Capstone Project: Full-Stack Application (FastAPI + DB + Data Pipeline) | 11. Capstone | **Yes** |
| 100 | module-100-where-to-go-next | Where to Go Next: Specializations, OSS, Continuing Education | 11. Capstone | No |

---

## 7. Root-Level Documents

### `README.md` (repo landing page) must include:
- Project tagline and one-paragraph description.
- A visual/table "Learning Path Map" grouping modules by phase (mirrors §6 but condensed).
- Quickstart: clone → create venv → `pip install -r requirements.txt` → open `modules/module-000.../README.md`.
- How to use the repo (linear order, do the exercises before checking solutions, use `scripts/check_progress.py`).
- Contribution note pointing to `CONTRIBUTING.md`.

### `CURRICULUM.md`
- The full table from §6, each Folder Slug rendered as a relative markdown link to that module's `README.md`.

### `SETUP.md`
- Python 3.12+ install instructions for Windows/macOS/Linux.
- `venv` creation and activation per-OS.
- `pip install -r requirements.txt`.
- How to launch Jupyter (`jupyter notebook` / VS Code notebook support).
- Recommended VS Code extensions (Python, Jupyter, Pylance).

### `CONTRIBUTING.md`
- How to propose fixes/additions using `scripts/new_module.py` as a scaffold generator.
- Style rules: PEP 8, docstrings, must include tests/quiz updates if content changes.

### `requirements.txt` (base, expand per later modules as needed)
```
jupyter
notebook
pytest
mypy
black
ruff
requests
beautifulsoup4
pandas
matplotlib
sqlalchemy
flask
fastapi
uvicorn
```

### `pyproject.toml`
- Configure `black`, `ruff`, and `mypy` with sane beginner-friendly defaults (line length 88, Python target 3.12).

---

## 8. CI / Quality Gates

- `.github/workflows/notebook-check.yml`: on every push/PR, execute all `notebook.ipynb` files headlessly (e.g., via `nbconvert --execute` or `papermill`) and fail the build on any cell error.
- `.github/workflows/link-check.yml`: validate that all internal relative links between modules resolve (no broken "Next Module" links).
- Every module's code examples and solutions must be valid, runnable Python 3.12 with no syntax errors — this is a hard acceptance criterion, not a nice-to-have.

---

## 9. License & Governance

- `LICENSE`: MIT License, copyright holder = repository owner.
- Repository is intended to be forkable and freely reusable for teaching.

---

## 10. Acceptance Checklist (for the coding agent to self-verify before finishing)

- [ ] All 101 module folders exist, named exactly per §6's Folder Slug column, zero-padded 3-digit numbers.
- [ ] Every module has all 5 required files (`README.md`, `notebook.ipynb`, `exercises.md`, solutions file, `quiz.md`).
- [ ] Every milestone module (10 total, per §6) additionally has a complete `project/` folder with brief, starter code, and solution.
- [ ] No module references a concept not yet introduced by an earlier module.
- [ ] Root `README.md`, `CURRICULUM.md`, `SETUP.md`, `CONTRIBUTING.md`, `LICENSE`, `requirements.txt`, `pyproject.toml` all exist and are complete.
- [ ] All notebooks execute cleanly top-to-bottom.
- [ ] All internal links between modules resolve correctly.
- [ ] Module 000 specifically covers: Python's history, its guiding philosophy (Zen of Python), the breadth of applications/domains Python is used in, and an overview of Python's architecture (CPython interpreter, bytecode, how `.py` becomes running code, the PEP process) — exactly as scoped by the user.