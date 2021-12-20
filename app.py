
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
    noticias_mogi = resultado.DataFrame (noticias, '//div[@class="container-topo-3-colunas grid-x"]//div[@class="highlight__title theme-title-element "]//a'))
    vehtml = dados.to_html(render_links=True,index=False,escape=True,table_id="dados")
 return render_template("noticias.html", vehtml = dados )
