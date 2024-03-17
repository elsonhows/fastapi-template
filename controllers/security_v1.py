from fastapi import APIRouter, Depends, Request, Security
from fastapi.security import APIKeyHeader, HTTPBearer

from utils.contextvars import request as ctx_request

# refer https://stackoverflow.com/questions/74085996/how-to-send-authorization-header-through-swagger-ui-using-fastapi/74088523#74088523
security = HTTPBearer()
api_key_header = APIKeyHeader(name="Authorization")
PROTECTED = [Depends(security)]

router = APIRouter()


@router.get("/http_bearer")
def get_http_bearer(authorization: str = Depends(security)):
    return authorization.credentials


@router.get("/api_key_header_auth")
def get_api_key_header_auth(api_key: str = Security(api_key_header)):
    return api_key


@router.get("/use_request_direct", dependencies=PROTECTED)
def use_request_direct(request: Request):
    # refer https://fastapi.tiangolo.com/advanced/using-request-directly/
    return request.state.jwt_token


@router.get("/use_ctx_request", dependencies=PROTECTED)
def use_ctx_request():
    # refer https://github.com/tiangolo/fastapi/discussions/8628
    # use case: in order to use `request` var everywhere in app without passing var thru param
    return ctx_request.value.state.jwt_token
