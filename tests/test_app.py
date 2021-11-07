from app import index

def test_index():
	assert index() == "<h1>Hello world!!</h1>"
