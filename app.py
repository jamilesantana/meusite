import pandas as pd
import os
from pandas import json_normalize 
from flask import Flask, render_template
from GoogleNews import GoogleNews 
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route('/noticias')
def news():
    googlenews = GoogleNews()
    googlenews.set_lang('pt-br') 
    googlenews.get_news("'transparência pública'") 
    googlenews.get_news("'Lei de Acesso à Informação'") 
    resultado = googlenews.result() 
    
    df = pd.DataFrame(resultado) 
    df1= df.drop(columns=['desc', 'datetime', 'img', 'media']) 
    return render_template("noticias.html", dados = df1.to_html()) 

 
