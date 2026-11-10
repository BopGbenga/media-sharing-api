import uuid
from typing import Optional
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin, models
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)
from fastapi_users.db import SQLAlchemyUserDatabase
from src.db import User, get_user_db

SECRET = "12344556"


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_audience = SECRET
    verification_token_audience = SECRET

    async def on_after_register(self, user, request: Optional[Request] = None):
        print(f"User{user.id} has registered")

    async def on_after_forgot_password(
        self, user, token: str, request: Optional[Request] = None
    ):
        print(f"User{user.id}has forgot their password. Reset token:{token}")

    async def on_after_request_verify(
        self, user, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user{user.id}. Verification token: {token}")


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)


bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy():
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="JWT", transport=bearer_transport, get_strategy=get_jwt_strategy
)

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager, auth_backends=[auth_backend]
)

current_active_user = fastapi_users.current_user(active=True)
