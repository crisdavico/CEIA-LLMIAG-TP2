from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document
import os
import time
from dotenv import load_dotenv

def crear_embeddings(docs, index_name):
    # Cargar variables de entorno
    load_dotenv()
    pinecone_api_key = os.getenv("PINECONE_API_KEY")

    pc = Pinecone(api_key=pinecone_api_key)
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    # text_embeddings = [embedding_model.embed_query(text) for text in texts]

    namespace = "default"

    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name,
            dimension=384,
            metric="cosine", # Replace with your model metric
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            ) 
        )
    
    vectorstore = PineconeVectorStore.from_documents(
        documents=docs,
        index_name=index_name,
        embedding=embedding_model, 
        namespace=namespace
    )
    print("upserted values to {} index".format(index_name))

    time.sleep(1)

    return vectorstore

