import os

from flask import Flask, render_template, session, request, redirect
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = "my secret key"
socketio = SocketIO(app)

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/signin", methods=['GET','POST'])
def signin():
    ''' Save the username on a Flask session 
    after the user submit the sign in form '''

    if request.method == "POST":
        username = request.form.get("username")

        session["username"] = username

        redirect("/")


    return render_template("signin.html")
