from flask import Flask, request, jsonify
from managers.history_manager import HistoryManager
from managers.context_manager import ContextManager
from managers.llm_manager import LLM

context_manager = ContextManager("./store").load_db()
history_manager = HistoryManager()

llm = LLM()

app = Flask(__name__)
app.config['CORS_HEADERS'] = "Content-Type"


@app.route('/question', methods=['POST'])
def question():
    data = request.json
    history_manager.add_user_message(data["question"])
    history = history_manager.get_history()
    matches = context_manager.get_matches(data["question"])
    prompt = "Contexto: " + matches + "\n\nMensaje: " + data["question"]
    response = llm.run(history, prompt)
    return response


if __name__ == '_main_':
    app.run(debug=True)
