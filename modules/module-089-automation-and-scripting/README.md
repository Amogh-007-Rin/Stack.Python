# Module 089: Automation & Scripting (shutil, Scheduling, File Automation)

- **Phase:** 9. Databases & Web Apps
- **Duration:** 2 hours

## Learning Objectives

- Copy, move, and archive files with shutil
- Match file patterns with glob
- Walk directory trees with os.walk
- Schedule tasks with the schedule library
- Build file organization and backup scripts

## Topics Covered

1. shutil module: copy, move, rmtree, make_archive
2. glob for file pattern matching
3. os.walk for directory traversal
4. Scheduling with schedule library or cron
5. File organization scripts
6. Batch file renaming
7. Backup scripts

## Prerequisites

Modules 000-088.

## Key Concepts

```python
import shutil
import glob
import os
from typing import List

# Copy and archive
shutil.copy('source.txt', 'backup.txt')
shutil.make_archive('backup', 'zip', 'data_folder')

# File pattern matching
pdf_files: List[str] = glob.glob('**/*.pdf', recursive=True)

# Directory traversal
for dirpath, dirnames, filenames in os.walk('project'):
    for f in filenames:
        print(os.path.join(dirpath, f))

# Scheduling
import schedule
import time

def job() -> None:
    print("Running automated task...")

schedule.every().day.at("09:00").do(job)
```

## Resources

- Python shutil documentation
- Python glob documentation
- schedule library: https://pypi.org/project/schedule
- Cron how-to (Linux/macOS)
