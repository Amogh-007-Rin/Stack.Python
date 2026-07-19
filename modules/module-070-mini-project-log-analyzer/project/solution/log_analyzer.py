#!/usr/bin/env python3
"""
Log File Analyzer — Full Solution.

Reads, parses, filters, analyzes, and exports log files.

Usage:
    python project/solution/log_analyzer.py <logfile> [--level LEVEL] [--from DATE] [--to DATE] [--export FILE]
"""

import json
import re
import sys
from collections import Counter
from datetime import datetime
from typing import Optional


LOG_PATTERN = re.compile(
    r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+"
    r"(?P<level>DEBUG|INFO|WARNING|ERROR|CRITICAL)\s+"
    r"(?P<message>.+)"
)

IP_PATTERN = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")


class LogEntry:
    """Represents a single parsed log entry.

    Attributes:
        timestamp: Datetime object of the log entry.
        level: Severity level string.
        message: Log message content.
    """

    def __init__(self, timestamp: datetime, level: str, message: str) -> None:
        self.timestamp = timestamp
        self.level = level
        self.message = message

    def to_dict(self) -> dict:
        """Serialize entry to a JSON-compatible dict."""
        return {
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "level": self.level,
            "message": self.message,
        }


def parse_log(filepath: str) -> list[LogEntry]:
    """Parse a log file into a list of LogEntry objects.

    Args:
        filepath: Path to the log file.

    Returns:
        List of parsed LogEntry objects.

    Raises:
        FileNotFoundError: If the log file does not exist.
    """
    entries: list[LogEntry] = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            m = LOG_PATTERN.match(line)
            if m:
                ts = datetime.strptime(m.group("timestamp"), "%Y-%m-%d %H:%M:%S")
                entries.append(LogEntry(ts, m.group("level"), m.group("message")))
    return entries


def filter_entries(
    entries: list[LogEntry],
    level: Optional[str] = None,
    date_from: Optional[str] = None,
    date_to: Optional[str] = None,
) -> list[LogEntry]:
    """Filter log entries by level and/or date range.

    Args:
        entries: List of log entries.
        level: Optional severity level filter (case-insensitive).
        date_from: Optional start date (YYYY-MM-DD), inclusive.
        date_to: Optional end date (YYYY-MM-DD), inclusive.

    Returns:
        Filtered list of log entries.
    """
    result = entries

    if level:
        result = [e for e in result if e.level.upper() == level.upper()]

    if date_from:
        from_dt = datetime.strptime(date_from, "%Y-%m-%d")
        result = [e for e in result if e.timestamp >= from_dt]

    if date_to:
        to_dt = datetime.strptime(date_to, "%Y-%m-%d").replace(
            hour=23, minute=59, second=59
        )
        result = [e for e in result if e.timestamp <= to_dt]

    return result


def analyze(entries: list[LogEntry]) -> dict:
    """Compute summary statistics from log entries.

    Args:
        entries: List of log entries.

    Returns:
        Dictionary containing level counts, top errors, IPs, and summary.
    """
    level_counts: dict[str, int] = Counter(e.level for e in entries)

    error_entries = [e for e in entries if e.level in ("ERROR", "CRITICAL")]
    error_messages = Counter(e.message for e in error_entries)
    top_errors = error_messages.most_common(5)

    all_ips: list[str] = []
    for e in error_entries:
        all_ips.extend(IP_PATTERN.findall(e.message))
    unique_ips = sorted(set(all_ips))

    timestamps = [e.timestamp for e in entries]
    date_range = {}
    if timestamps:
        date_range = {
            "from": min(timestamps).strftime("%Y-%m-%d %H:%M:%S"),
            "to": max(timestamps).strftime("%Y-%m-%d %H:%M:%S"),
        }

    return {
        "total_entries": len(entries),
        "date_range": date_range,
        "level_counts": dict(level_counts),
        "top_errors": top_errors,
        "unique_ips": unique_ips,
    }


def export_results(results: dict, filepath: str) -> None:
    """Export analysis results to a JSON file.

    Args:
        results: Analysis results dictionary.
        filepath: Destination JSON file path.
    """
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"Results exported to {filepath}")


def print_summary(results: dict) -> None:
    """Print a human-readable summary of the analysis.

    Args:
        results: Analysis results dictionary.
    """
    print("\n" + "=" * 50)
    print("  LOG FILE ANALYSIS SUMMARY")
    print("=" * 50)
    print(f"  Total entries:    {results['total_entries']}")
    if results["date_range"]:
        print(f"  Date range:       {results['date_range']['from']} to {results['date_range']['to']}")
    print()
    print("  Level distribution:")
    for level in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
        count = results["level_counts"].get(level, 0)
        bar = "█" * min(count, 40)
        print(f"    {level:<10} {count:>5}  {bar}")
    print()

    if results["top_errors"]:
        print("  Top error messages:")
        for msg, count in results["top_errors"]:
            print(f"    [{count:>3}] {msg[:70]}")

    if results["unique_ips"]:
        print(f"\n  Unique IPs found: {len(results['unique_ips'])}")
        for ip in results["unique_ips"][:10]:
            print(f"    {ip}")
        if len(results["unique_ips"]) > 10:
            print(f"    ... and {len(results['unique_ips']) - 10} more")
    print("=" * 50)


def main() -> None:
    """Parse CLI args and run the log analyzer."""
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print("Usage: python log_analyzer.py <logfile> [--level LEVEL] [--from DATE] [--to DATE] [--export FILE]")
        sys.exit(0)

    logfile = args[0]
    level: Optional[str] = None
    date_from: Optional[str] = None
    date_to: Optional[str] = None
    export_path: Optional[str] = None

    i = 1
    while i < len(args):
        if args[i] == "--level" and i + 1 < len(args):
            level = args[i + 1]
            i += 2
        elif args[i] == "--from" and i + 1 < len(args):
            date_from = args[i + 1]
            i += 2
        elif args[i] == "--to" and i + 1 < len(args):
            date_to = args[i + 1]
            i += 2
        elif args[i] == "--export" and i + 1 < len(args):
            export_path = args[i + 1]
            i += 2
        else:
            print(f"Unknown argument: {args[i]}")
            sys.exit(1)

    try:
        entries = parse_log(logfile)
    except FileNotFoundError:
        print(f"Error: File not found: {logfile}")
        sys.exit(1)

    filtered = filter_entries(entries, level=level, date_from=date_from, date_to=date_to)
    results = analyze(filtered)

    print_summary(results)

    if export_path:
        export_results(results, export_path)


if __name__ == "__main__":
    main()
