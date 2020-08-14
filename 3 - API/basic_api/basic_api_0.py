# create application instance
# import 'Flask class/application constructor', & 'jsonify' module
from flask import Flask, jsonify
# pass argument, to determine the location of application, files, images, templates
app = Flask(__name__)

# REGISTER VIEW FUNCTIONS

# METHOD 1: 'app.route decorator' method

@app.route("/") # register handler for application's root URL
def index():
    # return a response with the JSON representation of the given arguments, with the appropriate content-type header 'application/json'
    return jsonify({"about": "Hello World!"}) # returns response to a client(web browser)

# (Programmatically) Development Web Server
if __name__ == '__main__':
    app.run(debug=True)
# Debugger enables 2 modules: 'reloader' & 'debugger'

# (Manual) Development Web Server
# $ $env:FLASK_APP='basic_app.py'
# $ $env:FLASK_DEBUG='1'
# $ flask run --host 0.0.0.0
