def validar_valor(texto: str):
    try:
        valor = float(texto.replace(",", "."))
        if valor <= 0:
            return None
        return valor
    except ValueError:
        return None


def validar_mes_ano(mes: str, ano: str) -> bool:
    if not (mes.isdigit() and ano.isdigit()):
        return False

    mes = int(mes)
    ano = int(ano)

    if mes < 1 or mes > 12:
        return False

    if ano < 2000 or ano > 2100:
        return False

    return True