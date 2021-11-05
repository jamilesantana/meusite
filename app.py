from flask import Flask 

app = Flask(__name__)
@app.route("/")
def hello_word():
    return """<h1>Olá mundo!</h1> 
    <p><b>Esse é meu primeiro site</b>!</p>
    <a href="/sobre">Sobre esse site</a>
    """


@app.route("/sobre")
def sobre():
    return """<h1>Sobre</h1> 
    
    <a href="/">Página inicial</a>
    
    <p> Esse site foi criado por <b>Jamile Santana </b>.</p>"""




