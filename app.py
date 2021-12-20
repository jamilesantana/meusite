import csv
import pandas as pd
from GoogleNews import GoogleNews
from flask import Flask, render_template 

def noticias():
    googlenews = GoogleNews()
    googlenews.set_lang('pt-br')
    googlenews.get_news("Mogi das Cruzes")
    resultado = googlenews.result()
    return pd.DataFrame(resultado)

app = Flask(_name_)
@app.route("/")
def hello_word():
    return render_template("home.html")
    

@app.route("/sobre")
def sobre():
    arquivo= open("templates/sobre.html")
    return arquivo.read()


@app.route("/raspador_noticias")
def raspador_noticias():
    googlenews = GoogleNews()
    googlenews.set_lang('pt-br')
    googlenews.get_news("Mogi das Cruzes")
    resultado = googlenews.result()
    df = pd.DataFrame(resultado) #coloca o resultado em uma tabela  
    return render_template("raspador_noticias.html", dados = df.to_html) # chama a variável dados que contém df para ser mostrada nesta seção do site

 
