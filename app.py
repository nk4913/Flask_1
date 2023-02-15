from flask import Flask, render_template , flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

app.config["SECRET_KEY"] = "nanashi@7011"


db = SQLAlchemy(app)

#model
class Users(db.Model):

    app.app_context().push()
    id = db.Column(db.Integer, primary_key = True) 
    name = db.Column( db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return '<Name %r>' % self.name

class UserForm(FlaskForm):
    name = StringField("Name" , validators=[DataRequired()])
    email = StringField("Email" , validators=[DataRequired()])
  
    submit = SubmitField("Submit") 
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

@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None :
            user = Users(name=form.name.data, email = form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
        flash('User added successfully')
    our_users = Users.query.order_by(Users.date_added)
    return render_template("add_user.html", form= form, name=name ,our_users= our_users)

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
        flash("Form submitted Successfully")
        
    return render_template("name.html", name = name, form=form, age = age,)