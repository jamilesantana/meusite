from flask import Flask 

app = Flask(__name__)
@app.route("/")
def hello_word():
    return "<p> Olá! <b> Esse é meu primeiro site</b>!</p>" 

@app.route("/sobre")
def sobre():
    return "<h1>Sobre</h1> <p> Esse site foi criado por <b>Jamile Santana </b>.</p>"
