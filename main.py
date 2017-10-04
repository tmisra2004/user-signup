from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)
app.config['DEBUG'] = True

username = ""
password = ""
verify = ""
email = ""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods=['POST'])
def user_signup():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    
    if username == "":
        error = "Please enter a username."
        return error

    if password == "":
        error = "Please enter a password."
        return error

    if len(username) < 3 or len(username) > 20:
        error = "Username must be at least 3 characters but not more than 20 characters."
        return error

    if password != verify:
        error = "Passwords do not match."
        return error

    test = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

    if test == None:
        error = "Please enter a valid email address."
        return error
    
    else:
        return render_template("success.html")

app.run()