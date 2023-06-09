#%%  imports
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin


###### AI #####################################################
from langchain import OpenAI
from langchain.agents import create_csv_agent
import os
import json
import ast
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
# user_text = 'select 50 random walls'
# try:
#     chatbot_text = agent.run(user_text)
#     guid_list = agent.run(user_text + ' ' + pm.prefix_filtering)
# except:
#     chatbot_text = pm.error_message
# print(agent.run('what is the most deviated element?'))
# print(key)
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
        chatbot_text = agent.run(user_text)
        guid_list = agent.run(user_text + ' ' + pm.prefix_filtering)
        #just grab the string within the brackets
        guid_list = '[' + guid_list.split('[')[1].split(']')[0] + ']'
        try:
            guid_list = ast.literal_eval(guid_list)
        except:
            print(f'guid_list {guid_list} cannot be converted to a list')
            pass
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