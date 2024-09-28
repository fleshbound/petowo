from dataclasses import dataclass


@dataclass
class HTTPError:
    detail: str
