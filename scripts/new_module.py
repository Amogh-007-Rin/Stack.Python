"""Scaffold a new module folder from the standard template."""

import argparse
import os
from pathlib import Path


MODULES_DIR = Path(__file__).resolve().parent.parent / "modules"


MODULE_FILES = {
    "README.md": """# Module {number:03d}: {title}

> **Phase:** {phase}  |  **Estimated time:** 1-2 hours  |  **Milestone Project:** {milestone}

## Prerequisites
- No prior knowledge assumed.

## Learning Objectives
By the end of this module, you will be able to:
- Understand the core concepts of {title}
- Apply these concepts in Python code

## Why This Matters
This topic is foundational to programming in Python.

## Concept Explanation
Content goes here.

## Common Pitfalls
- Common mistake 1
- Common mistake 2

## Hands-On Walkthrough
Step-by-step guided example.

## Key Takeaways
- Key point 1

## Further Reading
- [Official Python Docs](https://docs.python.org/3/)

## Next Module
- Teaser for the next module.
""",
    "notebook.ipynb": """{"cells":[],"metadata":{"kernelspec":{"display_name":"Python 3","language":"python","name":"python3"}},"nbformat":4,"nbformat_minor":5}""",
    "exercises.md": """# Exercises

## Warm-Up
1. Simple exercise.

## Core
2. Core exercise.

## Challenge
3. Challenge exercise.

## Stretch
4. Stretch exercise.
""",
    "solutions.md": """# Solutions

## 1. Warm-Up
```python
# Solution
```

## 2. Core
```python
# Solution
```

## 3. Challenge
```python
# Solution
```

## 4. Stretch
```python
# Solution
```
""",
    "quiz.md": """# Quiz

1. Question 1?
   - [ ] A) Option A
   - [ ] B) Option B
   - [ ] C) Option C

## Answers
1. B
""",
}

PROJECT_FILES = {
    "project/README.md": "# Project: {title}\n\nProject brief goes here.\n",
    "project/starter_code.py": "# TODO: Implement the project\n",
    "project/solution/__init__.py": "",
}


def main():
    parser = argparse.ArgumentParser(description="Scaffold a new module")
    parser.add_argument("--number", type=int, required=True, help="Module number (0-100)")
    parser.add_argument("--title", required=True, help="Module title")
    parser.add_argument("--phase", default="", help="Phase name")
    parser.add_argument("--milestone", default="No", choices=["Yes", "No"], help="Milestone project?")
    parser.add_argument("--slug", help="Folder slug (auto-generated if omitted)")
    args = parser.parse_args()

    if args.slug:
        slug = args.slug
    else:
        slug = f"module-{args.number:03d}-" + args.title.lower().replace(" ", "-").replace(",", "").replace(":", "").replace("(", "").replace(")", "").replace("/", "-")
        slug = slug.replace("--", "-").strip("-")

    module_dir = MODULES_DIR / slug
    if module_dir.exists():
        print(f"Error: {module_dir} already exists.")
        return 1

    module_dir.mkdir(parents=True)

    for filename, content in MODULE_FILES.items():
        file_content = content.format(number=args.number, title=args.title, phase=args.phase, milestone=args.milestone)
        (module_dir / filename).write_text(file_content)

    if args.milestone == "Yes":
        for rel_path, content in PROJECT_FILES.items():
            full_path = module_dir / rel_path
            full_path.parent.mkdir(parents=True, exist_ok=True)
            file_content = content.format(number=args.number, title=args.title)
            full_path.write_text(file_content)

    print(f"Created module at {module_dir}")
    return 0


if __name__ == "__main__":
    exit(main())
