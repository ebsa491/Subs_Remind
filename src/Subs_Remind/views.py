"""
The routes of the project. (mt`V` pattern)
"""

from Subs_Remind import app
from flask import (
    render_template,
    request,
    redirect,
    url_for,
)


@app.route('/')
def home():
    return render_template("home/index.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return redirect(url_for('home'))
    elif request.method == "POST":
        return "POST"


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return redirect(url_for('home'))
    elif request.method == "POST":
        return "POST"


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard/index.html")


@app.route('/dashboard/new')
def new():
    return render_template("new/index.html")


@app.route('/dashboard/edit')
def edit():
    return render_template("new/index.html")


@app.errorhandler(404)
def error_404(err):
    return render_template("error/404.html"), 404
