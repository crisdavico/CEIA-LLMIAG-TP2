import os
from cv_processor import procesar_cv
from embeddings import crear_embeddings
from agent import Agent
import streamlit as st

def main():
    st.title("Chatbot sobre mi CV")
    st.write("Hazme una pregunta sobre las experiencia y habilidades de mis colaboradores.")

    # Inicializa el historial de conversación en el estado de la sesión
    if "conversation_history" not in st.session_state:
        st.session_state.conversation_history = []

    # Procesar CV y crear embeddings (solo la primera vez)
    if 'vectorstore_dict' not in st.session_state:
        st.session_state.vectorstore_dict = {}
        with st.spinner('Procesando los CV y configurando el chatbot...'):
            folder_path = "CEIA-LLMIAG-TP2\\files"
            # Listar todos los archivos en la carpeta
            for file_name in os.listdir(folder_path):
                name = file_name[:-4]
                path = os.path.join(folder_path, file_name)
                if os.path.isfile(path):  # Verificar que sea un archivo
                    docs = procesar_cv(path)
                    qa_chain = crear_embeddings(docs, name)
                    st.session_state.vectorstore_dict[name] = qa_chain
            st.success('Chatbot configurado exitosamente.')

    pregunta = st.text_input("Escribe tu pregunta aquí indicando la persona sobre la cual quiere conocer información:")
    if st.button("Enviar") and pregunta:
        with st.spinner('Generando respuesta...'):
            jperez_words = ['joaquin', 'joaco', 'perez', 'pérez']
            sgomez_words = ['sergio', 'gomez', 'gómez']

            if any(word in pregunta.lower() for word in jperez_words):
                vectorstore = st.session_state.vectorstore_dict['cv-joaquin-perez']
                cibanez = Agent('cv-joaquin-perez')
                response = cibanez.run(pregunta,st.session_state.conversation_history, vectorstore)
            elif any(word in pregunta.lower() for word in sgomez_words):
                vectorstore = st.session_state.vectorstore_dict['cv-sergio-gomez']
                cibanez = Agent('cv-sergio-gomez')
                response = cibanez.run(pregunta,st.session_state.conversation_history, vectorstore)
            else:
                vectorstore = st.session_state.vectorstore_dict['cv-claudia-ibanez']
                cibanez = Agent('cv-claudia-ibanez')
                response = cibanez.run(pregunta,st.session_state.conversation_history, vectorstore)
            
            st.write("**Respuesta:**")
            st.write(response)

            







    

if __name__ == "__main__":
    main()