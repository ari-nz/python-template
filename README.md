# {{Title}} 


This readme contains some setup instructions for getting this thing running, as well as other helpful bits of code


## Project Setup

### One time setup
```sh
# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
# On macOS and Linux:
source .venv/bin/activate
# On Windows:
source .venv\\Scripts\\activate

# Install pip-tools for managing dependencies
pip install pip-tools


# Copy the env file for local development
cp .env.example .env

```

### Utilise pip tools for light weight package manager.

When you want to add new packages, or install the required ones, do the following

```sh

# Compile project dependencies
pip-compile requirements.in
pip-compile requirements-dev.in

# Sync project dependencies
pip-sync requirements.txt requirements-dev.txt

# Further syncing should only need this last command

```

Ensure you then have the pre-commit hooks installed for this process - this too is a (mostly) one time process

Ensure

```sh
pre-commit install
pre-commit run --all-files
```


## Building the project

This is the dockerfile used by prod
``` sh
docker build . -t {{tag_name}} -f Dockerfile
docker run {{tag_name}}
```

If you don't want to do that, you can run and develop locally.


## Running parts of the process
