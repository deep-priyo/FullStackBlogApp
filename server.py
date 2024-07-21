from flask import Flask, render_template
import requests
import datetime
app = Flask(__name__)


@app.route("/")
def home():
    url="https://api.npoint.io/674f5423f73deab1e9a7"
    all_posts=requests.get(url).json()
    return render_template("index.html",posts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")



if __name__ == "__main__":
    app.run(debug=True)
