# fastapi-template

## Installation

```bash
pip install -r requirement.txt
```

## Run

```bash
# start one instance of server, any changes and save will auto restart the server
$ uvicorn main:app --reload

# start multiple instance of the server
$ uvicorn main:app --workers 5

# start server with specific port
$ uvicorn main:app --port 8000
```
