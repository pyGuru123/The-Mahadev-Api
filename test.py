import requests
from PIL import Image

url = 'https://mahadev-api.herokuapp.com/api/v1/edited'
try:
	r = requests.get(url)
	data = r.content
	with open('img.jpg', 'wb') as f:
		f.write(data)

	img = Image.open('img.jpg')
	img.show()
except:
	print('Check your internet connection')