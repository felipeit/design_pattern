from .abstract_handler import AbstractHandler


class ConcreteHandlerA(AbstractHandler):
    def handler_request(self, request):
        if request == "A":
            print("Handler A tratou a solicitação.")
        else:
            print("Handler A não tratou a solicitação.")