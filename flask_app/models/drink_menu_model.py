from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import bcrypt, DB, session
from flask_app.models import drinks_menu_model
# from flask_app.models import user_model
from flask import flash


class Drink:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.small = data['small']
        self.medium = data['medium']
        self.large = data['large']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.drinks_id = data['drinks_id']


    @property
    def drinks(self):
        data = {   
            "id":self.drinks_id
        }
        return drinks_menu_model.Drinks.get_one(**data)


    @classmethod
    def get_all(cls, data) -> list:
        query  = f"""SELECT * FROM drink WHERE drinks_id = %(drinks_id)s;"""
        print(data, 'Hello')
        results = connectToMySQL(DB).query_db(query,data)
        print(results)
        drinks = []
        if results:
            for row in results:
                print(row)
                drinks.append(cls(row))
        print(drinks)
        return drinks


    @classmethod
    def add_drink(cls,data):
        drinks ={
            'name' : data['drinks_id'].lower()
        }
        check = drinks_menu_model.Drinks.get_one(name=data['drinks_id'].lower())
        if not check:
            drinks_menu_model.Drinks.add_drinks(drinks)

        drinks = drinks_menu_model.Drinks.get_one(name=data['drinks_id'].lower())

        drink_data = {
            **data,
            'drinks_id': drinks.id
        }
        query = f"""INSERT INTO drink ({', '.join(f'{key}' for key in drink_data)}) VALUES ({', '.join(f'%({key})s'for key in drink_data)});"""
        results = connectToMySQL(DB).query_db(query, drink_data)
        if results:
            return results 


    @classmethod
    def edit_drink(cls, data, id = None):
        query = f""" UPDATE drink SET { ' , '.join(f' {key} = %({key})s ' for key in data ) } WHERE id = %(id)s ;"""
        data = {
            **data,
            'id' : id
        }
        results = connectToMySQL(DB).query_db(query, data)
        if results:
            return results 



    @classmethod
    def get_one(cls,**data):
        query = """SELECT * FROM drink WHERE drink.id = %(id)s;"""
        results = connectToMySQL(DB).query_db(query,data)
        if results:
            return cls(results[0])


    @classmethod
    def delete_drink(cls,**data):
        query = " DELETE FROM drink WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query,data)


    @staticmethod
    def validate_drink(data):
        print(data)
        is_Valid = True
        if len(data['name']) < 2:
            flash("Name must be greater than 2 characters.")
        return is_Valid
