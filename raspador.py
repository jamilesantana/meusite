import pandas as pd
import requests
from GoogleNews import GoogleNews
from pandas import json_normalize

def raspador_noticias():
    googlenews = GoogleNews()
    googlenews.set_lang("pt-br")
    googlenews.get_news("'transparência pública'")
    googlenews.get_news("'Lei de Acesso à Informação'")
    resultado = googlenews.result()
    

    df = pd.DataFrame(resultado)
    return render_template("noticias.html", dados=df.to_dict("records"))
