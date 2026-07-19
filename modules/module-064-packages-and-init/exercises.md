# Module 064: Packages and \_\_init\_\_.py — Exercises

1. **Basic package**: Create a directory `mypackage/` with an empty `__init__.py` and a module `math_ops.py` containing `add` and `subtract` functions. Import and call them from outside the package.

2. **Package initialization**: Add code to `__init__.py` that imports `add` and `subtract` from `math_ops` so users can write `from mypackage import add` directly.

3. **Subpackages**: Create a subpackage `mypackage/advanced/` with a module `calc.py` containing `factorial(n)`. Use both absolute and relative imports to access it from outside.

4. **__all__**: Define `__all__` in `mypackage/__init__.py` to only expose `add`. Verify that `from mypackage import *` only imports `add`.

5. **Relative imports**: Inside `mypackage/advanced/calc.py`, use a relative import to import `add` from `mypackage.math_ops`. Demonstrate it works.

6. **Namespace package**: Create two directories `namespace_pkg/sub_a/` and `namespace_pkg/sub_b/` without `__init__.py` files. Place modules in each. Show that Python can still discover them as a namespace package.
