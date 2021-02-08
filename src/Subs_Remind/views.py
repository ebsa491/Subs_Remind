"""
The routes of the project. (mt`V` pattern)
"""

from Subs_Remind import app
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import (
    render_template,
    request,
    redirect,
    url_for,
)


limiter = Limiter(
    app,
    key_func=get_remote_address,
)


@limiter.limit("15 per 2 minutes")  # For brute force
@app.route('/')
def home():
    return render_template("home/index.html")


@limiter.limit("15 per 2 minutes")  # For brute force
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return redirect(url_for('home'))
    elif request.method == "POST":
        return "POST"

@limiter.limit("15 per 2 minutes")  # For brute force
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
