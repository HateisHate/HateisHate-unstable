from flask import Flask, render_template, Markup
from subprocess import call
app = Flask(__name__)

@app.route('/')
def index():
	f = open("../README.md",'r')
	readme_text = f.read()
	f.close
	readme_text = Markup(readme_text)
	return render_template('index.html', readme=readme_text)
