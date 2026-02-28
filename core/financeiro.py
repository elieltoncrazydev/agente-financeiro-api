from datetime import date
from infra.database import get_connection, criar_tabela


# Garante que a tabela exista ao importar o módulo
criar_tabela()


def registrar_movimento(
    tipo,
    valor,
    categoria,
    descricao="",
    origem_entrada=None,
    tipo_gasto=None
):
    hoje = date.today()
    mes = hoje.month
    ano = hoje.year

    conn = get_connection()
    cursor = conn.cursor()

    # Buscar último saldo
    cursor.execute("SELECT saldo_atual FROM movimentos ORDER BY id DESC LIMIT 1")
    resultado = cursor.fetchone()

    saldo_anterior = resultado[0] if resultado else 0

    if tipo == "entrada":
        saldo_atual = saldo_anterior + valor
        origem = origem_entrada
    else:
        saldo_atual = saldo_anterior - valor
        origem = None

    cursor.execute("""
        INSERT INTO movimentos (
            tipo,
            valor,
            categoria,
            descricao,
            data,
            mes,
            ano,
            origem,
            tipo_gasto,
            saldo_atual
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        tipo,
        valor,
        categoria,
        descricao,
        hoje,
        mes,
        ano,
        origem,
        tipo_gasto,
        saldo_atual
    ))

    conn.commit()
    conn.close()


def listar_movimentos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            tipo,
            valor,
            categoria,
            descricao,
            data,
            mes,
            ano,
            origem,
            tipo_gasto,
            saldo_atual
        FROM movimentos
        ORDER BY id
    """)

    colunas = [desc[0] for desc in cursor.description]
    dados = cursor.fetchall()

    conn.close()

    return [dict(zip(colunas, linha)) for linha in dados]