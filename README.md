# US Procurement Scraper

A Python-based scraper for collecting and analyzing US government procurement data.

## Features
- government websites data scraping
- AI-powered analysis of procurement data
- Structured data output

## Prerequisites
- Python 3.8+
- Poetry (for dependency management)
- Required API keys (OpenAI, etc.)

### Poetry to manage dependency
Poetry is a modern dependency management and packaging tool. Here's why it's useful:
1. Dependency Management
```bash
# Without Poetry (requirements.txt)
requests==2.31.0
playwright==1.41.0
openai==1.12.0

# With Poetry (pyproject.toml)
[tool.poetry.dependencies]
python = "^3.9"
requests = "^2.31.0"
playwright = "^1.41.0"
openai = "^1.12.0"

[tool.poetry.group.dev.dependencies]
pytest = "^8.0.0"
black = "^24.1.1"
```
2. Lock File for Reproducibility
3. Project Management
```bash
# Without Poetry
pip install -r requirements.txt
python setup.py build
python setup.py install

# With Poetry
poetry install  # Installs all dependencies
poetry build    # Builds your package
poetry publish  # Publishes to PyPI
```
4. Development vs Production Dependencies
```bash
[tool.poetry.dependencies]
# Production dependencies
requests = "^2.31.0"
playwright = "^1.41.0"

[tool.poetry.group.dev.dependencies]
# Development-only dependencies
pytest = "^8.0.0"
black = "^24.1.1"
mypy = "^1.8.0"
```

When you run poetry add requests or poetry add --dev black, Poetry will:
- Install the package in your project's virtual environment
- Automatically update your pyproject.toml file with the new dependency
- Update the poetry.lock file (which locks exact versions of all dependencies)

Think of pyproject.toml as:
- A recipe book (build instructions)
- A shopping list (dependencies)
- A toolbox inventory (development tools)
- An ID card (project information)
All in one file that helps manage your Python project!


## Setup the Python Development Environment

### 1. Install Poetry
```bash
# Official method of install poetry - Linux, macOS, Windows (WSL)
curl -sSL https://install.python-poetry.org | python3 -
# or
pip install poetry

# Verify if poetry is installed
# Poetry should be installed globally (once per computer), not per project!
poetry --version
```

### 2. Create Project (choose one method)
```bash
# Method 1: Create a new project from scratch
poetry new us-procurement-scraper
cd us-procurement-scraper

# OR Method 2: Start in existing directory
mkdir us-procurement-scraper
cd us-procurement-scraper
poetry init  # Interactive setup of pyproject.toml
```

### 3. Setup Dependencies and Run
```bash
# Install all dependencies
poetry install

# Install Playwright browsers
poetry run playwright install

# Run the scraper
poetry run python -m src.main
```



## Playwright
Playwright is a tool to automate web browsers. It's like a remote control for your browser.
```bash
# First, add the Playwright package
poetry add playwright

# Then, install the browser binaries
poetry run playwright install
```
This two-step process is necessary because:
The Python package is just the code to control browsers
The actual browsers are separate executables that need to be installed separately
Browser binaries are large files that aren't distributed through PyPI

```poetry run``` is needed because it runs the command inside your project's virtual environment. Without it, your system would try to run the playwright command globally, which likely won't work because:
- Playwright is installed in your project's virtual environment, not globally
- The system won't know where to find the playwright command

Think of it like this:
Your project is in a special isolated environment (virtual environment)
poetry run is like saying "go into that environment and then run this command"
It's similar to activating a virtual environment:
```bash
# These are equivalent:
# Option 1: Using poetry run
poetry run playwright install

# Option 2: Activating venv manually
source .venv/bin/activate  # or activate.bat on Windows
playwright install
deactivate
```

# Testing
Run tests using pytest:
```
# Run all tests
pytest

# Run specific test file
pytest tests/test_scrapers.py

# Run with verbose output
pytest -v

# Run and show print statements
pytest -s
```

# Other Notes about python:
```__init__.py``` files serve several important purposes in Python:
1. Make the directory a package: Without it, Python won't recognize the directory as a package
2. Initialize the package: It's used to initialize the package when it's imported
3. Define the package's API: It's used to define the package's API when it's imported
Can be empty - just having the file is enough to make the directory a package


# list of dependencies
## Pydantic
Pydantic is a data validation and settings management library for Python. It's like a Swiss Army knife for data validation and configuration.
```poetry add pydantic-settings```
Poetry will automatically install pydantic as well because it's a dependency of pydantic-settings

## SQLAlchemy
SQLAlchemy is a SQL toolkit and Object-Relational Mapping (ORM) library for Python. It's like a remote control for your database.


## Loguru
Loguru is a logging library for Python. It's like a remote control for your logs.


