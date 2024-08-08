from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

from flask_app.models.user import User

class Vehicle:
    def __init__(self, data):
        self.id = data['id']
        self.plate = data['plate']
        self.country = data['country']
        self.model = data['model']
        self.version = data['version']
        self.displacement = data['displacement']
        self.year = data['year']
        self.vin = data['vin']
        self.motor_number = data['motor_number']
        self.brand_name = data['brand_name']
        self.user_id = data["user_id"]

    @classmethod
    def save_vehicle(cls, form):
        query = "INSERT INTO vehicle (plate, country, model, version, displacement, year, vin, motor_number, brand_name, user_id) VALUES (%(plate)s, %(country)s, %(model)s, %(version)s, %(displacement)s, %(year)s, %(vin)s, %(motor_number)s, %(brand_name)s, %(user_id)s)"
        return connectToMySQL("repartes").query_db(query, form)
    
    @classmethod
    def get_vehicle_by_plate(cls, plate):
        query = "SELECT * FROM vehicle WHERE plate = %(plate)s"
        data = {'plate': plate}
        results = connectToMySQL("repartes").query_db(query, data)
        vehicles = [cls(vehicle) for vehicle in results]
        return vehicles
      
    @classmethod
    def get_vehicle_by_vin(cls, vin):
        query = "SELECT * FROM vehicle WHERE vin = %(vin)s"
        data = {'vin': vin}
        results = connectToMySQL("repartes").query_db(query, data)
        vehicles = [cls(vehicle) for vehicle in results]
        return vehicles
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM vehicle ORDER BY plate ASC"
        results = connectToMySQL("repartes").query_db(query)
        vehicles = []
        for vehicle in results:
            vehicles.append(cls(vehicle))
        return vehicles

    @staticmethod
    def validate_vehicle(form):
        is_valid = True

        if len(form["plate"])<5:
            flash("Plate must have 6 characters at least","add_vehicle")
            is_valid = False

        if len(form["model"])<1:
            flash("Model is required","add_vehicle")
            is_valid = False

        if len(form["version"])<1:
            flash("Version is required","add_vehicle")
            is_valid = False

        if len(form["displacement"])<1:
            flash("Displacement is required","add_vehicle")
            is_valid = False 

        if len(form["year"])<4:
            flash("Year must have 4 number","add_vehicle")
            is_valid = False

        if len(form["vin"])<4:
            flash("Vin is required","add_vehicle")
            is_valid = False

        if len(form["motor_number"])<4:
            flash("Motor_number is required","add_vehicle")
            is_valid = False            

        return is_valid
