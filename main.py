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
agent = create_csv_agent(llm, file_path, verbose=True)
print('agent created')
import prompt as pm
agent.run(pm.prefix_csv_description)
user_text = 'select 50 random walls'
try:
    chatbot_text = agent.run(user_text)
    guid_list = agent.run(user_text + ' ' + pm.prefix_filtering)
except:
    chatbot_text = pm.error_message
# print(agent.run('what is the most deviated element?'))
# print(key)
###############################################################
#%% image
# import base64

# with open("yourfile.ext", "rb") as image_file:
#     encoded_string = base64.b64encode(image_file.read())

# import PIL.Image

# # assume data contains your decoded image
# file_like = os.StringIO(data)

# img = PIL.Image.open(file_like)
# img.show()
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
    except:
        chatbot_text = pm.error_message
    print(chatbot_text)
    print(guid_list)
    return jsonify({'echoedText': chatbot_text,
                    'guidList': guid_list})

if __name__ == '__main__':
    app.run()
# http://localhost:8080/
# %%
#