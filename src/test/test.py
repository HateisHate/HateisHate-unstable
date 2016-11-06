from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'HATE IS HATE - TWITTER APP FOR HACKATHON. V.0.0.1.'
