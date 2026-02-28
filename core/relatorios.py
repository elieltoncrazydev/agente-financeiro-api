def relatorio_por_categoria(movimentos):
    """
    Gera um resumo financeiro agrupado por categoria
    """

    resumo = {}

    for m in movimentos:
        categoria = m["categoria"]
        tipo = m["tipo"]
        valor = m["valor"]

        if categoria not in resumo:
            resumo[categoria] = {
                "entrada": 0.0,
                "saida": 0.0
            }

        resumo[categoria][tipo] += valor

    return resumo

def resumo_entradas_por_origem(movimentos):
    resumo = {}

    for m in movimentos:
        if m["tipo"] != "entrada":
            continue

        origem = m["origem"]
        resumo[origem] = resumo.get(origem, 0) + m["valor"]

    return resumo


def resumo_saidas_por_tipo_gasto(movimentos):
    resumo = {
        "fixo": 0.0,
        "variavel": 0.0,
        "cartao": 0.0
    }

    for m in movimentos:
        if m["tipo"] != "saida":
            continue

        tipo_gasto = m["tipo_gasto"]
        resumo[tipo_gasto] += m["valor"]

    return resumo


def gasto_real_mensal(movimentos):
    total = 0.0

    for m in movimentos:
        if m["tipo"] == "saida" and m["tipo_gasto"] != "cartao":
            total += m["valor"]

    return total


def comprometimento_cartao(movimentos):
    total = 0.0

    for m in movimentos:
        if m["tipo"] == "saida" and m["tipo_gasto"] == "cartao":
            total += m["valor"]

    return total

def relatorio_mensal(movimentos, mes, ano):
    relatorio = {
        "mes": mes,
        "ano": ano,
        "entradas": 0.0,
        "saidas": 0.0,
        "saldo_mes": 0.0,
        "entradas_por_origem": {},
        "saidas_por_tipo": {
            "fixo": 0.0,
            "variavel": 0.0,
            "cartao": 0.0
        }
    }

    for m in movimentos:
        if m["mes"] != mes or m["ano"] != ano:
            continue

        if m["tipo"] == "entrada":
            valor = m["valor"]
            relatorio["entradas"] += valor

            origem = m["origem"]
            relatorio["entradas_por_origem"][origem] = (
                relatorio["entradas_por_origem"].get(origem, 0) + valor
            )

        else:  # saída
            valor = m["valor"]
            relatorio["saidas"] += valor

            tipo_gasto = m["tipo_gasto"]
            relatorio["saidas_por_tipo"][tipo_gasto] += valor

    relatorio["saldo_mes"] = relatorio["entradas"] - relatorio["saidas"]
    return relatorio