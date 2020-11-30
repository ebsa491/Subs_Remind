"""
Have you ever forgotten your subscribing payments? This website is yours!
"""

from flask import Flask

app = Flask(__name__)


def import_views():
    """This function imports the routes from `views.py`
    """
    import Subs_Remind.views
    print(f"[\033[1;32m+\033[0m] {Subs_Remind.views.__name__} detected...")


import_views()


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=False)
