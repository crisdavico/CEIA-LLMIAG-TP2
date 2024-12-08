import os
from groq import Groq

class Agent():
    def __init__(self, person):
        self.person = person

    def search_rag(self, question, vectorstore):
        pinecone_search = vectorstore.similarity_search(question, k=3)
        rag = " ".join([resultado.page_content for resultado in pinecone_search])
        return rag
    
    def run(self, question, chat_history, vectorstore):
        rag = self.search_rag(question, vectorstore)
        # Carga la clave de API de GROQ desde las variables de entorno
        groq_api_key = os.environ.get("GROQ_API_KEY")

        # Crea el cliente de GROQ
        client = Groq(
            api_key=groq_api_key,
        )

        # Agrega el mensaje del usuario al historial de conversación
        chat_history.append({"role": "user", "content": question + rag})

        # Genera la respuesta del chatbot utilizando el modelo LLaMA 3 y el historial de la conversación
        chat_completion = client.chat.completions.create(
            messages=chat_history,
            model="llama3-8b-8192",
        )

        system_prompt = f"""
        Eres un asistente experto que utiliza información específica proporcionada por el usuario para responder preguntas de manera precisa y contextual.

        La pregunta es sobre una persona en particular asi que podes ignorar esa parte y concentrarte en el resto de la información.

        A continuación, se te proporcionará un fragmento de información relevante y una pregunta relacionada con esta información. Debes responder únicamente basándote en los datos proporcionados, sin inventar ni asumir información adicional. Si no encuentras suficiente información en el fragmento proporcionado para responder la pregunta, indica claramente que no puedes responder con los datos disponibles.

        ### Información proporcionada:
        {rag}

        ### La pregunta es sobre:
        {self.person.split('-')}

        ### Pregunta:
        {question}

        ### Respuesta:

        """

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": f"{system_prompt}",
                },
                {
                    "role": "user",
                    "content": f"{chat_history}",
                }
            ],
            model="llama3-8b-8192",
            temperature=0.5,
        )

        response = chat_completion.choices[0].message.content

        # Agrega la respuesta del chatbot al historial de conversación
        chat_history.append({"role": "assistant", "content": response})

        return response
