from flask import Flask, render_template
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():
    return "Bot up and running"

def run():
    app.run(port=8080,host="0.0.0.0")

def keep_alive():
    t = Thread(target=run)
    t.start()
