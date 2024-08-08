from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data) :
        self.id = data['id']
        self.full_name = data['full_name']
        self.email = data['email']
        self.password = data['password']

    #metodo de clase crea un nuevo registro
    @classmethod
    def save(cls,form):
        query = 'INSERT INTO user (full_name, email, password) VALUES (%(full_name)s, %(email)s, %(password)s)'
        return connectToMySQL("repartes").query_db(query, form)
    
    #metodo que regresa objeto de usuario en base al email
    @classmethod
    def get_by_email(cls, form):  
        query = "select * from user where email = %(email)s"
        result = connectToMySQL("repartes").query_db(query, form) 

        if len(result) <1: 
            return False
        else:
            user = cls(result[0]) 
            return user
        
    #metodo que valide la info que recibimos del form   
    @staticmethod
    def validate_user(form):
        is_valid = True
        if len(form["full_name"])<2:
            flash("Full name must have at least 2 chars", "register") 
            is_valid = False

        if len(form["password"])<5:
            flash("Password must have at least 5 chars", "register")
            is_valid = False

        query = "select * from user where email = %(email)s"
        result = connectToMySQL("repartes").query_db(query, form)
        
        if len(result) >=1:
            flash("E-mail already registered", "register")
            is_valid = False

        if form["password"] != form["confirm"]: 
            flash("Password do not match", "register")
            is_valid = False

        if not EMAIL_REGEX.match(form["email"]): 
            flash("E-mail not valid", "register")
            is_valid = False

        return is_valid
    
    @classmethod
    def get_by_id(cls, data):  
        query = "select * from user where id = %(id)s"
        result = connectToMySQL("repartes").query_db(query, data) 
        user = cls(result[0])
        return user