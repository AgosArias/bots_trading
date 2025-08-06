import yfinance as yf
import requests
import time
import os

# ✅ Tomamos variables desde el entorno
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
TICKER = os.getenv("TICKER") or "AAPL"
PRECIO_OBJETIVO = float(os.getenv("PRECIO_OBJETIVO") or "180")
INTERVALO = int(os.getenv("INTERVALO") or "600")

def enviar_mensaje(mensaje):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": mensaje}
    requests.post(url, data=data)

def obtener_precio(ticker):
    data = yf.Ticker(ticker).history(period="1d")
    precio = data["Close"].iloc[-1]
    return precio

while True:
    try:
        precio = obtener_precio(TICKER)
        print(f"{TICKER}: {precio}")
        if precio >= PRECIO_OBJETIVO:
            enviar_mensaje(f"🚨 {TICKER} llegó a {precio:.2f} USD")
            break
    except Exception as e:
        enviar_mensaje(f"❌ Error: {e}")
    time.sleep(INTERVALO)
