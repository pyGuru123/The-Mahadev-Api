# The-Mahadev-Api

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/check-it-out.svg)](https://forthebadge.com)

### An Api to get Lord Mahadev Images. Har Har Mahadev 🕉️

<img alt="Shiva" align="right" width=200 height=150 src="https://st3.depositphotos.com/31221070/33178/v/380/depositphotos_331787960-stock-illustration-creative-abstract-illustration-lord-shiva.jpg">

 #### Happy Mahashivratri <br/>
 This Api is created to get random Lord Shiva images. The Api is created using flask and is
 hosted on Heroku. It's free to use and can be accessed using python packages like requests.

 #### Api is online here : [Mahadev Api](https://mahadev-api.herokuapp.com/api/v1/edited)

### The API endpoints are :

base url :  https://mahadev-api.herokuapp.com/api/v1/

* edited : to get edited shiva images [endpoint](https://mahadev-api.herokuapp.com/api/v1/edited)
* mahadev : to get rando mahadev images [endpoint](https://mahadev-api.herokuapp.com/api/v1/mahadev)
* shivlinga : to get random shivlinga images [endpoint](https://mahadev-api.herokuapp.com/api/v1/shivlinga)
* random : to get random edited, mahadev or shivlinga images [endpoint](https://mahadev-api.herokuapp.com/api/v1/random)
* today : to get daily date based random lord shiva images [endpoint](https://mahadev-api.herokuapp.com/api/v1/today)

### if you want to run it locally :
* clone the repo
* execute requirements.txt file
* run main.py
* open this location in browser : http://127.0.0.1:5000/api/v1/mahadev

### Requirements

All the requirements are provided inside the requirements.txt file, to install packages using this requirements.txt run the following 
command in cmd

```bash
pip3 install -r requirements.txt
```

to run test.py file, two additional packages are required. Install them from pip

```bash
pip install pillow
pip install reqeusts
```
