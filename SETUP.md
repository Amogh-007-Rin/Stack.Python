# Setup Guide

## Installing Python 3.12+

### Windows
1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Download Python 3.12+ for Windows
3. Run the installer — **check "Add Python to PATH"** at the bottom of the first screen
4. Click "Install Now"
5. Verify: open Command Prompt and run `python --version`

### macOS
1. Install [Homebrew](https://brew.sh/) if you don't have it: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
2. Run: `brew install python@3.12`
3. Verify: `python3 --version`

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3.12 python3.12-venv python3-pip
python3.12 --version
```

### Linux (Fedora)
```bash
sudo dnf install python3.12
python3.12 --version
```

## Creating a Virtual Environment

A virtual environment keeps your project dependencies isolated.

### Windows (Command Prompt)
```bash
python -m venv venv
venv\Scripts\activate
```

### Windows (PowerShell)
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### macOS / Linux
```bash
python3.12 -m venv venv
source venv/bin/activate
```

After activation, your terminal prompt will show `(venv)`.

## Install Dependencies

With the virtual environment activated:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Launching Jupyter Notebook

### Option 1: Terminal
```bash
jupyter notebook
```
This opens the Jupyter dashboard in your browser. Navigate to any module's `notebook.ipynb` file.

### Option 2: VS Code
1. Install the [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) extensions
2. Open any `.ipynb` file
3. Select your kernel (the `venv` you created)

## Recommended VS Code Extensions

- **Python** (ms-python.python) — IntelliSense, debugging, linting
- **Jupyter** (ms-toolsai.jupyter) — notebook support
- **Pylance** (ms-python.vscode-pylance) — fast, feature-rich language support
- **Ruff** (charliermarsh.ruff) — fast Python linter
- **Black Formatter** (ms-python.black-formatter) — automatic code formatting

## Verifying Everything Works

```bash
# With venv activated
python -c "import jupyter, pytest, requests; print('All good!')"
```
