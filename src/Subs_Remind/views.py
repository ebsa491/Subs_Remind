"""
The routes of the project. (mt`V` pattern)
"""

from Subs_Remind import app
from flask import render_template


@app.route('/')
def home():
    return render_template("home/index.html")


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard/index.html")


@app.route('/dashboard/new')
def new():
    return render_template("new/index.html")


@app.route('/dashboard/edit')
def edit():
    return render_template("new/index.html")
