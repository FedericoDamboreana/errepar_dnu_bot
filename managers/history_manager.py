class HistoryManager:
    def __init__(self):
        self.chat_history = []
    
    def add_ai_message(self, message):
        self.chat_history.append({"role": "assistant", "content": message})
    
    def add_user_message(self, message):
        self.chat_history.append({"role": "user", "content": message})
    
    def get_history(self):
        return self.chat_history
    
    def clear_history(self):
        self.chat_history = []
