# main.py
from config.settings import settings
from vectorstore.qdrant_store import create_embeddings, get_vectordb
from retriever.retriever import get_retrievers
from db.sql_database import get_database
from prompts.sql_query_generation import get_sql_prompt, SQLResponse
from prompts.chatbot_response import get_response_prompt
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

def main():
    # Crie as embeddings
    embeddings, sparse_embeddings = create_embeddings()

    # Obtenha o banco de dados vetorial
    collection_name = "test_collection"
    qdrant = get_vectordb(embeddings, sparse_embeddings, url=settings.QDRANT_URL, collection_name=collection_name, docs=None)

    # Configure os retrievers
    retriever_ddl, retriever_sql, retriever_documents = get_retrievers(qdrant)

    # Consulta
    query = "Quem é o artilheiro do campeonato?"
    docs_ddl = retriever_ddl.invoke(query)
    docs_sql = retriever_sql.invoke(query)
    docs_documents = retriever_documents.invoke(query)

    # Obtenha o banco de dados SQL
    db = get_database()

    # Inicialize o LLM
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=settings.OPENAI_API_KEY, max_retries=5)

    # Prepare o conteúdo dos documentos
    docs_ddl_content = "\n".join([doc.page_content for doc in docs_ddl])
    docs_sql_content = "\n".join(
        [f"{doc.page_content} (Consulta SQL: {doc.metadata['sql']})" for doc in docs_sql]
    )
    docs_documents_content = "\n".join([doc.page_content for doc in docs_documents])

    # Crie o parser e o prompt para geração de SQL
    parser = JsonOutputParser(pydantic_object=SQLResponse)
    sql_prompt = get_sql_prompt(parser, docs_ddl_content, docs_documents_content, docs_sql_content, query)

    # Crie e execute a cadeia para gerar a SQL
    chain_sql = sql_prompt | llm | parser
    result_sql = chain_sql.invoke({
        "docs_ddl_content": docs_ddl_content,
        "docs_sql_content": docs_sql_content,
        "docs_documents_content": docs_documents_content,
        "query": query
    })

    # Extraia a SQL
    sql = result_sql['sql']
    print(f"SQL Gerada: {sql}")

    # Execute a consulta SQL
    resposta = db.run(sql, include_columns=True)
    print(f"Resposta do Banco de Dados: {resposta}")

    # Prepare o prompt de resposta
    response_prompt = get_response_prompt()
    chain_response = response_prompt | llm | StrOutputParser()

    # Gere a resposta final
    final_result = chain_response.invoke({
        "query": query,
        "sql": sql,
        "resposta": resposta
    })

    print(final_result)

if __name__ == "__main__":
    main()
