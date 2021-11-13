import csv
import pandas as pd
from GoogleNews import GoogleNews
from flask import Flask 

def noticias():
    googlenews = GoogleNews()
    googlenews.set_lang('pt-br')
    googlenews.get_news("Mogi das Cruzes")
    resultado = googlenews.result()
    return pd.DataFrame(resultado)

app = Flask(__name__)
@app.route("/")
def hello_word():
    arquivo = open("templates/home.html")
    return arquivo.read()
    

@app.route("/sobre")
def sobre():
    arquivo= open("templates/sobre.html")
    return arquivo.read()


@app.route("/raspador_noticias")
def raspador_noticias():
    noticias_mogi = noticias()
    return render_template("noticias.html", dados = noticias_mogi)



