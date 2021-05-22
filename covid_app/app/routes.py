from flask import render_template, url_for, Blueprint, redirect


routes = Blueprint("routes", __name__, static_folder="static", template_folder="templates")

@routes.route("/")
def index():
    return render_template("index.html")
# 

@routes.route("/country")
def country():
    return render_template("country.html")

# @routes.route("/hell")
# def hell():
    # return redirect(url_for("home"))