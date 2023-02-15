from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config["SECRET_KEY"] = "nanashi@7011"

#create a form class
class name_form(FlaskForm):
    name = StringField("what's your Name" , validators=[DataRequired()])
    age = StringField("what's your Age" , validators=[DataRequired()])
    submit = SubmitField("Submit") 



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


@app.route('/name', methods=['GET','POST'])
def name():
    name = None
    age = None
    form = name_form()
    if form.validate_on_submit():
        name =  form.name.data
        age = form.age.data
        form.name.data =  ''
        form.age.data = " "
        
    return render_template("name.html", name = name, form=form, age = age,)