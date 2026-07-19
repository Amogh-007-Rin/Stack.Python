# Module 097: Packaging and Distributing Python Projects (PyPI)

- **Phase:** 10. Concurrency & Internals
- **Duration:** 2 hours

## Learning Objectives

- Create a pyproject.toml for modern Python packaging
- Understand setup.py vs pyproject.toml
- Build source distributions (sdist) and wheels
- Upload packages to PyPI with twine
- Apply semantic versioning (semver)
- Add project metadata (authors, classifiers, README)

## Topics Covered

1. pyproject.toml (modern packaging)
2. setup.py vs pyproject.toml
3. setuptools
4. Creating source distributions (sdist) and wheels
5. Uploading to PyPI (twine)
6. Version numbering (semver)
7. Project metadata (authors, classifiers, README)
8. __version__ convention

## Prerequisites

Modules 000-096.

## Key Concepts

```toml
# pyproject.toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.backends._legacy:_Backend"

[project]
name = "mypackage"
version = "0.1.0"
description = "A short description"
readme = "README.md"
license = {text = "MIT"}
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
]
dependencies = [
    "requests>=2.25",
]
```

```python
# __init__.py
__version__: str = "0.1.0"
```

```bash
# Build and publish
python -m build
twine upload dist/*
```

## Resources

- Python packaging guide: https://packaging.python.org
- pyproject.toml specification: https://peps.python.org/pep-0621
- semver.org

## Next Module

Module 098: Performance Optimization & Profiling
