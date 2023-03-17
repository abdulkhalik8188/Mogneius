import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'LazyDeveloper'

os.system("git clone https://abdulkhalik8188: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/abdulkhalik8188/LazyPrincessV2 okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 bot.py &")
