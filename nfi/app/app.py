from flask import *
from os import urandom
from html import escape
from subprocess import getoutput
from time import time
import db

dbc = db.Database("db/users.db") # sqlite database connection

app = Flask(__name__)
app.secret_key = "vuctf{4n_unf0rtun4te_ch41n" # Congrats, you got the first part of the flag

sessions = {} # dictionary to contain local session data

def auth(sess_id):
    # Clean up sessions older than 10 minutes
    for current_session in list(sessions):
        if sessions[current_session]["logon_time"] + 600 < int(time()):
            sessions.pop(current_session)
    # Check role of user
    if sess_id in sessions and sessions[sess_id]["role"] == "admin":
        return True
    return False

@app.route("/", methods=["GET"])
def index():
    if (message := request.args.get("message")):
        message = escape(message)
    if session and auth(session["sess_id"]):
        return redirect("/dashboard")
    return render_template("index.html", message=message)

@app.route("/static/<path:path>", methods=["GET"])
def static_file(path):
    return send_from_directory("static", path)

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    logon_time = int(time())
    if (creds := dbc.login((username, password))):
        sess_id = urandom(16).hex()
        session["sess_id"] = sess_id
        new_session = {sess_id: {"username": creds[0], "role": creds[1], "logon_time": logon_time}}
        sessions.update(new_session)
        with open("./logs/authlog.txt", "at") as logfile:
            logfile.write(str(new_session) + "\n")
        print(sessions) # DEBUG
        return redirect("/dashboard")
    else:
        return redirect("/?message=Login Failed")

@app.route("/logout", methods=["GET"])
def logout():
    if session and (sess_id := session["sess_id"]) in sessions:
        sessions.pop(sess_id)
    print(sessions) # DEBUG
    return redirect("/?message=Logged out successfully!")

@app.route("/dashboard", methods=["GET"])
def dashboard():
    if session and auth(session["sess_id"]):
        return render_template("dashboard.html")
    else:
        return redirect("/?message=Not logged in")

@app.route("/tools/<path:path>", methods=["GET"])
def tools(path):
    if session and auth(session["sess_id"]):
        if path == "ping":
            return getoutput("ping -c4 127.0.0.1")
        elif path == 'ip_addr':
            return getoutput("ip addr")
        elif path == "view_logs":
            if (logfile := request.args.get("logfile")):
                return send_file(logfile)
            else:
                return "No logfile specified"
        elif path == "database_check":
            return send_file(db.somepath)
        
    else:
        return redirect("/?message=Not Logged in")

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
