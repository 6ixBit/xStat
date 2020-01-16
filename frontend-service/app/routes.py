from app import app
import requests

@app.route('/')
def index():
    res = requests.get("http://general-service/api/players")

    return res.json()