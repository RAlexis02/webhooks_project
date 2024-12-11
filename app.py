from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta principal para probar que el servidor está corriendo
@app.route('/', methods=['GET'])
def home():
    return "Hello, Webhooks!"

# Ruta para recibir un webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data:
        return jsonify({"message": "Webhook received!", "data": data}), 200
    else:
        return jsonify({"error": "No data received"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
