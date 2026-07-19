# Module 065: Virtual Environments and pip — Exercises

1. **Create a venv**: Create a new virtual environment named `test_env` using `python -m venv`. Activate it and verify the Python interpreter path.

2. **Install a package**: Inside the activated venv, install the `requests` package using pip. Verify it's installed with `pip list`.

3. **Freeze requirements**: Generate a `requirements.txt` file with `pip freeze`. Examine its contents and verify `requests` is listed.

4. **Install from requirements**: Deactivate the environment, create a second venv, and install all packages from the `requirements.txt` generated in exercise 3.

5. **Uninstall a package**: Inside the first venv, uninstall `requests` with `pip uninstall`. Verify it's gone with `pip list`.

6. **Pip vs conda**: Research and write a short paragraph (in comments) comparing pip and conda. Explain when you might choose one over the other.
