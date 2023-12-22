import openai

class LLM:
    def __init__(self) -> None:
        openai.api_key = "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"
        self.model = "gpt-3.5-turbo"
        self.primer = """
Eres un chatbot diseñado para responder preguntas sobre el decreto que hizo el presidente electo de Argentina, Javier Milei.
En cada pregunta, se te va a enviar también un contexto compuesto por extractos del decreto. Adjuntá los datos como numero de articulo siempre que puedas.
Usa el contexto para responder las preguntas del usuario pero no referencies el contexto en si mismo.
"""
    
    def run(self, history, prompt):
        messages = []
        messages.append({"role": "system", "content": self.primer})
        messages = messages + history
        messages.append({"role": "user", "content": prompt})

        res = openai.ChatCompletion.create(
            model=self.model,
            messages=messages
        )

        return res["choices"][0]["message"]["content"]