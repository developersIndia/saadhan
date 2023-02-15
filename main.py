import os
from pathlib import Path
from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms.fields import SelectField
from dotenv import load_dotenv
from resourcer import resourcer

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY") or "SECRET_KEY"


class FilterLevelForm(FlaskForm):
    level = SelectField("level", choices=[
        ("beginner", "beginner"),
        ("intermediate", "intermediate"),
        ("advanced", "advanced"),
        ("everyone", "everyone"),
    ])


class FilterTypeForm(FlaskForm):
    type = SelectField("type", choices=[
        ("video", "video"),
        ("article", "article"),
        ("book", "book"),
        ("github", "github"),
        ("course", "course"),
        ("audio", "audio"),
        ("cheatsheet", "cheatsheet"),
        ("website", "website"),
    ])


app = Flask(__name__)
app.config.from_object(Config)

CATEGORIES = {
    "Python": "python",
    "JavaScript": "javascript",
    "C++": "cpp",
    "C":"c",
    "CSS":"css",
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
    category = request.args.get("category")
    rsr = resourcer.Resource(category)
    resources = rsr.get_resource()
    level_form = FilterLevelForm()
    type_form = FilterTypeForm()
    return render_template(
        "resources.html", resources=resources["resources"], category=category, level_form=level_form, type_form=type_form
    )


@app.route("/contributors", methods=["GET"])
def contributors():
    contributors = resourcer.Resource.get_all_contributors()
    saadhan__contributors = resourcer.Resource.get_saadhan_contributors()
    return render_template(
        "contributors.html", contributors=contributors["contributors"]+saadhan__contributors["contributors"]
    )


@app.route("/filtered_resources", methods=["POST"])
def filtered_resources():
    rsr = resourcer.Resource(request.form.get("category"))
    level_form = FilterLevelForm()
    if level_form.validate_on_submit():
        res_level = level_form.level.data
        resources = rsr.get_resources_by_level(res_level)
        return render_template("filtered_resources.html", resources=resources)

    type_form = FilterTypeForm()
    if type_form.validate_on_submit():
        res_type = type_form.type.data
        resources = rsr.get_resources_by_type(res_type)
        return render_template("filtered_resources.html", resources=resources)

    return "Wuba luba dub dub"


if __name__ == "__main__":
    app.run(debug=True)
