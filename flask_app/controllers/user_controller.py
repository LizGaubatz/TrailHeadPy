from flask import render_template, redirect, request, session, flash
from werkzeug import datastructures
from flask_app import app, bcrypt
from flask_app.models.user_model import User

# ______________
# REGISTER USER

@app.route('/register')
def index():
    return render_template("register.html")

@app.post('/register/user')
def register():
    if not User.validate_user(request.form):
        print('banana')
        return redirect('/register')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "first_name": request.form['first_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    user = User.register(data)
    session['user'] = user
    print(user)
    return redirect("/login")

# ______________
# LOGIN

@app.route('/login')
def login():
    return render_template("login.html")

@app.post('/user/login')
def user_login():
    data = { "email" : request.form["email"] }
    user = User.get_by_email(data)
    if not user:
        flash("Invalid Email/Password")
        return redirect("/login")
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/login')
    session['user'] = user.id
    return redirect("/")

# ______________
# LOGOUT

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# ______________
