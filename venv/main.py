import yfinance as yf
import requests
import time

TICKER = "AAPL"
PRECIO_OBJETIVO = 180
TOKEN = "TU_TOKEN"
CHAT_ID = "TU_CHAT_ID"
INTERVALO = 600  # 10 minutos

def enviar_mensaje(mensaje):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": mensaje}
    requests.post(url, data=data)

while True:
    precio = yf.Ticker(TICKER).history(period="1d")["Close"].iloc[-1]
    print(f"Precio actual de {TICKER}: {precio}")
    if precio >= PRECIO_OBJETIVO:
        enviar_mensaje(f"📈 ¡{TICKER} alcanzó {precio} USD!")
        break
    time.sleep(INTERVALO)
