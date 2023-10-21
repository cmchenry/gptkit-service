
import sys
import os
import json
from dotenv import load_dotenv
from flask import Flask, request
from openai_service import ask

app = Flask(__name__)
load_dotenv()
secret_key = os.environ.get('SECRET_KEY')
client_app_url = os.environ.get('CLIENT_APP_URL')
app.config['SECRET_KEY'] = secret_key
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'None'
app.config['SESSION_COOKIE_HTTPONLY'] = False

@app.route('/bot', methods=['POST'])
def bot():
    chat_log = request.form.get('chat_log', type=str, default='')
    chat_log = json.loads(chat_log)
    print(chat_log)
    answer = ask(chat_log)
    return answer

@app.after_request
def cors_headers(response):
    response.headers.add("Access-Control-Allow-Origin", client_app_url)
    response.headers.add('Access-Control-Allow-Credentials', "true")
    response.headers.add('Access-Control-Allow-Headers', "Origin, X-Requested-With, Content-Type, Accept")
    return response 