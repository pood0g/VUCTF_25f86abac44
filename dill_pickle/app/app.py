from sqlite3.dbapi2 import Error
from flask import *
from os import urandom
import pickle
from base64 import urlsafe_b64encode, urlsafe_b64decode
import binascii
from hashlib import sha256

from werkzeug.wrappers import response
import db

dbc = db.Database("db/users.db")

app = Flask(__name__)
app.secret_key = urandom(32)


@app.route("/", methods=["GET"])
def root():
    if request.method == "GET":
        message = request.args.get("message")
        print(message)
        return render_template("index.html", message=message)

@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        resp = make_response(redirect("/database"))
        resp.set_cookie("auth", urlsafe_b64encode(pickle.dumps({"username": username, "password": password})))
        return resp



@app.route("/database", methods=["GET", "POST"])
def database():
    if not (cookie := request.cookies.get("auth")):
        return redirect("/?message=Not Logged In")
    try:
        cookie = pickle.loads(urlsafe_b64decode(cookie))
    except binascii.Error:
        return redirect("/?message=Nice try, you are on the right path.")
    if (creds := dbc.login((cookie["username"], sha256(cookie["password"].strip().encode()).hexdigest()))):
        if creds[4] == "admin":
            if request.method == "POST":
                search = request.form['user']
                results = dbc.search_user(table="users", return_columns="*", where_like=("username", search))
                if len(results) > 0:
                    return render_template("database.html", results=results)
                elif "'" in search or '"' in search:
                    return render_template("database.html", message="Hacking attempt detected.")
                else:
                    return render_template("database.html", message="No Results")
            else:
                return render_template("database.html")
        else:
            return redirect("/?message=Admin Users Only")
    else:
        return redirect("/?message=Login Failed")

@app.route("/static/<path:path>")
def static_file(path):
    return send_from_directory("static", path)
