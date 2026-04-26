import sqlite3 as lite

try:
    con = lite.connect('cadastro_alunos.db')
    print('Conexão com o banco de dados criada com sucesso!')
except lite.Error as e:
    print("Erro ao conectar com o banco de dados:", e)

# Criando as tabelas automaticamente se não existirem
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
    print('Tabelas verificadas com sucesso!')


# ─────────────────────────────────────────
# CURSOS
# ─────────────────────────────────────────

def criar_cursos(i):
    if len(i) != 3:
        raise ValueError("Esperado 3 elementos, recebeu {}".format(len(i)))
    with con:
        cur = con.cursor()
        query = "INSERT INTO cursos (nome, duracao, preco) VALUES (?, ?, ?)"
        cur.execute(query, i)

def ver_cursos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM cursos')
        linha = cur.fetchall()
        for i in linha:
            lista.append(i)
    return lista

def atualizar_curso(i):
    with con:
        cur = con.cursor()
        query = "UPDATE cursos SET nome=?, duracao=?, preco=? WHERE id=?"
        cur.execute(query, i)

def deletar_curso(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM cursos WHERE id=?"
        cur.execute(query, (i,))


# ─────────────────────────────────────────
# TURMAS
# ─────────────────────────────────────────

def criar_turma(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO turmas (nome, curso_id, data_inicio) VALUES (?, ?, ?)"
        cur.execute(query, i)

def ver_turmas():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM turmas')
        linha = cur.fetchall()
        for i in linha:
            lista.append(i)
    return lista

def atualizar_turma(i):
    with con:
        cur = con.cursor()
        query = "UPDATE turmas SET nome=?, curso_id=?, data_inicio=? WHERE id=?"
        cur.execute(query, i)

def deletar_turma(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM turmas WHERE id=?"
        cur.execute(query, (i,))


# ─────────────────────────────────────────
# ALUNOS
# ─────────────────────────────────────────

def criar_alunos(i):
    with con:
        cur = con.cursor()
        query = """INSERT INTO alunos 
                   (nome, email, telefone, sexo, imagem, data_nascimento, cpf, turma_nome) 
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
        cur.execute(query, i)

def ver_alunos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM alunos')
        linha = cur.fetchall()
        for i in linha:
            lista.append(i)
    return lista

def buscar_aluno(nome):
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM alunos WHERE nome LIKE ?"
        cur.execute(query, ('%' + nome + '%',))
        linha = cur.fetchall()
        for i in linha:
            lista.append(i)
    return lista

def atualizar_aluno(i):
    with con:
        cur = con.cursor()
        query = """UPDATE alunos 
                   SET nome=?, email=?, telefone=?, sexo=?, imagem=?, 
                       data_nascimento=?, cpf=?, turma_nome=? 
                   WHERE id=?"""
        cur.execute(query, i)

def deletar_aluno(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM alunos WHERE id=?"
        cur.execute(query, (i,))