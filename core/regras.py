from infra.database import inserir_transacao, calcular_saldo
def inserir_transacao(tipo, valor, categoria):
    pass

def calcular_saldo():
    return 0.0

from core.validacoes import validar_valor
from core.normalizacao import normalizar_categoria
from infra.database import inserir_transacao, calcular_saldo

def registrar_gasto(mensagem: str):
    partes = mensagem.split()

    if len(partes) < 3:
        return False, (
            "❌ Uso incorreto.\n"
            "Formato correto:\n"
            "gastei VALOR DESCRIÇÃO\n\n"
            "Exemplo:\n"
            "gastei 50 mercado"
        )

    valor = validar_valor(partes[1])
    if valor is None:
        return False, "❌ Valor inválido."

    categoria = normalizar_categoria(" ".join(partes[2:]))

    inserir_transacao("despesa", valor, categoria)

    return True, (
        "💸 *Gasto registrado com sucesso!*\n\n"
        f"Valor: R$ {valor:.2f}\n"
        f"Categoria: {categoria}"
    )


def obter_saldo():
    saldo = calcular_saldo()
    return f"💰 Saldo atual: R$ {saldo:.2f}"