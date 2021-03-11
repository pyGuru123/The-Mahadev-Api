# The Mahadev Api
# An api to get random lord shiva images

from math import ceil
from random import randint, choice
from datetime import datetime
from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/api/v1/mahadev', methods=['GET'])
def mahadev_pic():
	im_index = randint(1,150)
	file = f'assets/imgs/mahadev{im_index}.jpg'
	return send_file(file, mimetype='image/jpg')

@app.route('/api/v1/shivlinga', methods=['GET'])
def shivlinga_pic():
	im_index = randint(1,150)
	file = f'assets/imgs/shivlinga{im_index}.jpg'
	return send_file(file, mimetype='image/jpg')

@app.route('/api/v1/edited', methods=['GET'])
def edited_pic():
	im_index = randint(1,150)
	file = f'assets/imgs/edited{im_index}.jpg'
	return send_file(file, mimetype='image/jpg')

@app.route('/api/v1/random', methods=['GET'])
def random_pic():
	im_index = randint(1,150)
	type_ = choice(['mahadev', 'shivlinga', 'edited'])
	file = f'assets/imgs/{type_}{im_index}.jpg'
	return send_file(file, mimetype='image/jpg')

@app.route('/api/v1/today', methods=['GET'])
def today_pic():
	day_dict = {
		1 : 'edited',
		2 : 'mahadev',
		3 : 'shivlinga'
	}

	day_of_year = datetime.now().timetuple().tm_yday
	type_num = ceil(day_of_year / 150)
	type_ = day_dict.get(type_num, None)
	if type_ is None:
		return 'an error occured'
	
	im_index = day_of_year % 150
	if im_index == 0:
		im_index = 150
	file = f'assets/imgs/{type_}{im_index}.jpg'
	return send_file(file, mimetype='image/jpg')

if __name__ == '__main__':
	app.run(threaded=True, port=5000)