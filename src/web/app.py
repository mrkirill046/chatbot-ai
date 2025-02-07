from flask import Flask, request, jsonify, render_template
from src.scripts.chatbot import ChatBot

app = Flask(__name__)
chatbot = ChatBot()


@app.route('/')
def index():
    """
    The root route, which renders the `index.html` template.

    Returns:
    A rendered `index.html` template.
    """

    return render_template('index.html')


@app.route("/chat", methods=["POST"])
def chat():
    """
    Handles POST requests to the `/chat` endpoint, which are used for interacting with the chatbot.

    The request body should contain a JSON object with a "message" key, the value of which is a string representing the user's message.

    Returns:
    A JSON object with a "response" key, the value of which is a string representing the chatbot's response to the user's message.
    """

    user_message = request.json.get("message")

    if not user_message:
        return jsonify({"error": "Нет сообщения для обработки"}), 400

    bot_response = chatbot.respond(user_message)

    return jsonify({"response": bot_response})
