# Module 069: Logging — Exercises

1. **basicConfig**: Configure logging with `basicConfig` to show messages at INFO level and above. Log one message at each level: DEBUG, INFO, WARNING, ERROR, CRITICAL.

2. **File logging**: Set up logging to write to a file `app.log` with a format `"%(asctime)s - %(levelname)s - %(message)s"`. Write 5 log entries and verify the file contents.

3. **Logger objects**: Create two named loggers: `"app"` and `"app.network"`. Set different levels for each. Log messages to both and observe the hierarchy.

4. **Handlers**: Create a logger that has both a `StreamHandler` (console) and a `FileHandler` (file). Set different formatters for each handler.

5. **Custom formatter**: Create a custom formatter that includes the timestamp, logger name, level, and message in the format: `"[2025-06-15 14:30:00] [app] INFO: message"`. Apply it to a handler.

6. **Logging vs print**: Refactor a simple script that currently uses `print()` for status messages to use `logging` instead. Use appropriate levels: INFO for normal operation, WARNING for recoverable issues, ERROR for failures.
