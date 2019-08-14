from flask import Blueprint, render_template

routes = Blueprint("routes", __name__, static_url_path='', static_folder='assets',)


# Generic routes
@routes.route('/')
def index():
    return render_template("index.html")

@routes.route('/sidebar')
def sidebar():
    return render_template('sidebar.html')

@routes.route('/header')
def header():
    return render_template('header.html')

@routes.route('/games/<name>')
def games(name):
    name_map = {
        "madgab": 'games/madgab.html',
    }

    if name not in name_map:
        return render_template("index.html")
    else:
        return render_template(name_map[name])


@routes.route('/mixmash/<name>')
def mixmash(name):
    name_map = {
        "biblicaltrump": 'mixmash/biblicaltrump.html',
    }

    if name not in name_map:
        return render_template("index.html")
    else:
        return render_template(name_map[name])


@routes.route('/textgen/<name>')
def textgen(name):
    name_map = {
    }

    if name not in name_map:
        return render_template("index.html")
    else:
        return render_template(name_map[name])
