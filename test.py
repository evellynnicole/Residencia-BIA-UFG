import sqlite3

conexao = sqlite3.connect(r'C:\Users\mevel\OneDrive\Área de Trabalho\Residência\futebol.db')

cursor = conexao.cursor()

consulta_sql = """
SELECT time_nome, saldo_gols FROM tabela WHERE saldo_gols < 0;
"""

cursor.execute(consulta_sql)

resultados = cursor.fetchall()

print(resultados)