"""Dev utility: executes every notebook via papermill.

Usage:
    python scripts/run_all_notebooks.py
    python scripts/run_all_notebooks.py --start 0 --end 10
    python scripts/run_all_notebooks.py --parallel
"""

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed


MODULES_DIR = Path(__file__).resolve().parent.parent / "modules"


def run_notebook(notebook_path: Path) -> tuple[str, bool, str]:
    """Execute a single notebook with papermill. Returns (slug, success, message)."""
    slug = notebook_path.parent.name
    with tempfile.NamedTemporaryFile(suffix=".ipynb", delete=False) as tmp:
        output_path = tmp.name

    try:
        result = subprocess.run(
            [
                sys.executable, "-m", "papermill",
                str(notebook_path),
                str(output_path),
                "--kernel", "python3",
                "--cwd", str(notebook_path.parent),
            ],
            capture_output=True, text=True, timeout=300,
        )
        if result.returncode == 0:
            return slug, True, "OK"
        else:
            return slug, False, result.stderr[:500]
    except subprocess.TimeoutExpired:
        return slug, False, "Timeout (300s)"
    except Exception as e:
        return slug, False, str(e)
    finally:
        Path(output_path).unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description="Execute all notebooks via papermill")
    parser.add_argument("--start", type=int, default=0, help="Start module index")
    parser.add_argument("--end", type=int, default=100, help="End module index")
    parser.add_argument("--parallel", action="store_true", help="Run notebooks in parallel")
    args = parser.parse_args()

    notebooks = []
    for d in sorted(MODULES_DIR.iterdir()):
        if d.is_dir() and d.name.startswith("module-"):
            parts = d.name.split("-", 2)
            try:
                num = int(parts[1])
            except (IndexError, ValueError):
                continue
            if args.start <= num <= args.end:
                nb = d / "notebook.ipynb"
                if nb.exists():
                    notebooks.append(nb)

    print(f"Found {len(notebooks)} notebooks to execute")

    if args.parallel:
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = {executor.submit(run_notebook, nb): nb.parent.name for nb in notebooks}
            for future in as_completed(futures):
                slug, success, msg = future.result()
                status = "OK" if success else "FAIL"
                print(f"  [{status}] {slug}")
                if not success:
                    print(f"    Error: {msg}")
    else:
        failures = 0
        for nb in notebooks:
            slug, success, msg = run_notebook(nb)
            status = "OK" if success else "FAIL"
            print(f"  [{status}] {slug}")
            if not success:
                print(f"    Error: {msg}")
                failures += 1

        if failures:
            print(f"\n{ failures } notebook(s) failed.")
            return 1

    print("\nAll notebooks executed successfully.")
    return 0


if __name__ == "__main__":
    exit(main())
