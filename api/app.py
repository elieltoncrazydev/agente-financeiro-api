from flask import Flask, jsonify

app = Flask(__name__)

# Rota raiz para teste de status da API
@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "API Agente Financeiro online"})

# (Futuras rotas do agente financeiro entram aqui)
# ex: /mensagem, /saldo, /relatorio, etc.

# ==============================
# PONTO CRÍTICO PARA DEPLOY
# ==============================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)