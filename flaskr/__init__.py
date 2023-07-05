#   Launcher project - Home HUB
from flask import app, render_template, Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

