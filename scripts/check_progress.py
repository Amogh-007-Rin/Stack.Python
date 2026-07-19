"""CLI tool: prints the learner's completion checklist.

Usage:
    python scripts/check_progress.py --completed 0 1 2 3 10
    python scripts/check_progress.py --start 0 --end 10
"""

import argparse
import sys
from pathlib import Path


MODULES_DIR = Path(__file__).resolve().parent.parent / "modules"

PHASES = [
    (0, "0. Orientation"),
    (2, "1. Fundamentals"),
    (11, "2. Control Flow & Data"),
    (21, "3. Data Structures"),
    (31, "4. Functions"),
    (41, "5. OOP"),
    (51, "6. Advanced OOP & Errors"),
    (61, "7. Modules, Stdlib & Testing"),
    (71, "8. Data, Web & APIs"),
    (81, "9. Databases & Web Apps"),
    (91, "10. Concurrency & Internals"),
    (99, "11. Capstone"),
]


def get_module_slugs():
    slugs = {}
    for d in sorted(MODULES_DIR.iterdir()):
        if d.is_dir() and d.name.startswith("module-"):
            parts = d.name.split("-", 2)
            try:
                num = int(parts[1])
                slugs[num] = d.name
            except (IndexError, ValueError):
                pass
    return slugs


def main():
    parser = argparse.ArgumentParser(description="Check module completion progress")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--completed", nargs="*", type=int, help="List of completed module numbers")
    group.add_argument("--start", type=int, default=0, help="Start module (inclusive)")
    parser.add_argument("--end", type=int, default=100, help="End module (inclusive)")

    args = parser.parse_args()

    if args.completed is not None:
        completed = set(args.completed)
    else:
        completed = set(range(args.start, args.end + 1))

    slugs = get_module_slugs()
    total = len(slugs)

    print(f"Stack.Python Progress ({len(completed)}/{total} modules completed)")
    print("=" * 60)

    phase_idx = 0
    for i in range(0, 101):
        if i not in slugs:
            continue

        # Print phase header
        if phase_idx < len(PHASES) - 1 and i >= PHASES[phase_idx + 1][0]:
            phase_idx += 1
        if i == PHASES[phase_idx][0]:
            print(f"\n--- Phase {PHASES[phase_idx][1]} ---")

        marker = "[x]" if i in completed else "[ ]"
        name = slugs[i]
        # Truncate the module name for display
        display = name.replace("module-", "Mod ").replace("-", " ").strip()
        print(f"  {marker} {i:03d}: {display}")

    print("\n" + "=" * 60)
    print(f"Total: {len(completed)}/{total} complete ({100 * len(completed) // total}%)")


if __name__ == "__main__":
    main()
