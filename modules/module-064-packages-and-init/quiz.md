# Module 064: Packages and \_\_init\_\_.py — Quiz

1. **What is the minimum requirement for a directory to be a regular package?**
   - a) A `__init__.py` file
   - b) A `__main__.py` file
   - c) A `setup.py` file
   - d) At least two modules

2. **Which import syntax performs a relative import from a sibling module?**
   - a) `from . import sibling`
   - b) `from .. import sibling`
   - c) `import .sibling`
   - d) `import ../sibling`

3. **What does `__all__` control?**
   - a) Which modules are imported at startup
   - b) Which names are exported by `from package import *`
   - c) The list of subpackages
   - d) The module search path

4. **What is a namespace package (PEP 420)?**
   - a) A package with `__init__.py` that uses `__import__`
   - b) A package without an `__init__.py` file
   - c) A package installed via pip
   - d) A package with `namespace = True`

5. **Which import is an absolute import?**
   - a) `from . import utils`
   - b) `from ..config import settings`
   - c) `from mypackage import utils`
   - d) `from ...root import func`

<details>
<summary>Answers</summary>
1-a, 2-a, 3-b, 4-b, 5-c
</details>
