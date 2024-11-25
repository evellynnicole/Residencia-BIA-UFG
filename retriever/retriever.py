from qdrant_client.http.models import Filter, FieldCondition, MatchValue

def create_filter(retorno):
    qdrant_filter = Filter(
        must=[
            FieldCondition(
                key="metadata.type",
                match=MatchValue(value=retorno)
            )
        ]
    )
    return qdrant_filter

def get_retrievers(qdrant):
    retriever_ddl = qdrant.as_retriever(search_kwargs={'k': 4, 'filter': create_filter("schema")})
    retriever_sql = qdrant.as_retriever(search_kwargs={'k': 7, 'filter': create_filter("sql")})
    retriever_documents = qdrant.as_retriever(search_kwargs={'k': 10, 'filter': create_filter("documentation")})
    return retriever_ddl, retriever_sql, retriever_documents