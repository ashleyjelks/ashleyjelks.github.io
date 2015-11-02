from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
import os


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.secret_key = os.environ["SECRET_KEY"]


@app.route('/', methods=['GET'])
def view_index():

    return render_template("index.html")




if __name__ == "__main__":
    app.debug = False
    DebugToolbarExtension(app)
    app.run()