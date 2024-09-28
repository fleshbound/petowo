from abc import abstractmethod, ABC
from typing import Optional

from core.utils.types import Token
from tech.utils.types import UserConsoleInfo


class IAuthHandler(ABC):
    @abstractmethod
    def signin(self) -> Optional[UserConsoleInfo]:
        raise NotImplemented

    @abstractmethod
    def verify_token(self, token: Token) -> bool:
        raise NotImplemented

    @abstractmethod
    def logout(self, token: Token) -> None:
        raise NotImplemented
