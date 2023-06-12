#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template, url_for
app = Flask(__name__, static_folder='static')

"""
nav bar
"""


def get_navigation_data():
    return [
            {"url": "/", "label": "Home", "title": "HOME"},
            {"url": "/blog", "label": "Blog", "title": "BLOG"},
            {"url": "/courses", "label": "Courses", "title": "COURSES"},
            {"url": "/about", "label": "About", "title": "ABOUT"},
            {"url": "/contact", "label": "Contact", "title": "CONTACT"},
            ]


@app.route('/home', strict_slashes=False)
@app.route('/', strict_slashes=False)
def index():
    nav_data = get_navigation_data()
    return render_template("index.html", nav_data=nav_data)


@app.route('/blog', strict_slashes=False)
def blog():
    nav_data = get_navigation_data()
    return render_template("index.html", nav_data=nav_data)


@app.route('/courses', strict_slashes=False)
def courses():
    nav_data = get_navigation_data()
    return render_template("index.html", nav_data=nav_data)


@app.route('/about', strict_slashes=False)
def about():
    nav_data = get_navigation_data()
    return render_template("index.html", nav_data=nav_data)


@app.route('/contact', strict_slashes=False)
def contact():
    nav_data = get_navigation_data()
    return render_template("index.html", nav_data=nav_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
