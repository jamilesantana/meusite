from flask import Flask 

app = Flask(__name__)
@app.route("/")
def hello_word():
    return "<p> Olá! <b> Esse é meu primeiro site</b>!</p>" 
