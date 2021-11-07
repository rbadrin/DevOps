from app import index

def test_index():
	assert index() == "<h1>Hello world!!</h1><br> Use '/getWeather' to nav to weather api</p>"
