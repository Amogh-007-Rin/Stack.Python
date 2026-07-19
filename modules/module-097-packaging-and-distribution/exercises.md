# Exercises: Packaging and Distributing Python Projects (PyPI)

## Exercise 1: Minimal Package Structure
Create a Python package called `calculator` with a single module `ops.py` containing `add`, `subtract`, `multiply`, `divide`. Include a `pyproject.toml`.

## Exercise 2: Metadata
Add proper metadata to your package: author, description, license (MIT), Python version classifiers, and a `README.md`.

## Exercise 3: __version__ Convention
Add `__version__ = "0.1.0"` to your package's `__init__.py`. Write a script that imports and prints the version.

## Exercise 4: CLI Script
Add a console script entry point in `pyproject.toml` so that `calculator` runs a CLI that accepts two numbers and an operation.

## Exercise 5: Build and Test
Build both source distribution (sdist) and wheel. Use `twine check` to verify the distribution.

## Exercise 6: Semantic Versioning
Given version 1.3.0, determine what the new version should be for:
- A bug fix
- A new backward-compatible feature
- A breaking API change

## Challenge: Upload to Test PyPI
Create a Test PyPI account, configure `~/.pypirc`, build your package, and upload it. Then install it from Test PyPI and verify it works.
