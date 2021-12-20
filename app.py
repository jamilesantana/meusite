import csv
import pandas as pd
from GoogleNews import GoogleNews
from flask import Flask, render_template 

def noticias():
    googlenews = GoogleNews()
    googlenews.set_lang('pt-br')
    googlenews.get_news("Mogi das Cruzes")
    resultado = googlenews.result():
    
    
    
app = Flask(__name__)
@app.route("/")
def hello_word():
    return render_template("home.html")
    

@app.route("/sobre")
def sobre():
    arquivo= open("templates/sobre.html")
    return arquivo.read()


@app.route("/raspador_noticias")
def raspador_noticias():
    noticias_mogi_html = noticias()
    return render_template( "raspador_notícias.html", html_resultados = noticias_mogi_html.to_html)


