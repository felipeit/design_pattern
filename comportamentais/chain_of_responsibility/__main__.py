from handlers import ConcreteHandlerA, ConcreteHandlerB, ConcreteHandlerC, AbstractHandler

class Handler:
    def execute(self, handler: AbstractHandler, text: str):
        handler.handler_request(text)
        
pipeline = {
    "step_1": ConcreteHandlerC(),
    "step_2": ConcreteHandlerB(),
    "step_3":  ConcreteHandlerA()
}

for k, v in pipeline.items():
    print(f"starting: {k} with {v}")
    Handler().execute(v, "A")