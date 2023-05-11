from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['POST'])
@cross_origin()
def echo():
    data = request.json
    user_text = data['userText']
    list = ['1pdHpeJLP3rvbLyK6FkvNo','1JvJxRgnX0jgWvu1TIUOOh','0AVzrqkSr8JhJhzZ1$XluR']
    return jsonify({'echoedText': user_text, 'ids': list, 'answerText': 'and at the end the love you make is eaten like a piece of cake'})

if __name__ == '__main__':
    app.run()