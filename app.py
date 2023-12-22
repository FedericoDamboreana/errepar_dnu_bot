from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from managers.history_manager import HistoryManager
from managers.context_manager import ContextManager
from managers.llm_manager import LLM

context_manager = ContextManager("./store")
context_manager.load_db()
history_manager = HistoryManager()

llm = LLM()
print("Hola hola me imprimi 1")
app = Flask(__name__)
print("Hola hola me imprimi 2")
cors = CORS(app)
print("Hola hola me imprimi 3")
app.config['CORS_HEADERS'] = "Content-Type"
print("Hola hola me imprimi 4")
@app.route('/question', methods=['POST'])
@cross_origin()
def question():
    data = request.json
    if len(data["historial"]) >= 8:
        return {"message": "Si querés seguir haciendo consultas, suscribite y usá sin límites la herramienta de IA"}
    matches = context_manager.get_matches(data["historial"][-1]["content"])
    prompt = "Contexto: " + matches + "\n\nMensaje: " + data["historial"][-1]["content"]
    response = llm.run(data["historial"], prompt)
    return {"message": response}


if __name__ == '__main__':
    app.run(debug=True)
