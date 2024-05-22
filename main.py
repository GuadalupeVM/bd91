from flask import Flask, request, jsonify, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    prompt = request.form['prompt']
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "llama2",
        "prompt": prompt,
        "system": "Responde como si fueras Son Goku",
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        result = response.json()
        answer = result.get("response", "No se recibió respuesta.")
    else:
        answer = f"Error: {response.status_code}"

    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)