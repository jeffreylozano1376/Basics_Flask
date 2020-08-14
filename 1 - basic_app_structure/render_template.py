from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<car>')
def home(car):          # (html file, parameters...)        
    return render_template("index.html", content=car, number=99, names=["jeff","ken", "joe"])
# 'render_template' takes an html file as first argument. Any additional arguments are key-value pairs that represent actual values for variables referenced in the template

if __name__=="__main__":
    app.run(debug=True)



