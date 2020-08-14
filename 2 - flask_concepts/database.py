from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "aiah"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # also removes warning
app.permanent_session_lifetime = timedelta(minutes=5)
# database object
db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True) # unique indentification
    name = db.Column(db.String(100)) # sets variable as default name
    email = db.Column(db.String(100))
    # takes the variables to create a new object
    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        
        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit()
        
        flash("Login Successful!")
        return redirect(url_for("user")) 
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))
        
        return render_template("login.html")

@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        # check the current method if the user is in session
        if request.method == "POST":
            email = request.form["email"] # gets value('email') in email field
            session["email"] = email # stores value('email') in a session
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash("Email was saved!")
        else: # if request is not POST
            if "email" in session:
                email = session["email"] # GETS email from session
        return render_template("user.html", email=email)
    else: 
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    flash("You have been logged out!", "info")
    session.pop("user", None)
    session.pop("email", None) # 'pops' session on logout
    return redirect(url_for("login"))

if __name__=="__main__":
    db.create_all()
    app.run(debug=True)
