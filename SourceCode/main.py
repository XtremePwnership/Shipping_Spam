# line 14 you need to insert your bot ID. No other changes required.

import json
import requests

from Shipping_Spam import spammer

from flask import Flask
from flask import request
from flask import Response

from flask_sslify import SSLify

token = "INSERT_YOUR_BOT'S_TOKEN_ID" #don't write 'bot' in front inside this string.

def write_json(data,filename='incoming_msg.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent = 4, ensure_ascii = False)

def parsit(message):
    senderId = message['message']['from']['id']
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    senderName = message['message']['from']['first_name']
    return chat_id, txt, senderId, senderName

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {'chat_id':chat_id, 'text': text}
    r = requests.post(url,json=payload)
    return r

app = Flask(__name__)
sslify = SSLify(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        chat_id, txt, senderId, senderName = parsit(msg)
        write_json(msg,'telegram_incoming.json') #this is just if you want to refer the json file
        if (senderId-4378925) != 702451676: #just a lame authentication check
            send_message(chat_id, "Sorry, this is a private bot. :) ")
            send_message("706830601",f"Unauthorized usage detected. Guilty party asf -  Name:{senderName}, Sender ID:{senderId}, Message:{txt}") #sends alert to bot owner's account. In case of emergency when someone uses your bot you can disrupt the connection entirely by running this command https://api.telegram.org/botID/deleteWebhook
            return Response('Ok', status=200)
        if txt == "/start":
            send_message(chat_id, "Hi. Send me 1 or more email IDs & i'll add 'em to the existing filter. (NB: no duplicate check in place currently)")
            return Response('Ok', status=200)
        output=spammer(txt)
        send_message(chat_id, output)
        return Response('Ok', status=200)
    else:
        return '<h1>Shipping Spam Bot</h1>'

if __name__ == '__main__':
    app.run(debug=True)
