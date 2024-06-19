from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Pre-defined responses for the chatbot
responses = {
    "hello": "Hi there! How can I help you today?",
    "how are you": "I'm just a bot, but I'm here to assist you!",
    "bye": "Goodbye! Have a great day!",
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    print(f"User message: {user_message}")  # Debugging
    bot_response = responses.get(user_message.lower(), "I'm not sure how to respond to that.")
    print(f"Bot response: {bot_response}")  # Debugging
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    # Debugging: Print the current working directory
    print("Current Working Directory:", os.getcwd())
    
    # Debugging: Verify template directory and its contents
    template_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates')
    print("Template Folder:", template_dir)
    print("Files in Template Directory:", os.listdir(template_dir))
    
    app.run(debug=True)
