# Python Training

### Setup Development Environment

## 1. Python

Python is a high-level, interpreted programming language known for its simplicity and readability. It's widely used for web development, data science, automation, and AI. Python emphasizes code readability with its clean syntax and indentation-based structure.

## 2. How Python is Executed

Python code is interpreted, not compiled to machine code. The Python interpreter reads your `.py` files line by line and executes them directly. This makes development faster but slightly slower at runtime compared to compiled languages.

## 3. What is a Virtual Environment (venv)?

A virtual environment is an isolated Python environment for your project. It keeps project dependencies separate from system-wide packages. This prevents version conflicts between different projects.

## 4. What is UV?

UV is a modern, extremely fast Python package manager written in Rust. It replaces pip and virtualenv with a single, faster tool. UV can install packages 10-100x faster than pip.

## 5. Creating a Virtual Environment

Execute any one of the following

```bash
# Create a virtual environment with UV
uv venv

# Create with specific Python version
uv venv --python 3.12

# Create with custom name
uv venv myenv
```

This creates a `.venv` folder containing an isolated Python environment for your project.

## 6. How to Activate the Virtual Environment

```bash
# Activate
source .venv/bin/activate

# Deactivate
deactivate
```

**Why activate?** Activation ensures your project uses the correct Python version and packages. Without activation, you'll use system Python and global packages, causing potential conflicts.

## 7. Installing Packages with UV

**Modern way (recommended):**

```bash
# Add a single package
uv add requests

# Add multiple packages
uv add requests httpx

# Add with specific version
uv add requests==2.31.0

# Add as dev dependency
uv add --dev ruff pytest
```

**Note:** For traditional pip workflow, see [README-pip.md](README-pip.md)

## 8. What is Ruff?

Ruff is an extremely fast Python linter and formatter written in Rust. A **linter** checks your code for errors, bugs, and style issues, while a **formatter** automatically fixes code style (spacing, line length, etc.). Ruff replaces multiple tools (flake8, black, isort) with one fast tool.

**Why use Ruff?** It catches bugs before runtime, enforces consistent code style across teams, and runs 10-100x faster than traditional Python tools.

```bash
# Install ruff
uv pip install ruff

# Check code
ruff check .

# Format code
ruff format .
```

## 9. VS Code Extensions for Python Development

**Essential:**

- **Python** (Microsoft) - Python language support
- **Pylance** (Microsoft) - Fast language server, IntelliSense
- **Ruff** (Astral Software) - Linting and formatting

**Recommended:**

- **Error Lens** - Inline error display
- **Better Comments** - Highlighted comments
- **GitLens** - Git integration

## 10. Running Python Code with UV

```bash
# Run a Python file directly
uv run python main.py

# Run a Python script
uv run python hello.py

# Run with specific Python version
uv run --python 3.12 python main.py

# Run a script defined in pyproject.toml
uv run <script-name>
```

**Note:** `uv run` automatically manages the virtual environment for you.

---

## Quick Start

```bash
# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment
uv venv

# Activate environment
source .venv/bin/activate

# Install a package (example)
uv add requests

# Run your Python script
uv run python main.py
```
