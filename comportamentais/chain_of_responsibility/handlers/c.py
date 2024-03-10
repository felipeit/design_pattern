from typing import Any
from .abstract_handler import AbstractHandler


class ConcreteHandlerC(AbstractHandler):
    def handler_request(self, request):
        if request == "C":
            print("Handler C tratou a solicitação.")
        else:
             print("Handler C não tratou a solicitação.")