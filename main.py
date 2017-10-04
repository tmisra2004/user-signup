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

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""
    
    if username == "":
        username_error = "Please enter a username."
    
    if len(username) <= 3 or len(username) > 20:
        username_error = "Username must be at least 3 characters but not more than 20 characters."
        

    if password == "":
        password_error = "Please enter a password."

    if len(password) < 3 or len(password) > 20:
        password_error = "Password must be at least 3 characters but no more than 20 characters long."

    if " " in username:
        username_error = "Username cannot contain spaces."

    if " " in password:
        password_error = "Password cannot contain spaces."
    
    if verify == "" or verify != password:
        verify_error = "Passwords do not match."
        

    if email != "":
        
        if not re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email):
            email_error = "Please enter a valid email address."
       
    
    if not username_error and not password_error and not verify_error and not email_error:
        return render_template("success.html", username = username)

    else:
        return render_template(
            "index.html",
            username = username,
            username_error = username_error,
            password_error = password_error,
            verify_error = verify_error,
            email = email,
            email_error = email_error
        )

app.run()