from time import time

from fastapi import Depends, FastAPI, Request, Security
from fastapi.security import APIKeyHeader, HTTPBearer
from loguru import logger

from controllers import user_v1

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


# refer https://stackoverflow.com/questions/74085996/how-to-send-authorization-header-through-swagger-ui-using-fastapi/74088523#74088523
security = HTTPBearer()
api_key_header = APIKeyHeader(name="Authorization")


@app.get("/http_bearer", tags=["security"])
def get_http_bearer(temp: str, authorization: str = Depends(security)):
    return authorization.credentials


@app.get("/api_key_header_auth", tags=["security"])
def get_api_key_header_auth(api_key: str = Security(api_key_header)):
    return api_key


@app.get(
    path="/health",
    summary="Health check endpoint",
    tags=["system"],
)
async def healthcheck():
    return {"message": "ok"}
