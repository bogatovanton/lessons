from flask import Flask, request, render_template, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

OLLAMA_API_URL = "http://localhost:11434/api/chat"
@app.route('/api/ask', methods=['POST'])
def ask():
    user_input = request.json.get('input')

    
    payload = {
        "model": "gpt-oss:20b-cloud",  
        "messages": [
            {
                "role": "user",  
                "content": user_input  
            }
        ],
        "stream": False  
    }

    try:
        
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()  

        
        model_response = response.json().get('message', {}).get('content', '')

        return jsonify({"response": model_response})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Ошибка при запросе к модели: {str(e)}"}), 500
    
if __name__ == '__main__':
    app.run(debug=True)
