from typing import Union

from container import Container
from core.auth.schema.auth import AuthDetails, AuthSchemaSignIn
from core.auth.service.auth import IAuthService
from core.utils.exceptions import AuthServiceError
from core.utils.types import Token
from dependency_injector.wiring import Provide, inject
from fastapi import Depends, APIRouter, Response, status
from fastapi.responses import PlainTextResponse

from internal.src.api.router.utils.response import HTTPError

router = APIRouter(
    prefix="/auth/jwt",
    tags=["Auth"]
)

dep_auth = Depends(Provide[Container.auth_service])


@router.post("/auth/jwt/authorization")
@inject
def authorization(
        auth_details: Union[Token, AuthSchemaSignIn],
        response: Response,
        auth_service: IAuthService = dep_auth
) -> Union[AuthDetails, HTTPError]:
    if isinstance(auth_details, Token):
        auth_service.logout(Token(value=auth_details))
        return AuthDetails(access_token=Token(""), refresh_token=Token(""))
    elif isinstance(auth_details, AuthSchemaSignIn):
        try:
            res = auth_service.signin(auth_details)
        except AuthServiceError as e:
            response.status_code = status.HTTP_401_UNAUTHORIZED
            return HTTPError(f"{e.detail}")

    return res


@router.post("/logout")
@inject
def logout(
        token: str,
        auth_service: IAuthService = dep_auth
) -> PlainTextResponse:
    auth_service.logout(Token(value=token))
    return PlainTextResponse('session deleted')
