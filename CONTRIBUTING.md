# Contributing to Stack.Python

Thank you for considering contributing! This project aims to be a high-quality, beginner-friendly Python curriculum.

## How to Contribute

### Reporting Issues
- Open a GitHub issue describing the problem
- Include the module number, file, and a clear description
- For content errors: note the incorrect content and what it should say

### Proposing Changes

1. Fork the repository
2. Create a feature branch: `git checkout -b fix/module-XXX-description`
3. Make your changes
4. Run quality checks: `black . && ruff check . && mypy .`
5. Submit a pull request

### Adding a New Module

Use the scaffolding script:

```bash
python scripts/new_module.py --number XXX --title "Your Title" --phase "Phase Name"
```

This creates the folder with stub files. Follow the existing module template structure.

## Style Rules

- **PEP 8** — all Python code must conform
- **Google-style docstrings** — required for all functions/classes (from Module 031 onward, type hints from Module 073 onward)
- **Type hints** — required for all new code in modules 073+
- **Tests** — if you change exercises or add content that can be tested, include test updates
- **Quizzes** — if you add significant content, add corresponding quiz questions
- **No forward references** — never reference a concept taught in a later module
- **Line length** — 88 characters (Black default)

## Review Process

All PRs are reviewed for:
- Pedagogical correctness (is the explanation clear and accurate?)
- Technical correctness (does the code run?)
- Style compliance (PEP 8, docstrings, type hints)
- Linearity (no forward references)
