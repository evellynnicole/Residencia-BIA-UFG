from langchain_qdrant import QdrantVectorStore, RetrievalMode
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_qdrant import FastEmbedSparse
from config.settings import settings

def create_embeddings():
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large", openai_api_key=settings.OPENAI_API_KEY)
    sparse_embeddings = FastEmbedSparse(model_name="prithvida/Splade_PP_en_v1")
    return embeddings, sparse_embeddings

def get_vectordb(embeddings, sparse_embeddings, url, collection_name: str, docs):
    try:
        qdrant = QdrantVectorStore.from_existing_collection(
            collection_name=collection_name,
            embedding=embeddings, 
            sparse_embedding=sparse_embeddings,
            url=url,
            prefer_grpc=True,
            api_key=settings.QDRANT_API_KEY,
            retrieval_mode=RetrievalMode.HYBRID,
            content_payload_key='page_content',
            metadata_payload_key='metadata'
        )
        print(f"Usando a coleção existente: {collection_name}")

        if docs:
            print(f"Adicionando documentos à coleção existente: {collection_name}")
            qdrant.add_documents(docs)


    except Exception as e:
        if docs is None:
            raise ValueError(f"Coleção '{collection_name}' não encontrada e 'docs' não foi fornecido para criá-la.")
        print(f"Coleção '{collection_name}' não encontrada. Criando uma nova...")
        qdrant = QdrantVectorStore.from_documents(
            docs,
            embedding=embeddings,  # Correção aqui
            sparse_embedding=sparse_embeddings,
            url=url,
            prefer_grpc=True,
            api_key=settings.QDRANT_API_KEY,
            collection_name=collection_name,
            retrieval_mode=RetrievalMode.HYBRID,
            content_payload_key='page_content',
            metadata_payload_key='metadata'
        )
    return qdrant
