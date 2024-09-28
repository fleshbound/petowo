from abc import abstractmethod, ABC


class IShowHandler(ABC):
    @abstractmethod
    def score_animal(self, user_id: int) -> None:
        raise NotImplemented

    @abstractmethod
    def create_show(self) -> None:
        raise NotImplemented

    @abstractmethod
    def start_show(self) -> None:
        raise NotImplemented

    @abstractmethod
    def stop_show(self) -> None:
        raise NotImplemented

    @abstractmethod
    def register_animal(self, user_id: int) -> None:
        raise NotImplemented

    @abstractmethod
    def unregister_animal(self, user_id: int) -> None:
        raise NotImplemented

    @abstractmethod
    def register_user(self) -> None:
        raise NotImplemented

    @abstractmethod
    def unregister_user(self) -> None:
        raise NotImplemented

    @abstractmethod
    def get_shows_all(self) -> None:
        raise NotImplemented

    @abstractmethod
    def get_show_result(self) -> None:
        raise NotImplemented

    @abstractmethod
    def get_animals_by_show(self) -> None:
        raise NotImplemented
