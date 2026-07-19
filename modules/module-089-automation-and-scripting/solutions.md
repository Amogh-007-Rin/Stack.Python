# Solutions: Automation & Scripting (shutil, Scheduling, File Automation)

## Exercise 1: Copy and Move
```python
import shutil
import os
from pathlib import Path

src_dir: Path = Path('test_source')
src_dir.mkdir(exist_ok=True)

(test_file := src_dir / 'hello.txt').write_text('Hello, World!')
print(f"Created file: {test_file}")

shutil.copy(test_file, 'hello_copy.txt')
print(f"Copied to hello_copy.txt: {os.path.exists('hello_copy.txt')}")

shutil.move('hello_copy.txt', 'hello_moved.txt')
print(f"Moved: moved exists={os.path.exists('hello_moved.txt')}, copy exists={os.path.exists('hello_copy.txt')}")
```

## Exercise 2: Directory Tree Walk
```python
import os
from typing import List

def print_tree(root_dir: str, indent: str = '') -> None:
    entries: List[str] = sorted(os.listdir(root_dir))
    for i, entry in enumerate(entries):
        path: str = os.path.join(root_dir, entry)
        is_last: bool = i == len(entries) - 1
        prefix: str = '└── ' if is_last else '├── '
        print(f"{indent}{prefix}{entry}")
        if os.path.isdir(path):
            extension: str = '    ' if is_last else '│   '
            print_tree(path, indent + extension)

print_tree('.')
```

## Exercise 3: File Pattern Matching
```python
import glob
import os
from typing import List

txt_files: List[str] = glob.glob('**/*.txt', recursive=True)
for filepath in txt_files:
    size: int = os.path.getsize(filepath)
    print(f"{filepath} ({size} bytes)")
```

## Exercise 4: Batch Rename
```python
import glob
import os
from typing import List

jpg_files: List[str] = sorted(glob.glob('*.jpg'))
for i, filepath in enumerate(jpg_files, 1):
    new_name: str = f"image_{i:03d}.jpg"
    os.rename(filepath, new_name)
    print(f"Renamed: {filepath} -> {new_name}")
```

## Exercise 5: Archive Creation
```python
import shutil
import os

archive_path: str = shutil.make_archive('project_backup', 'zip', '.')
print(f"Archive created: {archive_path} ({os.path.getsize(archive_path)} bytes)")

extract_dir: str = 'extracted_backup'
shutil.unpack_archive(archive_path, extract_dir)
print(f"Extracted to: {extract_dir}")
```

## Exercise 6: Remove Directory
```python
import shutil
import os

def safe_rmtree(path: str) -> None:
    if not os.path.exists(path):
        print(f"Path does not exist: {path}")
        return
    confirm: str = input(f"Delete '{path}' and all contents? (yes/no): ")
    if confirm.lower() == 'yes':
        shutil.rmtree(path)
        print(f"Deleted: {path}")
    else:
        print("Cancelled")

safe_rmtree('extracted_backup')
```

## Exercise 7: File Organizer
```python
import os
import shutil
from typing import Dict, List

EXTENSION_MAP: Dict[str, str] = {
    '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images', '.gif': 'Images',
    '.pdf': 'Documents', '.doc': 'Documents', '.docx': 'Documents', '.txt': 'Documents',
    '.mp3': 'Audio', '.wav': 'Audio', '.flac': 'Audio',
    '.zip': 'Archives', '.tar': 'Archives', '.gz': 'Archives', '.rar': 'Archives',
    '.mp4': 'Videos', '.avi': 'Videos', '.mkv': 'Videos',
}

def organize_directory(target_dir: str) -> None:
    if not os.path.isdir(target_dir):
        print(f"Not a directory: {target_dir}")
        return

    for filename in os.listdir(target_dir):
        filepath: str = os.path.join(target_dir, filename)
        if os.path.isdir(filepath):
            continue

        ext: str = os.path.splitext(filename)[1].lower()
        category: str = EXTENSION_MAP.get(ext, 'Others')
        category_dir: str = os.path.join(target_dir, category)
        os.makedirs(category_dir, exist_ok=True)

        dest: str = os.path.join(category_dir, filename)
        shutil.move(filepath, dest)
        print(f"Moved: {filename} -> {category}/")

organize_directory('downloads')
```

## Exercise 8: Scheduling
```python
import shutil
import schedule
import time
from datetime import datetime

def backup_folder(source: str, backup_root: str) -> None:
    timestamp: str = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_name: str = f"backup_{timestamp}"
    backup_path: str = f"{backup_root}/{backup_name}"
    shutil.copytree(source, backup_path)
    print(f"Backup created: {backup_path}")

schedule.every().day.at("18:00").do(
    backup_folder, source='/path/to/project', backup_root='/path/to/backups'
)

if __name__ == '__main__':
    print("Scheduler running. Press Ctrl+C to stop.")
    while True:
        schedule.run_pending()
        time.sleep(60)
```

## Challenge: Automated Download Cleaner
```python
import os
import shutil
import argparse
import logging
from typing import Dict, List

logging.basicConfig(
    filename='download_cleaner.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
)

EXTENSION_MAP: Dict[str, str] = {
    '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images', '.gif': 'Images',
    '.pdf': 'Documents', '.doc': 'Documents', '.docx': 'Documents', '.txt': 'Documents',
    '.mp3': 'Audio', '.wav': 'Audio', '.flac': 'Audio',
    '.zip': 'Archives', '.tar': 'Archives', '.gz': 'Archives', '.rar': 'Archives',
    '.mp4': 'Videos', '.avi': 'Videos', '.mkv': 'Videos',
}

def organize_downloads(download_dir: str, dry_run: bool = False) -> None:
    if not os.path.isdir(download_dir):
        print(f"Error: {download_dir} is not a directory")
        return

    moved: int = 0
    for filename in os.listdir(download_dir):
        filepath: str = os.path.join(download_dir, filename)
        if os.path.isdir(filepath):
            continue

        ext: str = os.path.splitext(filename)[1].lower()
        category: str = EXTENSION_MAP.get(ext, 'Others')
        category_dir: str = os.path.join(download_dir, category)
        dest: str = os.path.join(category_dir, filename)

        if dry_run:
            print(f"[DRY RUN] Would move: {filename} -> {category}/")
        else:
            os.makedirs(category_dir, exist_ok=True)
            shutil.move(filepath, dest)
            print(f"Moved: {filename} -> {category}/")
            logging.info(f"Moved {filename} -> {category}/")
        moved += 1

    print(f"\n{moved} files processed ({'dry run' if dry_run else 'done'})")
    logging.info(f"Organized {moved} files in {download_dir}")

def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description='Download folder organizer'
    )
    parser.add_argument('directory', help='Directory to organize')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done')
    args: argparse.Namespace = parser.parse_args()

    organize_downloads(args.directory, dry_run=args.dry_run)

if __name__ == '__main__':
    main()
```
```bash
# Schedule with cron (Linux/macOS):
# 0 9 * * * cd /path/to/script && python download_cleaner.py ~/Downloads
```
