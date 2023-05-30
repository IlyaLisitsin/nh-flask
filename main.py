#%%  imports
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import ast

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
os.environ["OPENAI_API_KEY"] = key[0:-5] # remove the last 5 characters
# Closing file
f.close()

#%%  craete the agent
llm = OpenAI(temperature=0)
agent = create_csv_agent(llm, file_path, verbose=True)
print('agent created')
import prompt as pm
agent.run(pm.prefix_csv_description)
###############################################################
#%%  app 
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['POST'])
@cross_origin()
def echo():
    data = request.json
    user_text = data['userText']
    print(user_text)
    try:
        # chatbot_text = agent.run(user_text)
        # make user_text lowercase
        if user_text.lower().startswith('select') or user_text.lower().startswith('show') or user_text.lower().startswith('display'):
            guid_list = agent.run(pm.prefix_filtering + ' ' + user_text)
            if '[' in guid_list and ']' in guid_list:
                chatbot_text = guid_list.split('[')[0]
                if chatbot_text == '':
                    chatbot_text = 'I updated the viewer. :)'
                guid_list = '[' + guid_list.split('[')[1].split(']')[0] + ']'
            try:
                guid_list = ast.literal_eval(guid_list)
            except:
                print(f'guid_list {guid_list} cannot be converted to a list')
                pass
        else:
            chatbot_text = agent.run(user_text)
            guid_list = []
    except:
        chatbot_text = pm.error_message
        guid_list = []
        
    
    return jsonify({'answerText': chatbot_text,
                    'ids': guid_list})

if __name__ == '__main__':
    app.run()
# http://localhost:8080/
# %%
#