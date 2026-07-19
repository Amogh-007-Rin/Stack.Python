"""
Module 099: Capstone Project - Full-Stack Application (Solutions)

This file contains solution code for the exercises.
The complete project solution is in project/solution/.
"""

# Exercise 1: Database Models
# See project/solution/models.py

# Exercise 2: CRUD Endpoints
# See project/solution/app.py

# Exercise 3: Input Validation
# See project/solution/schemas.py

# Exercise 4: Data Ingestion
# See project/solution/app.py (POST /tasks/import endpoint)

# Exercise 5: Web UI with Jinja2
# See project/solution/templates/

# Exercise 6: Error Handling
# See project/solution/app.py (exception handlers)

# Challenge: Dashboard with Statistics
# See project/solution/app.py (GET /dashboard endpoint)


def verify_setup() -> None:
    """Verify that the project solution is properly structured.

    Raises:
        ImportError: If required modules cannot be imported.
    """
    import importlib
    import sys
    from pathlib import Path
    from typing import List

    solution_dir: Path = Path(__file__).parent / 'project' / 'solution'
    sys.path.insert(0, str(solution_dir))

    required_modules: List[str] = [
        'models', 'database', 'schemas', 'app'
    ]

    for module_name in required_modules:
        try:
            importlib.import_module(module_name)
            print(f"  ✓ {module_name}.py loaded successfully")
        except ImportError as e:
            print(f"  ✗ {module_name}.py failed: {e}")

    sys.path.remove(str(solution_dir))


if __name__ == '__main__':
    print("Verifying Capstone Project Solution...")
    verify_setup()
