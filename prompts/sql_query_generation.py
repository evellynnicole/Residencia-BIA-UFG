from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field

class SQLResponse(BaseModel):
    sql: str = Field(description="Consulta SQL que responde à pergunta do usuário")

def get_sql_prompt(parser, docs_ddl_content, docs_documents_content, docs_sql_content, query):
    prompt_template_text = """
    Você é um modelo responsável por gerar queries SQL sobre um banco de dados do Campeonato Brasileiro de Futebol Série A.
    Você receberá uma pergunta e precisa responder no formato JSON contendo a chave "sql" com o comando SQL que responde à pergunta.
    Se a pergunta não puder ser respondida, retorne um JSON vazio.
    Quando envolver times, certifique-se de gerar as queries tanto para o time mandante quanto para o time visitante, já que a ordem pode variar.
    Qauando for usar ORDER BY, nunca utilize LIMIT 1, já que pode limitar a query e não trazer todos os resultados para ser analisado na resposta. Então, sempre use LIMIT 10, mesmo se a query for para trazer apenas um resultado.

    {format_instructions}

    1. Dados DDL (Definição de Esquema):
    {docs_ddl_content}

    2. Documentação de Referência:
    {docs_documents_content}

    3. SQLs de exemplo:
    {docs_sql_content}

    Com base nessas informações, gere o SQL para a seguinte pergunta:
    "{query}"
    """

    prompt_template = PromptTemplate(
        template=prompt_template_text,
        input_variables=["docs_ddl_content", "docs_documents_content", "docs_sql_content", "query"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )
    return prompt_template
