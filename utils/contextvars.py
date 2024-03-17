from contextvars import ContextVar, Token
from typing import Generic, TypeVar

from fastapi import Request

T = TypeVar("T")


class ContextWrapper(Generic[T]):
    def __init__(self, value: ContextVar[T]):
        self.__value: ContextVar = value

    def set(self, value: T):
        return self.__value.set(value)

    def reset(self, token: Token):
        self.__value.reset(token)
        return

    def __module__(self) -> T:
        return self.__value.get()

    @property
    def value(self) -> T:
        return self.__value.get()


request: ContextWrapper[Request] = ContextWrapper(
    value=ContextVar("request", default=None)
)
