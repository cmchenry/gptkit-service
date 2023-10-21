import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.environ.get('OPENAI_KEY')
completion = openai.Completion()
chat_completion = openai.ChatCompletion()
model = openai.Model();   

def ask(chat_log):
    prompt = {"role": "system", "content": "You are a helpful assistant.  Please answer any questions the user asks in a professional tone."}
    chat_log.insert(0, prompt)
    print(chat_log)

    response = chat_completion.create(
        model="gpt-3.5-turbo",
        messages=chat_log,
        temperature=0.9,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        max_tokens=150)

    answer = response['choices'][0]['message']['content']
    return answer