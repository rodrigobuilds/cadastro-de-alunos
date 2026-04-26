import sqlite3

try:
    con = sqlite3.connect('cadastro_alunos.db')
    print('Conexão com o banco de dados realizada com sucesso!')
except sqlite3.Error as e:
    print('Erro ao conectar com o banco de dados:', e)

# Tabela cursos
try:
    with con:
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS cursos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                duracao TEXT,
                preco REAL      
            )
        """)
        print('Tabela cursos criada com sucesso!')
except sqlite3.Error as e:
    print('Erro ao criar a tabela cursos:', e)

# Tabela turmas
try:
    with con:
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS turmas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                curso_id INTEGER,
                data_inicio DATE,
                FOREIGN KEY (curso_id) REFERENCES cursos(id) 
                ON UPDATE CASCADE ON DELETE CASCADE
            )
        """)
        print('Tabela turmas criada com sucesso!')
except sqlite3.Error as e:
    print('Erro ao criar tabela turmas:', e)

# Tabela alunos
try:
    with con:
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS alunos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                email TEXT,
                telefone TEXT,
                sexo TEXT,
                imagem TEXT,
                data_nascimento DATE,
                cpf TEXT,
                turma_nome TEXT
            )
        """)
        print('Tabela alunos criada com sucesso!')
except sqlite3.Error as e:
    print('Erro ao criar a tabela alunos:', e)