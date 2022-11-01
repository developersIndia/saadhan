from flask import Flask, request, render_template

app = Flask(__name__)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
    "Content-Type": "application/json",
}

API="https://developersIndia.github.io/resources/"


@app.route('/', methods=["GET"])
def index():
    return render_template('base.html')


@app.route('/category', methods=["GET"])
def category():
    params = request.args
    
    return f"{params}"
