from managers.history_manager import HistoryManager
from managers.context_manager import ContextManager
from managers.llm_manager import LLM

class Chain:
    def __init__(self, history: HistoryManager, context: ContextManager, llm: LLM) -> None:
        self.history_manager = history
        self.context_manager = context
        self.llm = llm

    def get_prompt(self, context, message):
        prompt = "Contexto: " + context + "\n\nMensaje: " + message
        return prompt
    
    def run(self, message):
        self.history_manager.add_user_message(message)
        history = self.history_manager.get_history()
        matches = self.context_manager.get_matches(message)
        prompt = self.get_prompt(matches, message)

        response = self.llm.run(history, prompt)
        print(">>> final response: ", response)
        # self.history_manager.add_ai_message(response)

        return response


