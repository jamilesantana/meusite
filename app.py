from flask import Flask 

app = Flask(__name__)
@app.route("/")
def hello_word():
    return "<p> Olá,<b>turma do fundão</b>!</p> Esse é meu primeiro site" 
