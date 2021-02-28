import sqlite3

from sqlite3 import Error


def ConexaoBanco():
    caminho="C:\\Users\\leand\\Desktop\\Python\\python_sqlite\\banco\\agenda.db"

    conn = None

    try:
        conn=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return conn

vcon = ConexaoBanco()

vsql = """CREATE TABLE tb_contatos(
            N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
            T_NOMECONTATO VARCHAR(30),
            T_TELEFONECONTATO VARCHAR(14),
            T_EMAILCONTATO VARCHAR(30)
        );"""

def criarTabela(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        print('Tabela criada')
    except Error as ex:
        print(ex)

criarTabela(vcon,vsql)

vcon.close()
