from flask import Flask, render_template, redirect, request, session, flash

from flask_app import app

from flask_app.models.vehicle import Vehicle
from flask_app.models.user import User

@app.route("/add", methods = ['POST'])
def add_vehicle():
    if not Vehicle.validate_vehicle(request.form):
        return redirect("/data")
    
    Vehicle.save_vehicle(request.form)
    return redirect("/data")

@app.route("/findByPlate", methods=['POST'])
def by_plate():
    if "user_id" not in session:
        return redirect("/")
    
    plate= request.form['plate']
    vehicles = Vehicle.get_vehicle_by_plate(plate)

    dicc = {"id": session["user_id"]}
    user = User.get_by_id(dicc) 
    return render_template('byplate.html', user = user, vehicles = vehicles)

@app.route("/findByVIN", methods=['POST'])
def by_vin():
    if "user_id" not in session:
        return redirect("/")
    
    vin= request.form['vin']
    vehicles = Vehicle.get_vehicle_by_vin(vin)

    dicc = {"id": session["user_id"]}
    user = User.get_by_id(dicc) 
    return render_template("byvin.html", user = user, vehicles = vehicles)

@app.route("/vehicles", methods=['GET'])
def all_vehicles():
    if "user_id" not in session:
        return redirect("/")
    
    vehicles = Vehicle.get_all()
    dicc = {"id": session["user_id"]}
    user = User.get_by_id(dicc) 
    return render_template('vehicles.html', user = user, vehicles = vehicles)