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

