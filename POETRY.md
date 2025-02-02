```bash
#install poetry



# start a project with poetry
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

# Show the list of config
poetry config --list

# Or run commands in virtual environment without activation
poetry run python your_script.py

# Clear Poetry's cache
poetry cache clear . --all

# Update Poetry itself
poetry self update

# check the virtual environment path
poetry env info --path

# activate virtual environment - discontinued
poetry shell

# deactivate virtual environment - discontinued
deactivate

# Show virtual environment info
poetry env info

# List all environments
poetry env list

# Configure Poetry to create virtualenv in project directory
poetry config virtualenvs.in-project true
# Create a new virtualenv with the new configuration
sudo poetry env remove --all  # Remove existing virtual env if any
sudo poetry env remove $(poetry env info --path) # Remove specific exisiting virtual env 
poetry install          # Create new virtualenv and install dependencies

# Remove environment
poetry env remove python3.9
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
sudo poetry env remove --all  # Remove existing virtual env if any
sudo poetry env remove $(poetry env info --path) # Remove specific exisiting virtual env 
poetry install          # Create new virtualenv and install dependencies

```
