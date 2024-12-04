from flask import Flask, request, jsonify
from lightllm import LLMPredictor  # Assuming this is how you import LightLLM

app = Flask(__name__)

# Load your LLM model
predictor = LLMPredictor(model_path="path/to/your/model")

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt')
    response = predictor.predict(prompt)  # Replace with the actual generation method
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))