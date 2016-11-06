from flask import Flask, render_template
from subprocess import call
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
