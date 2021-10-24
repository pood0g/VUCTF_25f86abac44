from flask import *
from os import urandom
import db

dbc = db.Database("db/users.db")

app = Flask(__name__)
app.secret_key = urandom(32)


@app.route("/", methods=["GET", "POST"])
def root():
    if request.method == "POST":
        search = request.form['user']
        results = dbc.search_user(table="users", return_columns="*", where_like=("username", search))
        if len(results) > 0:
            return render_template("index.html", results=results)
        else:
            return render_template("index.html", no_results=True)
    else:
        return render_template("index.html")

@app.route("/static/<path:path>")
def static_file(path):
    return send_from_directory("static", path)