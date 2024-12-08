from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

def procesar_cv(ruta_cv_pdf):
    file_loader = PyPDFLoader(ruta_cv_pdf)
    documents = file_loader.load()
    
    # Dividir el texto en fragmentos más pequeños
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=150
    )
    docs = text_splitter.split_documents(documents)

    return docs

# a = procesar_cv('G:\Proyectos Python\CEIA-LLMIAG-TP1\cv_davico.pdf')
# print(a)


