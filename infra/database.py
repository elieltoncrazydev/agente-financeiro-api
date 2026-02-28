import os
import psycopg2

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL não definida no ambiente")


def get_connection():
    return psycopg2.connect(DATABASE_URL)


def criar_tabela():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movimentos (
            id SERIAL PRIMARY KEY,
            tipo TEXT,
            valor NUMERIC,
            categoria TEXT,
            descricao TEXT,
            data DATE,
            mes INTEGER,
            ano INTEGER,
            origem TEXT,
            tipo_gasto TEXT,
            saldo_atual NUMERIC
        )
    """)

    conn.commit()
    conn.close()