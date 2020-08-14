from flask import Flask, redirect, url_for

# create instance of flask web application
app = Flask(__name__)

# # ALTERNATIVE ROUTING
# def home():
#     return "Hello! this is the main page <h1>HELLO<h1>"
# app.add_url_rule('/', 'home', home)

# ROUTING (Register View Functions)
@app.route('/') # decorator(path)
def home(): # home page
    return "Hello! this is the main page <h1>HELLO<h1>"
# dynamic route
@app.route('/<name>') # decorator(path/<parameter>)
def user(name): 
    return f"Hello {name}!"

@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="Admin!")) # redirect to specified View Function 

# (programatically) Development Web Server
if __name__=="__main__":
    app.run(debug=True)
# Enables 2 modules: 'reloader' & 'debugger'

# (manual) Development Web Server
# $ $env:FLASK_APP='basic_app.py'
# $ $env:FLASK_DEBUG='1'
# $ flask run --host 0.0.0.0


