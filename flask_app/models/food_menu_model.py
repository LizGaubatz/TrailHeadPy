import imp
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app, DB
from flask_app.models import food_item_model
# from flask_app.models import user_model

class Food:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @property
    def item(self):
        print('food')
        data = {
            "food_id": self.id
        }
        return food_item_model.Items.get_items(data)


# ______________
# GET ALL FOOD TYPES
    @classmethod
    def get_food(cls):
        query = "SELECT * FROM food;"
        # query = "SELECT * FROM food LEFT JOIN item ON food.id = item.food_id WHERE food.id = %(food.id)s;"
        results = connectToMySQL(DB).query_db(query)
        food = []
        if results:
            for row in results:
                print(row)
                food.append(cls(row))
        print(food)
        return food


# # ______________
# # GET ALL FOOD TYPES
#     @classmethod
#     def get_food(cls):
#         query = "SELECT * FROM food;"
#         return connectToMySQL(DB).query_db(query)


# ______________
# CREATE A FOOD TYPE
    @classmethod
    def save(cls,data):
        query = "INSERT INTO food ( name ) VALUES ( %(name)s );"
        results = connectToMySQL(DB).query_db(query,data)
        return results

# # ______________
# # UPDATE

    @classmethod
    def edit_food(cls, data):
        query = "UPDATE food SET name = %(name)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data)

    # # ______________
# # DELETE

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM food WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data)

    # # ______________
# # VALIDATE

    @staticmethod
    def validate_food(data):
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