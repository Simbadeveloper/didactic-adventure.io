# views.py

from flask import render_template

from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/aboutus')
def aboutus():
    return render_template("Aboutus.html")

@app.route('/signup')
def signup():
    return render_template("register.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/forgetpassword')
def forgetpassword():
    return render_template("forgetpassword.html")

@app.route('/forgetusername')
def forgetusername():
    return render_template("forgetusername.html")

@app.route('/admin')
def admin():
    return render_template("Adminpage.html")

@app.route('/orders')
def orders():
    return render_template("userpagee.html")

@app.route('/approval')
def approval():
     return render_template("approval.html")

@app.route('/user')
def user():
    return render_template("userpage.html")

@app.route('/makeorder')
def makeorder():
    return render_template("order.html")


