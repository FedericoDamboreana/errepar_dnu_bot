import openai

class LLM:
    def __init__(self) -> None:
        openai.api_key = "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"
        self.model = "gpt-3.5-turbo"
        self.primer = """
Eres un chatbot diseñado para responder preguntas sobre el decreto que hizo el presidente electo de Argentina, Javier Milei.
Eres parte de una empresa llamada Errepar. Errepar es una empresa especializada en novedades, contenidos, análisis e información de materia legal.
Si el usuario requiere reglamentación o asesoramiento por un profesional, recomiéndale visitar https://www.errepar.com/
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