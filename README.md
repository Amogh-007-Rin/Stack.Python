# Stack.Python 🐍

**A 0–100, linear, project-based Python learning sandbox for absolute beginners.**

Take a learner with zero programming experience from Module 0 (Python's history and philosophy) to Module 100 (full-stack application deployment). Every module builds on everything before it — no gaps, no forward references.

## Learning Path

| Phase | Modules | Topic |
|---|---|---|
| **0. Orientation** | 000–001 | Introduction & Setup |
| **1. Fundamentals** | 002–010 | First programs, variables, types, I/O, operators, strings, numbers |
| **2. Control Flow & Data** | 011–020 | Booleans, conditionals, loops, lists |
| **3. Data Structures** | 021–030 | Tuples, sets, dicts, collections |
| **4. Functions** | 031–040 | Functions, scope, lambdas, recursion, decorators, generators |
| **5. OOP** | 041–050 | Classes, inheritance, polymorphism, dunder methods |
| **6. Advanced OOP & Errors** | 051–060 | Composition, properties, dataclasses, error handling, files |
| **7. Modules, Stdlib & Testing** | 061–070 | JSON, context managers, regex, dates, logging |
| **8. Data, Web & APIs** | 071–080 | Type hints, testing, APIs, pandas, web scraping |
| **9. Databases & Web Apps** | 081–090 | SQLite, SQLAlchemy, Flask, FastAPI, automation |
| **10. Concurrency & Internals** | 091–098 | Threading, multiprocessing, asyncio, memory management |
| **11. Capstone** | 099–100 | Full-stack application & next steps |

Milestone projects appear roughly every 10 modules — build a calculator, a to-do app, a text adventure, an expense tracker, a weather dashboard, and more.

## Quickstart

```bash
git clone https://github.com/your-org/Stack.Python.git
cd Stack.Python
python3.12 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Then open `modules/module-000-introduction-to-python/README.md` and start learning!

## How to Use This Repo

1. **Go in order.** Each module assumes you know everything from all prior modules.
2. **Read the lesson.** Start with `README.md` for each module.
3. **Follow the notebook.** Open `notebook.ipynb` and run the examples interactively.
4. **Do the exercises.** Attempt `exercises.md` before checking `solutions.py`/`solutions.md`.
5. **Take the quiz.** `quiz.md` helps reinforce what you learned.
6. **Build the projects.** Milestone modules have a `project/` folder with real builds.
7. **Track progress.** Run `python scripts/check_progress.py` to see your completion status.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to propose fixes, additions, or improvements.

## License

MIT — see [LICENSE](LICENSE).
