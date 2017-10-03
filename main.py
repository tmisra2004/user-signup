from flask import Flask, request, redirect, render_template

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
    
    num_ats = 0
    num_dots = 0
    num_spaces = 0

    for char in email:
        if char == "@":
            num_ats += 1
        
        if char == ".":
            num_dots += 1

        if char == " ":
            num_spaces += 1
        
        if num_ats < 1:
            error = "'{0}'E-mail address must contain at least one @ symbol.".format(email)
            return error
        
        if num_ats > 1:
            error = "'{0}'E-mail address must contain no more than one @ symbol.".format(email)
            return error

        if num_dots < 1:
            error = "'{0}'E-mail address must contain at least one . symbol.".format(email)
            return error
        
        if num_dots > 1:
            error = "'{0}'E-mail address must contain no more than one . symbol.".format(email)
            return error

        if num_spaces > 1:
            error = "'{0}'E-mail address must not contain spaces.".format(email)
            return error

    if len(email) < 3 or len(email) > 20:
            error= "'{0}'E-mail address must be between 3 and 20 characters in length.".format(email)
            return error

    else:
            return render_template("success.html")

app.run()