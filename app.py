import os

import pandas as pd
import requests
from GoogleNews import GoogleNews
from flask import Flask, render_template, request
from pandas import json_normalize


app = Flask(__name__)


@app.route("/")
def hello_word():
    return render_template("home.html")


@app.route("/sobre")
def sobre():
    arquivo = open("templates/sobre.html")
    return arquivo.read()


@app.route("/raspador_noticias")
def raspador_noticias():
    googlenews = GoogleNews()
    googlenews.set_lang("pt-br")
    googlenews.get_news("'transparência pública'")
    googlenews.get_news("'Lei de Acesso à Informação'")
    resultado = googlenews.result()
    

    df = pd.DataFrame(resultado)
    return render_template("noticias.html", dados=df.to_dict("records"))
