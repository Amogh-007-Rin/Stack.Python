# Module 070: Milestone Project: Log File Analyzer — Exercises

Complete the project in `project/starter_code.py`. The solution is at `project/solution/log_analyzer.py`.

## Requirements

### Core Features

- **CLI interface** using `sys.argv` to accept:
  - Input log file path (required)
  - `--level LEVEL` to filter by severity (optional)
  - `--from DATE` and `--to DATE` to filter by date range (optional, format: YYYY-MM-DD)
  - `--export FILE` to export results to JSON (optional)

- **Log parser** that extracts from each line:
  - `timestamp` (datetime)
  - `level` (str: DEBUG, INFO, WARNING, ERROR, CRITICAL)
  - `message` (str)
  - Use regex with named groups to parse lines like:
    `2025-06-15 14:30:00 ERROR Connection timeout from 192.168.1.1`

- **Analysis**:
  - Count log entries per severity level
  - Identify top-N most frequent error messages
  - Extract unique IP addresses from error messages
  - Summary statistics (total lines, date range, level distribution)

- **Export**: Write results as JSON when `--export` is specified

### Sample Log Format

```
2025-06-15 08:12:33 INFO Server started
2025-06-15 08:15:47 WARNING Disk space at 85%
2025-06-15 09:01:12 ERROR Connection timeout from 192.168.1.1
2025-06-15 09:02:05 ERROR Connection timeout from 192.168.1.2
2025-06-15 09:05:00 INFO Retry successful
2025-06-15 10:30:22 CRITICAL Database connection lost
```

## Steps

1. Create the log parser function (regex with named groups)
2. Implement filter logic (level, date range)
3. Build the analysis engine (counts, top errors, IP extraction)
4. Wire up CLI argument parsing with `sys.argv`
5. Add JSON export functionality
6. Test with the sample log format above
