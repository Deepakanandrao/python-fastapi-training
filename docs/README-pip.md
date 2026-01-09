# Python Training - Using pip

### Setup Development Environment (Traditional Method)

## 1. Python

Python is a high-level, interpreted programming language known for its simplicity and readability. It's widely used for web development, data science, automation, and AI. Python emphasizes code readability with its clean syntax and indentation-based structure.

## 2. How Python is Executed

Python code is interpreted, not compiled to machine code. The Python interpreter reads your `.py` files line by line and executes them directly. This makes development faster but slightly slower at runtime compared to compiled languages.

## 3. What is a Virtual Environment (venv)?

A virtual environment is an isolated Python environment for your project. It keeps project dependencies separate from system-wide packages. This prevents version conflicts between different projects.

## 4. What is pip?

pip is the default package installer for Python. It comes pre-installed with Python and is used to install packages from PyPI (Python Package Index). While reliable, pip can be slow with dependency resolution and requires separate tools for virtual environment management.

## 5. Creating a Virtual Environment

```bash
# Create a virtual environment with venv
python -m venv .venv

# Create with specific name
python -m venv myenv

# On some systems, use python3
python3 -m venv .venv
```

This creates a `.venv` folder containing an isolated Python environment for your project.

## 6. How to Activate the Virtual Environment

```bash
# Activate (macOS/Linux)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate

# Deactivate
deactivate
```

**Why activate?** Activation ensures your project uses the correct Python version and packages. Without activation, you'll use system Python and global packages, causing potential conflicts.

## 7. Installing Packages with pip

```bash
# Install a single package
pip install requests

# Install multiple packages
pip install requests httpx

# Install with specific version
pip install requests==2.31.0

# Install from requirements.txt
pip install -r requirements.txt

# Upgrade a package
pip install --upgrade requests

# Uninstall a package
pip uninstall requests
```

## 8. Managing Dependencies

```bash
# Create requirements.txt (freeze current packages)
pip freeze > requirements.txt

# Install from requirements.txt
pip install -r requirements.txt

# List installed packages
pip list

# Show package info
pip show requests
```

## 9. What is Ruff?

Ruff is an extremely fast Python linter and formatter written in Rust. A **linter** checks your code for errors, bugs, and style issues, while a **formatter** automatically fixes code style (spacing, line length, etc.). Ruff replaces multiple tools (flake8, black, isort) with one fast tool.

**Why use Ruff?** It catches bugs before runtime, enforces consistent code style across teams, and runs 10-100x faster than traditional Python tools.

```bash
# Install ruff
pip install ruff

# Check code
ruff check .

# Format code
ruff format .
```

## 10. VS Code Extensions for Python Development

**Essential:**

- **Python** (Microsoft) - Python language support
- **Pylance** (Microsoft) - Fast language server, IntelliSense
- **Ruff** (Astral Software) - Linting and formatting

**Recommended:**

- **Error Lens** - Inline error display
- **Better Comments** - Highlighted comments
- **GitLens** - Git integration

## 11. Running Python Code

```bash
# Run a Python file
python main.py

# Run a script
python hello.py

# Run with specific Python version
python3.12 main.py
```

---

## Quick Start with pip

```bash
# Create virtual environment
python -m venv .venv

# Activate environment
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate  # Windows

# Upgrade pip (recommended)
pip install --upgrade pip

# Install dependencies
pip install requests ruff

# Create requirements.txt
pip freeze > requirements.txt

# Run your script
python main.py
```

---

## pip vs UV Comparison

| Feature                   | pip                   | UV                           |
| ------------------------- | --------------------- | ---------------------------- |
| **Speed**                 | Slow (Python-based)   | 10-100x faster (Rust-based)  |
| **Dependency Resolution** | Can fail or be slow   | Fast and reliable            |
| **Virtual Env**           | Needs separate `venv` | Built-in: `uv venv`          |
| **Cache**                 | Basic                 | Smart global cache           |
| **Commands**              | `pip install`         | `uv add` or `uv pip install` |
| **Dependency Tracking**   | Manual (requirements) | Automatic (pyproject.toml)   |

**Recommendation:** Use UV for new projects. It's faster and has better dependency management. Use pip if you're working on legacy projects or have specific compatibility requirements.
