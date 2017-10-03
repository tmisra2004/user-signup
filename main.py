from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

username = ""
password = ""
verify = ""
email = ""

@app.route("/")
def index():
    content = """
    <!DOCTYPE html>

<html>
    <head>
        <style>
            .error {
                color: red;
            }
        </style>
    </head>
    <body>
    <h1>Signup</h1>
        <form method="post">
            <table>
                <tr>
                    <td><label for="username">Username</label></td>
                    <td>
                        <input name="username" type="text" value="">
                        <span class="error"></span>
                    </td>
                </tr>
                <tr>
                    <td><label for="password">Password</label></td>
                    <td>
                        <input name="password" type="password">
                        <span class="error"></span>
                    </td>
                </tr>
                <tr>
                    <td><label for="verify">Verify Password</label></td>
                    <td>
                        <input name="verify" type="password">
                        <span class="error"></span>
                    </td>
                </tr>
                <tr>
                    <td><label for="email">Email (optional)</label></td>
                    <td>
                        <input name="email" value="">
                        <span class="error"></span>
                    </td>
                </tr>
            </table>
            <input type="submit">
        </form>
    </body>
</html>
"""
    return content

@app.route("/", methods=['POST'])
def user_signup():
    username = request.form['username']
    if username == "":
        error = "'{0}'Please enter a username.".format(username)
        return error

    if username.length < 3 or username.length > 20:
        error = "'{0}'Username must be at least 3 characters but not more than 20 characters.".format(username)
        return error

    if password != verify:
        error = "'{0}'Passwords do not match.".format(password)
        return error
    
    num_ats = 0
    num_dots = 0
    num_spaces = 0

    for char in email:
        if char == "@":
            num_ats+=1
        
        if char == ".":
            num_dots+=1

        if char = =" ":
            num_spaces+=1
        
        if num_ats < 1:
            error = "'{0}'E-mail address must contain at least one @ symbol.".format(email)
            return error
        
        if num_ats > 1:
            error = "'{0}'E-mail address must contain no more than one @ symbol.".format(email)
            return error

        if num_dots < 1:
            error = "'{0}'E-mail address must contain at least one . symbol.".format(email)
            return error
        
        if num dots > 1:
            error = "'{0}'E-mail address must contain no more than one . symbol.".format(email)
            return error

        if num_spaces > 1:
            error = "'{0}'E-mail address must not contain spaces.".format(email)
            return error

        if email.length < 3 or email.length > 20:
            error= "'{0}'E-mail address must be between 3 and 20 characters in length.".format(email)

        else:
            return render_template("success.html")

app.run()