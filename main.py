from time import time

from fastapi import FastAPI, Request
from loguru import logger

from controllers import security_v1, user_v1

tags_metadata = [
    {"name": "users", "description": "Users endpoints"},
    {"name": "system", "description": "System endpoints"},
    {"name": "security", "description": "Security endpoints"},
]
exclude_logging_route = ["/docs", "/openapi.json", "/healthCheck"]

app_description = """
Just showing markdown is supported in description. 🚀

### Header

This is **bold**

This is *Italic*

This is list:
- one
- two
- three
"""

app = FastAPI(
    title="FastAPI-Template",
    summary="Attempt to create decent FastAPI template for personal reference.",
    description=app_description,
    version="0.0.1",
    openapi_tags=tags_metadata,
)
app.include_router(user_v1.router, prefix="/v1", tags=["users"])
app.include_router(security_v1.router, prefix="/v1/security", tags=["security"])


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    # docs for "request" refer to https://www.starlette.io/requests/
    start_time = time()
    response = await call_next(request)
    process_time = time() - start_time
    if request.url.path not in exclude_logging_route:
        logger.info(
            f"route '{request.method} {request.url.path}' took {process_time} sec"
        )
    # response.headers["X-Process-Time"] = str(process_time)
    return response


@app.middleware("http")
async def process_jwt_token(request: Request, call_next):
    from utils.contextvars import request as ctx_request

    auth_header = request.headers.get("Authorization")
    if auth_header:
        jwt_token = auth_header.replace("Bearer ", "")
        request.state.jwt_token = jwt_token
    # put reuqest into context var so that value can be accessible globally within session
    request_token = ctx_request.set(request)

    response = await call_next(request)

    ctx_request.reset(request_token)

    return response


@app.get(
    path="/health",
    summary="Health check endpoint",
    tags=["system"],
)
async def healthcheck():
    return {"message": "ok"}
