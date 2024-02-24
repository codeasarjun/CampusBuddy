from flask import Flask, render_template, request
from core.chatbot import chatbot

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for handling user input and returning chatbot responses
@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    response = chatbot.respond(user_input)
    return response

if __name__ == '__main__':
    app.run(debug=True)
