# Python Training Project

Use this repo if you want to quickly refresh python and stack.

## Documentation Index

- [Basic Setup Guide with (UV)](docs/README.md)
- [Python Basics Brush-up](docs/README-python-basics.md)
- [Git Quick Help Guide](docs/git-help.md)
- [Traditional Pip Workflow](docs/README-pip.md) - Optional

## Project Structure

```text
.
├── docs/                # Detailed guides and documentation
│   ├── git-help.md      # Git terminology and commands
│   ├── README-pip.md    # Traditional pip workflow
│   ├── README-python-basics.md # Python syntax refresher
│   └── README.md        # Basic setup guide with UV
├── .venv/               # Virtual environment (managed by UV)
├── main.py              # Main application entry point
├── pyproject.toml       # Dependencies and project metadata
├── uv.lock              # UV lockfile
└── README.md            # Project index (this file)
```

## Running the Project

### Running Linting and Formatting (Ruff)

```bash
# Check for linting errors
uv run ruff check .

# Automatically fix linting errors
uv run ruff check . --fix

# Format the code
uv run ruff format .
```

### Running the Application

```bash
# Run the main script
uv run python main.py
```

---

_Happy Learning!_
