import datetime
from abc import ABC, abstractmethod
from typing import Optional

from pydantic import PositiveInt

from tech.utils.lang.langmodel import LanguageModel


class IInputHandler(ABC):
    lang_model: LanguageModel

    @staticmethod
    @abstractmethod
    def ask_question(query: str) -> str:
        raise NotImplemented

    @abstractmethod
    def wait_input(self, question: str, out_question: str) -> Optional[str]:
        raise NotImplemented

    @abstractmethod
    def wait_positive_int(self, question: str, out_question: str) -> Optional[PositiveInt]:
        raise NotImplemented

    @abstractmethod
    def date_input(self, out_question: str) -> Optional[datetime.datetime]:
        raise NotImplemented
