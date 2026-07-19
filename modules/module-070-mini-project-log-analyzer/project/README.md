# Log File Analyzer — Project

A CLI tool that reads, parses, filters, analyzes, and exports log file data.

## Features

- Parse log entries with regex (timestamp, level, message)
- Filter by severity level and date range
- Count entries per severity level
- Identify top error messages
- Extract unique IP addresses from errors
- Export results to JSON

## Usage

```bash
python project/solution/log_analyzer.py sample.log
python project/solution/log_analyzer.py sample.log --level ERROR
python project/solution/log_analyzer.py sample.log --from 2025-06-01 --to 2025-06-15
python project/solution/log_analyzer.py sample.log --export results.json
```

## Sample Log Format

```
2025-06-15 08:12:33 INFO Server started
2025-06-15 08:15:47 WARNING Disk space at 85%
2025-06-15 09:01:12 ERROR Connection timeout from 192.168.1.1
```

## Starter Code

Open `starter_code.py` and follow the TODO comments to implement the full solution.

## Requirements

- Python 3.10+
- No external dependencies
