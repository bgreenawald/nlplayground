from flask import Flask, render_template
app = Flask(__name__, static_url_path='', static_folder='assets',)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sidebar')
def sidebar():
    return render_template('sidebar.html')

@app.route('/header')
def header():
    return render_template('header.html')



# Game routes
@app.route('/games/<name>')
def games(name):
    name_map = {
        "madgab": 'games/madgab.html',
    }

    if name not in name_map:
        return render_template("index.html")
    else:
        return render_template(name_map[name])

# Mix and mash routes
@app.route('/mixmash/<name>')
def mixmash(name):
    name_map = {
        "biblicaltrump": 'mixmash/biblicaltrump.html',
    }

    if name not in name_map:
        return render_template("index.html")
    else:
        return render_template(name_map[name])

# Text generation routes
@app.route('/textgen/<name>')
def textgen(name):
    name_map = {
    }

    if name not in name_map:
        return render_template("index.html")
    else:
        return render_template(name_map[name])

if __name__ == "__main__":
    app.run(debug=True)