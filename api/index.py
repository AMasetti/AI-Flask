from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize a global JSON object to store messages
messages = {
    "message_list": []
}

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

# POST endpoint to add a string to the message list
@app.route('/add_message', methods=['POST'])
def add_message():
    data = request.json
    if 'message' in data:
        message = data['message']
        messages['message_list'].append(message)
        return jsonify({"message": f"Added '{message}' to the message list"})
    else:
        return jsonify({"error": "Invalid data format"}), 400

# GET endpoint to retrieve and delete the latest message
@app.route('/get_latest_message', methods=['GET'])
def get_latest_message():
    if len(messages['message_list']) > 0:
        latest_message = messages['message_list'].pop()
        return jsonify({"message": latest_message})
    else:
        return jsonify({"message": "No messages available"})

