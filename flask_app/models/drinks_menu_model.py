from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app, DB
# from flask_app.models import user_model
from flask_app.models import drink_menu_model


class Drinks:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    @property
    def drink(self):
        print('drinks')
        data = {
            "drinks_id": self.id
        }
        return drink_menu_model.Drink.get_all(data)


# ______________
# GET ALL FOOD TYPES
    @classmethod
    def get_drinks(cls):
        query = "SELECT * FROM drinks;"
        results = connectToMySQL(DB).query_db(query)
        drinks = []
        if results:
            for row in results:
                print(row)
                drinks.append(cls(row))
        print(drinks)
        return drinks


# ______________
# CREATE A FOOD TYPE
    @classmethod
    def save(cls,data):
        query = "INSERT INTO drinks ( name ) VALUES ( %(name)s );"
        results = connectToMySQL(DB).query_db(query,data)
        return results

# # ______________
# # UPDATE

    @classmethod
    def edit_drinks(cls, data):
        query = "UPDATE drinks SET name = %(name)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data)

    # # ______________
# # DELETE

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM drinks WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data)

    # # ______________
# # VALIDATE

    @staticmethod
    def validate_drinks(data):
        print(data)
        is_Valid = True
        # if data['price'].isdigit():
        #     if int(data['price']) <= 0:
        #         flash("Price must be greater than 0.")
        #         is_Valid = False
        # else:
        #     flash('Please enter a valid price.')
        #     is_Valid = False
        if len(data['name']) < 2:
            flash("Name must be greater than 2 characters.")
        # if len(data['description']) < 0:
        #     flash("Description must be greater than 0 characters.")
        return is_Valid

# # ______________



    # @property
    # def drink(self):
    #     print('drinks')
    #     return drink_menu_model.Drink.get_all(drinks_id = self.id)

    # @classmethod
    # def get_all(cls):
    #     # query = "SELECT drink.id, drink.name, drink.small, drink.medium, drink.large, drink.description FROM drinks LEFT JOIN drink ON drinks.id = $(drink.drinks_id)s WHERE drinks.id = %(drinks.id)s;"
    #     query = "SELECT * FROM drinks;"
    #     results = connectToMySQL(DB).query_db(query)

    #     # drinks = []
    #     # if results:
    #     #     for row in results:
    #     #         drinks.append(cls(row))
    #     #     print('get all drinks')
    #     # return drinks

    #     # results = connectToMySQL(DB).query_db(query)


    #     drinks = []
    #     if results:
    #         for row in results:
    #             one = cls(row)
    #             drink_data = {
    #                 **row,
    #                 "id": row['id'],
    #                 "name": row['name'],
    #                 "small": row['small']
    #             }
    #             one.drink = drink_menu_model.Drink(drink_data)
    #             drinks.append(one)
    #         print('get all drinks')
    #     return [cls(row) for row in results]
    #     # return drinks

    # @classmethod
    # def get_one(cls, **data):
    #     query = f""" SELECT * FROM drinks WHERE {', '.join(f'{key} = %({key})s' for key in data)}"""
    #     results = connectToMySQL(DB).query_db(query, data)
    #     if results:
    #         return cls(results[0])

    # @classmethod
    # def add_drinks(cls, data):
    #     query = 'INSERT INTO drinks (name) VALUES (%(name)s)'
    #     results = connectToMySQL(DB).query_db(query, data)

    # @classmethod
    # def delete_drinks(cls,**data):
    #     query = " DELETE FROM drinks WHERE id = %(id)s;"
    #     results = connectToMySQL(DB).query_db(query,data)

    # @staticmethod
    # def validate_drinks(data):
    #     print(data)
    #     is_Valid = True
    #     if len(data['name']) < 2:
    #         flash("Name must be greater than 2 characters.")
    #     return is_Valid
