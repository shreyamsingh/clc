from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
   return render_template('index.html')

@app.route('/dog')
def getDog():
   return render_template('dog.html', url=requests.get('https://dog.ceo/api/breeds/image/random').json()['message'])

@app.route('/<name>')
def customHomepage(name):
   return render_template('index.html', name=name)
   
