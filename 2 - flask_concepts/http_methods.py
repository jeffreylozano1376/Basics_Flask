from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def home():   
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST": # redirect to 'user' page if 'submit' button...
        user = request.form["nm"] # ...is clicked, plus utilize the input value 
        return redirect(url_for("user", usr=user))
    else: # otherwise, render 'login.html'
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__=="__main__":
    app.run(debug=True)

# HTTP Methods (most common)
# 'get' method is a request to retrieve a specific data(non-secured)
# 'post' method is a request to submit an entity to a specified resource (secure/encrypted)
# 'forms' is a way to send information to a website