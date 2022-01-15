import requests
import os

from raspador import raspador_noticias
token = os.environ["TELEGRAM_TOKEN"]
url = f"https://api.telegram.org/bot{token}/sendMessage"
chat_id = 879112212
text = f"Olá! Acabei de atualizar a lista de notícias sobre Transparência Pública para data {Data}.\nSite: {Site}\nTítulo: {Título}"
message = {"chat_id": chat_id, "text": text}
requests.post(url, data=message)
