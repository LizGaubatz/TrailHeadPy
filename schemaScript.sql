SELECT * FROM users;
SELECT * FROM food;
SELECT * FROM item WHERE food_id = 1;
SELECT * FROM drink WHERE drinks_id = 1;
SELECT * FROM drink;
SELECT * FROM item;
SELECT * FROM drinks LEFT JOIN drink ON drinks.id = drink.drinks_id WHERE drinks.id = 1;
SELECT * FROM drinks;
SELECT * FROM food LEFT JOIN item ON food.id = item.food_id WHERE food.id = 1;