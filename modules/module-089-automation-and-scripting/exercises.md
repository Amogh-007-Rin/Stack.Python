# Exercises: Automation & Scripting (shutil, Scheduling, File Automation)

## Exercise 1: Copy and Move
Create a source directory with a few test files. Use `shutil.copy` and `shutil.move` to duplicate and relocate files. Verify the results.

## Exercise 2: Directory Tree Walk
Write a script that uses `os.walk` to traverse a directory and print a tree-like structure showing all files and subdirectories.

## Exercise 3: File Pattern Matching
Use `glob` to find all `.txt` files in a directory tree. Print their absolute paths and sizes.

## Exercise 4: Batch Rename
Write a script that renames all `.jpg` files in a directory to `image_001.jpg`, `image_002.jpg`, etc. Handle files with existing numeric suffixes.

## Exercise 5: Archive Creation
Use `shutil.make_archive` to create a ZIP archive of a project directory. Then extract it to a different location to verify.

## Exercise 6: Remove Directory
Use `shutil.rmtree` to delete a directory and all its contents. Add safety checks (confirm before delete).

## Exercise 7: File Organizer
Write a script that organizes files in a directory by extension. Move files into subdirectories: `Images/`, `Documents/`, `Audio/`, `Archives/`, `Others/`.

## Exercise 8: Scheduling
Use the `schedule` library to run a backup script every day at 6:00 PM. The script should copy a specified folder to a backup location with a timestamp.

## Challenge: Automated Download Cleaner
Build a script that:
- Monitors a Downloads folder
- Organizes files by type into subfolders (Images, Documents, Videos, Archives, Others)
- Logs all actions to a log file with timestamps
- Can be scheduled to run daily
- Dry-run mode (--dry-run) that shows what would be done without actually moving files
