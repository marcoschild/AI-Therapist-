import openai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Replace 'your-api-key' with your actual OpenAI API key
OPENAI_API_KEY = 'your-api-key'
openai.api_key = OPENAI_API_KEY

def get_therapist_response(user_input):
    """Generates a response from the AI therapist."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an empathetic AI therapist who provides thoughtful and supportive responses."},
                {"role": "user", "content": user_input}
            ]
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return "I'm sorry, but I encountered an error. Please try again later."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"response": "Please enter a message."})
    
    response = get_therapist_response(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
