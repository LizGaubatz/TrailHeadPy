from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_app import app, DB

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.email= data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# ______________
# GET ALL USER INFO
    @classmethod 
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DB).query_db(query)
        return cls(results[0])


# ______________
# GET ONE USER
    @classmethod
    def get_one(cls,**data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query, data)
        return cls(results[0])

# ______________
# REGISTER USER

    @classmethod
    def register(cls, data ):
        query = "INSERT INTO users (first_name, email, password, created_at) VALUES ( %(first_name)s, %(email)s,  %(password)s, NOW());"
        return connectToMySQL(DB).query_db( query, data )

# ______________
# VALIDATE REGISTER USER

    @staticmethod
    def validate_user(user):
        is_Valid = True
        if len(user['first_name']) < 3:
            flash("First name must be at least 3 characters.")
            is_Valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_Valid = False
        if not (user['confirm_password']) == (user['password']):
            flash("Passwords do not match!")
            is_Valid = False
        if not EMAIL_REGEX.match(user['email']): 
            print(user['email'])
            flash("Please enter a valid email address that is not already a user.")
            is_Valid = False
        return is_Valid
    
# ______________
# LOGIN

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DB).query_db(query,data)
        if result:
            return cls(result[0])