from flask import Flask, render_template, request
from urlfetch import extract_html, get_request
from scrappy import extract_headlines, get_headline_divs
import re

app = Flask(__name__)

@app.route('https://whatnownews.herokuapp.com/', methods=['POST','GET'])
def index():

    # Extract country names for dropdown list
    f = open('res/countries.txt','r')
    countries = f.readlines()

    for i in range(len(countries)):
        countries[i] = countries[i].strip()

    if request.method == 'GET':
        return render_template('index.html', countries=countries, country=None)
    elif request.method == 'POST':
        country = re.sub('\s','%20',request.form['countries'])
        url = f'https://news.google.com/search?q={country}&hl=en-ZA&gl=ZA&ceid=ZA%3Aen'
        html = extract_html(get_request(url))
        news = extract_headlines(get_headline_divs(html))

        return render_template('index.html', news=news, countries=countries)
