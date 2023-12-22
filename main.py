from managers.history_manager import HistoryManager
from managers.context_manager import ContextManager
from managers.llm_manager import LLM
from chain import Chain

class Main:
    def __init__(self):
        self.primer = """
Eres un chatbot diseñado para responder preguntas sobre el decreto que hizo el presidente electo de Argentina, Javier Milei.
En cada pregunta, se te va a enviar también un contexto compuesto por extractos del decreto. Adjuntá los datos como numero de articulo siempre que puedas.
Usa el contexto para responder las preguntas del usuario pero no referencies el contexto en si mismo.
"""
        self.model = "gpt-3.5-turbo"
        self.api_key = "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"


        self.history_manager = HistoryManager()
        self.context_manager = ContextManager("./store")
        self.context_manager.load_db()

        
        self.llm = LLM(self.model, self.primer, self.api_key)
        self.chain = Chain(self.history_manager, self.context_manager, self.llm)


    def run(self):
        self.chain.run("como funciona la aduana ahora?")
        pass

main = Main()
main.run()
