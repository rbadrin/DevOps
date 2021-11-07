from app import index
from app import getWeather
import requests

def test_index():
        assert index() == "<h1>Hello world!!</h1><br> Use '/getWeather' to nav to weather api</p>"

def test_getWeather():
        r = requests.get("https://api.openweathermap.org/data/2.5/weather?q=chennai&appid=06c921750b9a82d8f5d1294e1586276f")
        assert r.status_code == 200
