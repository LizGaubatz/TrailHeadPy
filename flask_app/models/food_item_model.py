from flask_app.config.mysqlconnection import connectToMySQL
from unittest import result
from flask import flash
from flask_app import app, DB
from flask_app.models import food_menu_model

class Items:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.price = data['price']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.food_id = data['food_id']


    @property
    def food(self):
        data = {   
            "id":self.food_id
        }
        return food_menu_model.Food.get_food(**data)


    @classmethod
    def get_items(cls, data) -> list:
        query  = f"""SELECT * FROM item WHERE food_id = %(food_id)s;"""
        print(data, 'Hello')
        results = connectToMySQL(DB).query_db(query,data)
        print(results)
        food = []
        if results:
            for row in results:
                print(row)
                food.append(cls(row))
        print(food)
        return food


# # ______________
# # GET ALL MENU ITEMS
#     @classmethod
#     def get_items(cls):
#         query = "SELECT * FROM item WHERE food_id = 1;"
#         results = connectToMySQL(DB).query_db(query)
#         return results


# ______________
# CREATE AN ITEM
    @classmethod
    def save(cls,data):
        query = "INSERT INTO item ( food_id, name, price, description) VALUES ( %(food_id)s, %(name)s, %(price)s, %(description)s);"
        results = connectToMySQL(DB).query_db(query,data)
        return results

# # ______________
# # UPDATE AN ITEM

    @classmethod
    def edit_item(cls, data):
        query = "UPDATE item SET name = %(name)s, price = %(price)s, description = %(description)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data)

    # # ______________
# # DELETE

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM item WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data)

    # # ______________
# # VALIDATE

    @staticmethod
    def validate_item(data):
        print(data)
        is_Valid = True
        if data['price'].isdigit():
            if int(data['price']) <= 0:
                flash("Price must be greater than 0.")
                is_Valid = False
        else:
            flash('Please enter a valid price.')
            is_Valid = False
        if len(data['name']) < 2:
            flash("Name must be greater than 2 characters.")
        if len(data['description']) < 0:
            flash("Description must be greater than 0 characters.")
        return is_Valid

# # ______________