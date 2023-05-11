#%%  imports
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin


###### AI #####################################################
from langchain import OpenAI
from langchain.agents import create_csv_agent
import os
import json
#%%  set the key from the json file
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)
key = config['key']
file_path = config['csv']

# set the key
os.environ["OPENAI_API_KEY"] = key

#%%  craete the agent
llm = OpenAI(temperature=0)
agent = create_csv_agent(llm, file_path, verbose=False)
print('agent created')
###############################################################

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['POST'])
@cross_origin()
def echo():
    data = request.json
    user_text = data['userText']
    chatbot_text = agent.run(user_text)
    return jsonify({'echoedText': chatbot_text})

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080) # http://localhost:8080/
# %%
#