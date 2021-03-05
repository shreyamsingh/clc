from flask import Flask, render_template
import requests

app = Flask(__name__)

# default homepage
@app.route('/')
def homepage():
   return render_template('index.html')

# dog page
@app.route('/dog')
def getDog():
   response = requests.get('https://dog.ceo/api/breeds/image/random')
   imgURL = response.json()['message']
   return render_template('dog.html', url=imgURL)

# homepage if there's something after the / besides 'dog'
@app.route('/<name>')
def customHomepage(name):
   return render_template('index.html', name=name.title())
   
