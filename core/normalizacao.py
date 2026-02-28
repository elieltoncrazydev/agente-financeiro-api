import unicodedata

def normalizar_texto(texto: str) -> str:
    """
    Remove acentos, deixa minúsculo e normaliza espaços.
    """
    texto = texto.strip().lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(
        c for c in texto if unicodedata.category(c) != "Mn"
    )
    texto = " ".join(texto.split())
    return texto


# Categorias padrão reaproveitadas do projeto antigo
CATEGORIAS_PADRAO = {
    "mercado": ["mercado", "supermercado", "super", "compras"],
    "cafe": ["cafe", "café", "coffee", "cafezinho"],
    "transporte": ["uber", "99", "onibus", "ônibus", "metro", "metrô"],
    "lazer": ["cinema", "filme", "show", "jogo"],
    "salario": ["salario", "salário", "pagamento"],
    "extra": ["extra", "bonus", "bônus"]
}

def normalizar_categoria(texto: str) -> str:
    """
    Normaliza a categoria com base em sinônimos.
    """
    texto = normalizar_texto(texto)

    for categoria, variacoes in CATEGORIAS_PADRAO.items():
        if texto in variacoes:
            return categoria

    return texto