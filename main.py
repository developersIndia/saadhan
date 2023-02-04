from flask import Flask, request, render_template
from resourcer import resourcer

app = Flask(__name__)

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
    return render_template(
        "resources.html", resources=resources["resources"], category=category
    )


@app.route("/contributors", methods=["GET"])
def contributors():
    contributors = resourcer.Resource.get_all_contributors()
    return render_template(
        "contributors.html", contributors=contributors["contributors"]
    )


@app.route("/filtered_resources", methods=["POST"])
def filtered_resources():
    res_type = request.form.get("type")
    res_level = request.form.get("level")

    rsr = resourcer.Resource(request.form.get("category"))

    if res_level is not None:
        resources = rsr.get_resources_by_level(res_level)
        return render_template("filtered_resources.html", resources=resources)

    elif res_type is not None:
        resources = rsr.get_resources_by_type(res_type)
        return render_template("filtered_resources.html", resources=resources)

    return "Wuba luba dub dub"

if __name__ == "__main__":
    app.run(debug=True)