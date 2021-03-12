from flask import Flask, render_template
import requests

app = Flask(__name__)

# display plain text
@app.route('/rawtext')
def customHomepage():
   return "Hello! This doesn't use HTML, but you can still see these words on the website!"

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

app.run()
   
