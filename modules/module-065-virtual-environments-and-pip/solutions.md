# Module 065: Virtual Environments and pip — Solutions

```python
# 1. Create a venv
# $ python -m venv test_env
# $ source test_env/bin/activate
# $ which python
# Output: .../test_env/bin/python


# 2. Install a package
# (test_env) $ pip install requests
# (test_env) $ pip list
# Output includes: requests  2.x.x


# 3. Freeze requirements
# (test_env) $ pip freeze > requirements.txt
# Contents of requirements.txt:
# certifi==2024.x.x
# charset-normalizer==x.x.x
# idna==x.x.x
# requests==2.x.x
# urllib3==x.x.x


# 4. Install from requirements
# $ deactivate
# $ python -m venv test_env2
# $ source test_env2/bin/activate
# (test_env2) $ pip install -r requirements.txt


# 5. Uninstall a package
# (test_env) $ pip uninstall requests -y
# (test_env) $ pip list
# requests should no longer appear


# 6. Pip vs conda
"""
Pip is Python's default package manager, installing from PyPI.
Conda is a cross-language package manager from Anaconda, popular in
data science. Conda handles non-Python dependencies and manages
environments natively. Use pip for general Python development;
use conda when working with scientific/numerical stacks (numpy,
pandas) where binary dependency resolution matters.
"""
print("See comments above for pip vs conda comparison")
```
