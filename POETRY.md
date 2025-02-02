# Poetry to manage dependency
Poetry is a modern dependency management and packaging tool. Here's why it's useful:
1. dependency management
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
2. project managment
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
3. Development vs Production Dependencies
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



When you run ```poetry add requests``` or ```poetry add --dev black```, Poetry will:
- Install the package in your project's virtual environment
- Automatically update your **pyproject.toml** file with the new dependency
- Update the poetry.lock file (which locks exact versions of all dependencies)

Think of ```pyproject.toml``` as:
A recipe book (build instructions)
A shopping list (dependencies)
A toolbox inventory (development tools)
An ID card (project information) All in one file that helps manage your Python project!

# start a project with poetry
```bash
# option 1: 
poetry install
# option 2:
cd pre-existing-project
poetry init

#list all the installed package along with their versions and descriptions
poetry show

# Install dependencies
poetry add pydantic-settings, openai

# Install dependencies for dev
poetry add --group dev pytest black mypy pytest-asyncio
# then you can specify to install as dev
poetry install --with dev

# remove a package
poetry remove openai

# update all dependencies
poetry update

# Or run commands in virtual environment without activation
poetry run python your_script.py

# Update Poetry itself
poetry self update
```

```poetry add``` will
- Install the package in your project's virtual environment
- Automatically update your pyproject.toml file with the new dependency
- Update the poetry.lock file (which locks exact versions of all dependencies)


By default, Poetry creates a virtual environment in {cache-dir}/virtualenvs. You can change the cache-dir value by editing the Poetry configuration. Additionally, you can use the virtualenvs.in-project configuration variable to create virtual environments within your project directory.

## Using your virtual environment
### Using poetry run
To run your script simply use ```poetry run python your_script.py```

### Activating the virtual environment
```bash
# show current activate virtual env
poetry env info
# if you only wants to know the path to the virtual env
poetry env info --path

#option1:
poetry env activate
#option2: you can set Python Interpretor in VScode to the virtual env
#option3: Activating venv manually
source .venv/bin/activate  # or activate.bat on Windows
deactivate


# list all the virtual env associate with this project
poetry env list
poetry env list --full-path


# delete virtual env
poetry env remove python3.7
poetry env remove --all


#activate a virtual env
poetry env activate


# Show the list of config
poetry config --list
# Configure Poetry to create virtualenv in project directory
poetry config virtualenvs.in-project true
# Create a new virtualenv with the new configuration
poetry env remove --all  # Remove existing virtual env if any
poetry env remove $(poetry env info --path) # Remove specific exisiting virtual env 
poetry install          # Create new virtualenv and install dependencies

# Clear Poetry's cache
poetry cache clear . --all

```
