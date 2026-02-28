from flask import Flask, request, jsonify

app = Flask(__name__)

# ============================
# ROTA RAIZ (STATUS DA API)
# ============================
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "API Agente Financeiro online"
    })


# ============================
# ROTA WHATSAPP (BOT)
# ============================
@app.route("/api/whatsapp", methods=["POST"])
def whatsapp():
    data = request.get_json()

    mensagem = data.get("mensagem", "").strip().lower()
    telefone = data.get("telefone")

    # ============================
    # COMANDO: !gastei
    # ============================
    if mensagem.startswith("!gastei"):
        partes = mensagem.split()

        # Validação básica
        if len(partes) < 3:
            return jsonify({
                "resposta": (
                    "❌ Uso incorreto.\n"
                    "Formato correto:\n"
                    "!gastei VALOR DESCRIÇÃO\n\n"
                    "Exemplo:\n"
                    "!gastei 50 mercado"
                )
            })

        # Tenta converter o valor
        try:
            valor = float(partes[1])
            descricao = " ".join(partes[2:])

            return jsonify({
                "resposta": (
                    "💸 *Gasto registrado com sucesso!*\n\n"
                    f"Valor: R$ {valor:.2f}\n"
                    f"Descrição: {descricao}"
                )
            })

        except ValueError:
            return jsonify({
                "resposta": (
                    "❌ Valor inválido.\n"
                    "Use apenas números.\n\n"
                    "Exemplo:\n"
                    "!gastei 50 mercado"
                )
            })

    # ============================
    # COMANDO DESCONHECIDO
    # ============================
    return jsonify({
        "resposta": (
            "❓ Comando não reconhecido.\n\n"
            "Comandos disponíveis:\n"
            "!gastei VALOR DESCRIÇÃO"
        )
    })


# ============================
# START DA APLICAÇÃO
# ============================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)