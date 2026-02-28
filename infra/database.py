import sqlite3
from datetime import datetime
from pathlib import Path

# Caminho absoluto do banco
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "financeiro.db"


def conectar():
    return sqlite3.connect(DB_PATH)


def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,
            valor REAL NOT NULL,
            categoria TEXT NOT NULL,
            data TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


def inserir_transacao(tipo: str, valor: float, categoria: str):
    criar_tabela()

    conexao = conectar()
    cursor = conexao.cursor()

    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO transacoes (tipo, valor, categoria, data)
        VALUES (?, ?, ?, ?)
    """, (tipo, valor, categoria, data))

    conexao.commit()
    conexao.close()


def calcular_saldo() -> float:
    criar_tabela()

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT tipo, valor FROM transacoes")
    registros = cursor.fetchall()

    saldo = 0.0
    for tipo, valor in registros:
        if tipo == "receita":
            saldo += valor
        else:
            saldo -= valor

    conexao.close()
    return saldo