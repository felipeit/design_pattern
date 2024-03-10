from typing import Protocol

class AbstractHandler(Protocol):
    def handler_request(self, request) -> None:...