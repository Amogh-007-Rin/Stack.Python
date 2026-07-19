# Module 069: Logging — Solutions

```python
import logging
import os


# 1. basicConfig
logging.basicConfig(level=logging.INFO)
logging.debug("This is DEBUG")
logging.info("This is INFO")
logging.warning("This is WARNING")
logging.error("This is ERROR")
logging.critical("This is CRITICAL")


# 2. File logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",
    filemode="w",
    force=True,
)
for i in range(5):
    logging.info(f"Log entry {i + 1}")

with open("app.log") as f:
    print(f.read())


# 3. Logger objects
logger_app = logging.getLogger("app")
logger_net = logging.getLogger("app.network")
logger_app.setLevel(logging.DEBUG)
logger_net.setLevel(logging.WARNING)

# Add console handler for visibility
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(name)s - %(levelname)s: %(message)s"))
logger_app.addHandler(handler)

logger_app.info("App info message")
logger_net.debug("Network debug (should not appear)")
logger_net.warning("Network warning")


# 4. Multiple handlers
logger = logging.getLogger("multi_handler")
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter("[CONSOLE] %(message)s"))

file_h = logging.FileHandler("multi.log", mode="w")
file_h.setLevel(logging.DEBUG)
file_h.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

logger.addHandler(console)
logger.addHandler(file_h)

logger.debug("Debug to file only")
logger.info("Info to both")


# 5. Custom formatter
custom_fmt = logging.Formatter(
    "[%(asctime)s] [%(name)s] %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
handler = logging.StreamHandler()
handler.setFormatter(custom_fmt)

logger = logging.getLogger("custom")
logger.addHandler(handler)
logger.setLevel(logging.INFO)
logger.info("This uses a custom formatter")


# 6. Logging vs print refactor
# Before: print(f"Starting process...")
# After:
logger = logging.getLogger("refactored")
logging.basicConfig(level=logging.INFO, force=True)
logger.info("Starting process...")
logger.warning("Disk space low")
logger.error("Failed to connect")


# Cleanup
for f in ["app.log", "multi.log"]:
    try:
        os.remove(f)
    except FileNotFoundError:
        pass
```
