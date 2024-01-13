from time import time
from loguru import logger
from fastapi import FastAPI, Request

from controllers import users_v1


tags_metadata = [
    {"name": "users", "description": "Users endpoints"},
    {"name": "system", "description": "System endpoints"},
]
exclude_logging_route = ["/docs", "/openapi.json", "/healthCheck"]

app = FastAPI(openapi_tags=tags_metadata)
app.include_router(users_v1.router, prefix="/v1", tags=["users"])


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


@app.get(
    path="/health",
    summary="Health check endpoint",
    tags=["system"],
)
async def healthcheck():
    return {"message": "ok"}
