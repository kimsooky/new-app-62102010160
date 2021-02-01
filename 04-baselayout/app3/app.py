from flask import Flask
from flask import render_template
from flask import request
from urllib.parse import quote
from urllib.request import urlopen
import json

app = Flask(__name__)

OPEN_WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?q={0}&units=metric&APPID={1}"

OPEN_WEATHER_KEY = '99b45c40d36d608ad54c3b7ffa1c11aa'

@app.route("/")
def home():
    city = request.args.get('city')
    if not city:
        city = 'melbourne'
    weather = get_weather(city, OPEN_WEATHER_KEY)

    return render_template("home.html", weather=weather)


def get_weather(city,API_KEY):
    query = quote(city)
    url = OPEN_WEATHER_URL.format(city, API_KEY)
    data = urlopen(url).read()
    parsed = json.loads(data)
    weather = None
    if parsed.get('weather'):

        description = parsed['weather'][0]['description']
        temperature = parsed['main']['temp']
        city = parsed['name']
        country = parsed['sys']['country']

        weather = {'description': description,
                   'temperature': temperature,
                   'city': city,
                   'country': country
                   }
    return weather

