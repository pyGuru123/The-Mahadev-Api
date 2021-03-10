import requests
from PIL import Image

url = 'http://127.0.0.1:5000//api/v1/mahadev'
try:
	r = requests.get(url)
	data = r.content
	with open('img.jpg', 'wb') as f:
		f.write(data)

	img = Image.open('img.jpg')
	img.show()
except:
	print('Check your internet connection')