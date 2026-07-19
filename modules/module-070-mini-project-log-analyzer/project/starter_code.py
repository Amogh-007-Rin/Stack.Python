"""
Log File Analyzer — Starter Code.

TODO: Implement the log parser, filter, analyzer, and CLI.

Usage:
    python project/starter_code.py <logfile> [--level LEVEL] [--from DATE] [--to DATE] [--export FILE]
"""

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
    """Represents a single parsed log entry."""

    def __init__(self, timestamp: datetime, level: str, message: str) -> None:
        # TODO: store attributes
        raise NotImplementedError

    def to_dict(self) -> dict:
        """Serialize entry to a JSON-compatible dict."""
        # TODO: return dict with timestamp (str), level, message
        raise NotImplementedError


def parse_log(filepath: str) -> list[LogEntry]:
    """Parse a log file into a list of LogEntry objects."""
    # TODO: open file, match each line against LOG_PATTERN,
    #       create LogEntry for each match
    raise NotImplementedError


def filter_entries(
    entries: list[LogEntry],
    level: Optional[str] = None,
    date_from: Optional[str] = None,
    date_to: Optional[str] = None,
) -> list[LogEntry]:
    """Filter log entries by level and/or date range."""
    # TODO: apply filters sequentially
    raise NotImplementedError


def analyze(entries: list[LogEntry]) -> dict:
    """Compute summary statistics from log entries."""
    # TODO: count by level, find top-5 error messages,
    #       extract unique IPs, determine date range
    raise NotImplementedError


def export_results(results: dict, filepath: str) -> None:
    """Export analysis results to a JSON file."""
    # TODO: write results dict as formatted JSON
    raise NotImplementedError


def print_summary(results: dict) -> None:
    """Print a human-readable summary of the analysis."""
    # TODO: display total entries, date range, level distribution,
    #       top errors, and unique IPs
    raise NotImplementedError


def main() -> None:
    """Parse CLI args and run the log analyzer."""
    # TODO: handle sys.argv, parse --level, --from, --to, --export
    #       call parse_log -> filter_entries -> analyze -> print_summary
    #       handle --export if provided
    print("Log File Analyzer")
    print("Usage: python starter_code.py <logfile> [--level LEVEL] [--from DATE] [--to DATE] [--export FILE]")


if __name__ == "__main__":
    main()
