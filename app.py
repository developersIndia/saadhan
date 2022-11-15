from flask import Flask, request, render_template
from resourcer import resourcer

app = Flask(__name__)

CATEGORIES = {
    "Python": "python",
    "JavaScript": "javascript",
    "Data Structures & Algorithms": "dsa",
    "Machine Learning": "machine-learning",
    "Deep Learning": "deep-learning",
    "Computer Science": "computer-science",
    "Computer Graphics": "computer-graphics",
    "Git": "git",
    "Android": "android",
    "Surprise Me!": "miscellaneous",
}


@app.route("/", methods=["GET"])
def home():
    return render_template("categories.html", categories=CATEGORIES)


@app.route("/resources", methods=["GET"])
def category():
    params = request.args
    resources = resourcer.Resource.get_resource(params)
    return render_template("resources.html", resources=resources['resources'])