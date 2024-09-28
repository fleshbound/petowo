from abc import ABC, abstractmethod


class IAnimalHandler(ABC):
    @abstractmethod
    def get_animals_by_user_id(self, user_id: int) -> None:
        raise NotImplemented

    @abstractmethod
    def delete_animal(self, user_id: int) -> None:
        raise NotImplemented

    @abstractmethod
    def create_animal(self, user_id: int) -> None:
        raise NotImplemented
