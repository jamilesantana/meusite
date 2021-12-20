import csv
import pandas as pd
from GoogleNews import GoogleNews
from flask import Flask, render_template 

def noticias():
    googlenews = GoogleNews()
    googlenews.set_lang('pt-br')
    googlenews.get_news("Mogi das Cruzes")
    resultado = googlenews.result()
    def path_to_image_html(path):
        return '<img src= "' + path + '" width ="60" >'
    resultado.to_html(escape = False, formatters=dict(img=path_to_image_html ))
    from IPython.core.display import HTML
    return HTML (resultado.to_html(escape=False, formatters=dict(img=path_to_image_html )))



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
    noticias_mogi = noticias()
    return render_template("noticias.html", dados = noticias_mogi)


