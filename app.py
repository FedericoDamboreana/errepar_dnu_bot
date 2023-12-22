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
    if len(data["historial"]) >= 8:
        return {"message": "Si querés seguir haciendo consultas, suscribite y usá sin límites la herramienta de IA"}
    matches = context_manager.get_matches(data["historial"][-1]["content"])
    prompt = "Contexto: " + matches + "\n\nMensaje: " + data["historial"][-1]["content"]
    response = llm.run(data["historial"], prompt)
    return {"message": response}


if __name__ == '_main_':
    app.run(debug=True)
