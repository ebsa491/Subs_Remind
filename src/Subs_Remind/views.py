"""
The routes of the project. (mt`V` pattern)
"""

from Subs_Remind import app


@app.route('/')
def home():
    return "Home"
