from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from managers.history_manager import HistoryManager
from managers.context_manager import ContextManager
from managers.llm_manager import LLM

context_manager = ContextManager("./store")
print("Se preparo el manager de contexto")
context_manager.load_db()
print("Se cargo la DB de Chroma")
history_manager = HistoryManager()
print("Se preparo el manager de historial")

llm = LLM()
print("Se preparo la LLM")
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = "Content-Type"
print("Se inicializo flask y cors")
print("API lista para uso")


@app.route('/question', methods=['POST'])
@cross_origin()
def question():
    data = request.json
    matches = context_manager.get_matches(data["historial"][-1]["content"])
    prompt = "Contexto: " + matches + "\n\nMensaje: " + data["historial"][-1]["content"]
    response = llm.run(data["historial"], prompt)
    return {"message": response}


if __name__ == '__main__':
    app.run(debug=True)
