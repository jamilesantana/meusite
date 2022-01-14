import pandas as pd
import os
from pandas import json_normalize 
from flask import Flask, render_template
from GoogleNews import GoogleNews 
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
    googlenews = GoogleNews()
    googlenews.set_lang('pt-br') 
    googlenews.get_news("'transparência pública'") 
    googlenews.get_news("'Lei de Acesso à Informação'") 
    resultado = googlenews.result() 
    
    df = pd.DataFrame(resultado) 
    df1= df.drop(columns=['desc', 'datetime', 'img', 'media']) 
    return render_template("noticias.html", dados = df1.to_html()) 

           
 from flask 
 import requestimport requests
           
@app.route("/telegram", methods=["POST"])
def telegram():
           token = "5034498375:AAENMAIqZObmce_hDdU90ZuT9evXEskHTGY"
           dados = request.json
           mensagem = {"chat_id": dados["message"]["chat"]["id"], "text": "oi!"}
           url = f"https://api.telegram.org/bot{token}/sendMessage"
           requests.post(url, data=mensagem)
           return "ok"
