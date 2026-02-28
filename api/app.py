from flask import Flask, request, jsonify
from core.regras import registrar_gasto, obter_saldo

app = Flask(__name__)

# =========================
# ROTA DE STATUS
# =========================
@app.route("/", methods=["GET"])
def status():
    return jsonify({
        "status": "API Agente Financeiro online"
    })


# =========================
# ROTA WHATSAPP (HTTP)
# =========================
@app.route("/api/whatsapp", methods=["POST"])
def whatsapp():
    data = request.get_json(silent=True) or {}

    mensagem = (data.get("mensagem") or "").strip().lower()

    if mensagem.startswith("gastei"):
        _, resposta = registrar_gasto(mensagem)
        return jsonify({"resposta": resposta})

    if mensagem == "saldo":
        return jsonify({"resposta": obter_saldo()})

    return jsonify({
        "resposta": (
            "❓ Comando não reconhecido.\n\n"
            "Comandos disponíveis:\n"
            "- gastei VALOR DESCRIÇÃO\n"
            "- saldo"
        )
    })


# =========================
# START LOCAL
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)