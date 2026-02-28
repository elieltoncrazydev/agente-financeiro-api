from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "API Agente Financeiro online"})

@app.route("/api/whatsapp", methods=["POST"])
def whatsapp():
    data = request.get_json()
    mensagem = data.get("mensagem")
    telefone = data.get("telefone")

    return jsonify({
        "resposta": "✅ Bot conectado com sucesso! Mensagem recebida."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)