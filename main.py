from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def echo():
    data = request.json
    user_text = data['userText']
    return jsonify({'echoedText': user_text})

if __name__ == '__main__':
    app.run()