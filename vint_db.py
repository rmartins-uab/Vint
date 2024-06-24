import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('vint.db')

# Criar um cursor
cursor = conn.cursor()

# Criar uma tabela
cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, url TEXT, desconto INTEGER)''')

# Salvar (commit) as mudanças
conn.commit()

# Fechar a conexão
conn.close()