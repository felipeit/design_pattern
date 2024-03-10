
from .abstract_handler import AbstractHandler


class ConcreteHandlerB(AbstractHandler):
    def handler_request(self, request):
        if request == "B":
            print("Handler B tratou a solicitação.")
        else:
            print("Handler B não tratou a solicitação.")
