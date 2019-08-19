from flask import Flask, render_template

from api import api
from routes import routes

app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug=True)