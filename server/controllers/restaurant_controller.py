from flask import request, jsonify
from server.app import app, db
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{
        "id": r.id,
        "name": r.name,
        "address": r.address,
    }
    for r in restaurants])

@app.route('/restauran',  methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    
    pizzas = [{
        "id": rp.pizza.id,
        "name": rp.pizza.name,
        "ingredients": rp.pizza.ingredients,
        "price": rp.price
    } for rp in restaurant.restaurant_pizzas]
    return jsonify({
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address,
        "pizzas": pizzas
    })
    