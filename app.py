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
@app.route('/games/madgab')
def madgab():
    return render_template('games/madgab.html')



# Mix and mash routes



# Text generation routes


if __name__ == "__main__":
    app.run(debug=True)