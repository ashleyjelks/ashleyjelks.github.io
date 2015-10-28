from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
import secrets


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined


@app.route('/', methods=['GET'])
def view_index():

   """Route to view drafts of github.io page"""

    return render_template("index.html")




if __name__ == "__main__":
    app.debug = False
    DebugToolbarExtension(app)
    app.run()