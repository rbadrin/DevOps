from flask import Flask
import requests


app = Flask(__name__)


@app.route('/')
def index():
	return "<h1>Hello world!!</h1><br> Use '/getWeather' to nav to weather api</p>"

@app.route('/getWeather')
def getWeather():
    city = "chennai"
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    final_info = "<br><center>"+condition + "<br><center>" + str(temp) + "°C" + "<br><center>"
    final_data = "<br><center>"+ "Min Temp: " + str(min_temp) + "°C" + "<br><center>" + "Max Temp: " + str(max_temp) + "°C" +"<br><center>" + "Pressure: " + str(pressure) + "<br><center>" +"Humidity: " + str(humidity) + "<br><center>" +"Wind Speed: " + str(wind) 


if __name__ == "__main__":
	app.run(debug=True)
