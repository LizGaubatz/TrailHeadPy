from flask import render_template, redirect, request, session, flash
from werkzeug import datastructures
from flask_app import app, bcrypt
from flask_app.models.drink_menu_model import Drink
from flask_app.models.drinks_menu_model import Drinks
from flask_app.models.food_menu_model import Food
from flask_app.models.food_item_model import Items
from flask_app.models.user_model import User


# ______________
# HOME

@app.route('/')
def home():
    return render_template("home.html")

# ______________
# MENU

@app.route('/menu')
def menu():
    food = Food.get_food()
    # items = Items.get_items()
    drinks = Drinks.get_drinks()
    # drink = Drink.get_all()
    return render_template('menu.html', food=food, drinks=drinks)

# ______________
# ABOUT US

@app.route('/about/us')
def about_us():
    return render_template("about_us.html")

    # ______________
# REVIEW

@app.route('/review')
def review():
    return render_template("review.html")

    # ______________
# CONTACT US

@app.route('/contact')
def contact():
    return render_template("contact.html")

# ______________
# NEW

# Food Category
@app.post('/food/new')
def create_food():
    if 'user' not in session:
        return redirect('/menu')
    if not Food.validate_food(request.form):
        print('hello')
        return redirect('/menu')
    data = {
        'name': request.form['name']
    }
    food = Food.save(data)
    print(food)
    return redirect('/menu')

# Food Item
@app.post('/item/new')
def create_item():
    if 'user' not in session:
        return redirect('/menu')
    if not Items.validate_item(request.form):
        print('hello')
        return redirect('/menu')
    data = {
        'food_id': request.form['food_id'],
        'name': request.form['name'],
        'price': request.form['price'],
        'description': request.form['description'],
    }
    item = Items.save(data)
    print(item)
    return redirect('/menu')

# Drink Category
@app.post('/drinks/new')
def create_drinks():
    if 'user' not in session:
        return redirect('/menu')
    if not Drinks.validate_drinks(request.form):
        print('hello')
        return redirect('/menu')
    data = {
        'name': request.form['name']
    }
    drinks = Drinks.add_drinks(data)
    print(drinks)
    return redirect('/menu')

    # Drink
@app.post('/drink/new')
def create_drink():
    if 'user' not in session:
        return redirect('/menu')
    if not Drink.validate_drink(request.form):
        print('hello')
        return redirect('/menu')
    data = {
        'drinks_id': request.form['drinks_id'],
        'name': request.form['name'],
        'small': request.form['small'],
        'medium': request.form['medium'],
        'large': request.form['large'],
        'description': request.form['description'],
    }
    drink = Drink.add_drink(data)
    print(drink)
    return redirect('/menu')

# ______________
# EDIT

# Food Category
@app.post('/edit/food/<int:id>')
def edit_food(id):
    if 'user' not in session:
        return redirect('/')
    if not Food.validate_food(request.form):
        return redirect('/menu')
    data = {
        'id':id,
        'name': request.form['name'],
    }
    food = Food.edit_food(data)
    print(food)
    return redirect('/menu')

# Food Item
@app.post('/edit/item/<int:id>')
def edit_item(id):
    if 'user' not in session:
        return redirect('/')
    if not Items.validate_item(request.form):
        return redirect('/menu')
    data = {
        'id':id,
        'food_id': request.form['food_id'],
        'name': request.form['name'],
        'price': request.form['price'],
        'description': request.form['description'],
    }
    item = Items.edit_item(data)
    print(item)
    return redirect('/menu')

    # Drink Category
@app.post('/edit/drinks/<int:id>')
def edit_drinks(id):
    if 'user' not in session:
        return redirect('/')
    if not Drinks.validate_drinks(request.form):
        return redirect('/menu')
    data = {
        'id':id,
        'name': request.form['name'],
    }
    drinks = Drinks.edit_drinks(data)
    print(drinks)
    return redirect('/menu')

    # Drink
@app.post('/edit/drink/<int:id>')
def edit_drink(id):
    if 'user' not in session:
        return redirect('/')
    if not Drink.validate_drink(request.form):
        return redirect('/menu')
    data = {
        'id':id,
        'drinks_id': request.form['drinks_id'],
        'name': request.form['name'],
        'small': request.form['small'],
        'medium': request.form['medium'],
        'large': request.form['large'],
        'description': request.form['description'],
    }
    drink = Drink.edit_drink(data)
    print(drink)
    return redirect('/menu')

# ______________
# DELETE

@app.route('/delete/<int:id>')
def delete(id):
    if 'user' not in session:
        return redirect('/menu')
    data = {
        'id':id
    }
    Items.delete(data)
    return redirect('/menu')
