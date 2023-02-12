from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about.html')
def about():
    return render_template("about.html")


@app.route('/contactus.html')
def contact_us():
    return "<h1>Hello fellow users</h1>"


@app.errorhandler(404)
def page_error(e):
    return render_template("404.html"), 404
