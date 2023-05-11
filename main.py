#%%  imports
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin


###### AI #####################################################
from langchain import OpenAI
from langchain.agents import create_csv_agent
import os
import json
#%%  set the key from the json file
# Opening JSON file
f = open('./config.json')
  
# returns JSON object as 
# a dictionary
config = json.load(f)

key = config['key']
file_path = config['csv']

# set the key
os.environ["OPENAI_API_KEY"] = key
# Closing file
f.close()

#%%  craete the agent
llm = OpenAI(temperature=0)
agent = create_csv_agent(llm, file_path, verbose=False)
print('agent created')
# print(agent.run('what is the most deviated element?'))
# print(key)
###############################################################

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['POST'])
@cross_origin()
def echo():
    data = request.json
    user_text = data['userText']
    print(user_text)
    chatbot_text = agent.run(user_text)
    print(chatbot_text)
    return jsonify({'echoedText': chatbot_text})

if __name__ == '__main__':
    app.run()
# http://localhost:8080/
# %%
#