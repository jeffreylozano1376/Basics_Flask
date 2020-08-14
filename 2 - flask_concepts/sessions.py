from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta


app = Flask(__name__)
# Session Data are normally encrypted on the server; hence 'secret key'
app.secret_key = "aiah" # encrypt/decrypt data
# Set storage duration of Session Data
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True # makes session permanent
        user = request.form["nm"]
        session["user"] = user # stores submitted data by the user as dict key
        flash("Login Successful!")
        return redirect(url_for("user")) 
    else:
        # if already logged-in, redirects to user page
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))
        
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session: # check if session data exists
        user = session["user"] # if valid, retrieves the specific session data
        return render_template("user.html", user=user)
    else: 
        # if invalid (i.e. logged out, expired), redirects to login page
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    flash("You have been logged out!", "info")
    session.pop("user", None) # removes session data of the user
    return redirect(url_for("login"))

if __name__=="__main__":
    app.run(debug=True)

# 'Sessions' allows quick access of information between all the different pages of a website.  It loads while a user is currently in a website, and terminates when the user leaves.
