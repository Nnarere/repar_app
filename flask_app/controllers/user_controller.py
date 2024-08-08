from flask import Flask, render_template, redirect, request, session, flash

from flask_app import app

from flask_app.models.user import User
from flask_app.models.vehicle import Vehicle

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/", methods=["POST" , "GET"])
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    if not User.validate_user(request.form):
        return redirect("/")
    
    pass_hash = bcrypt.generate_password_hash(request.form["password"])

    form = {
        "full_name": request.form["full_name"],
        "email": request.form["email"], 
        "password": pass_hash
    }

    id = User.save(form) 
    session["user_id"] = id
    return redirect("/")

@app.route("/data", methods=["POST" , "GET"])
def dashboard():
    if "user_id" not in session:
        return redirect("/")
    
    dicc = {"id": session["user_id"]}
    user = User.get_by_id(dicc) 
    return render_template("data.html", user = user) 

@app.route("/access", methods=["POST"])
def login():
    user = User.get_by_email(request.form)

    if not user: 
        flash("E-mail not found", "login")
        return redirect ("/") 
    
    if not bcrypt.check_password_hash(user.password, request.form["password"]):
        flash("Password incorrect", "login")
        return redirect ("/")

    session["user_id"] = user.id
    return redirect ("/data") 

@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect("/")