# fastapi-template

## Setup

### Python

https://www.python.org/downloads/

### Virtual Environment

```bash
# install 'virtualenv' lib to your global env
pip install virtualenv

# create new virtual environment to your project, this will create a new directory with your desired name
python -m venv {virtual-environment-name}
# for example
python -m venv fastapi-template-env
```

## Installation

```bash
# make sure you are already in your virtual environment
# for linux
source fastapi-template-env/bin/activate
#  for window
./fastapi-template-env/Scripts/activate

# install library based in requirements.txt in your virtual environment
pip install -r requirement.txt
```

## Run

```bash
# make sure you are already in your virtual environment
# for linux
source fastapi-template-env/bin/activate
#  for window
./fastapi-template-env/Scripts/activate

# start one instance of server, any changes and save will auto restart the server
$ uvicorn main:app --reload

# start multiple instance of the server
$ uvicorn main:app --workers 5

# start server with specific port
$ uvicorn main:app --port 8000
```
