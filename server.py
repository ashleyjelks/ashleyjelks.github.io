from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined


@app.route('/', methods=['GET'])
def homepage():

    """Wanderlust Homepage. Users can register for an account, login, or simply search flights."""

    return render_template("index.html")




if __name__ == "__main__":
    app.debug = True
    DebugToolbarExtension(app)
    app.run()