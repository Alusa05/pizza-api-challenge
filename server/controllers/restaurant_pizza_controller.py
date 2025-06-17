from flask import Blueprint, jsonify, request
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server import db

restaurant_pizzas_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizzas_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    
    # Validate price
    price = data.get('price')
    if not (1 <= price <= 30):
        return jsonify({'errors': ['Price must be between 1 and 30']}), 400
    
    # Check if restaurant exists
    restaurant = Restaurant.query.get(data.get('restaurant_id'))
    if not restaurant:
        return jsonify({'errors': ['Restaurant not found']}), 404
    
    # Check if pizza exists
    pizza = Pizza.query.get(data.get('pizza_id'))
    if not pizza:
        return jsonify({'errors': ['Pizza not found']}), 404
    
    # Create new RestaurantPizza
    restaurant_pizza = RestaurantPizza(
        price=price,
        restaurant_id=restaurant.id,
        pizza_id=pizza.id
    )
    
    db.session.add(restaurant_pizza)
    db.session.commit()
    
    return jsonify({
        'id': restaurant_pizza.id,
        'price': restaurant_pizza.price,
        'pizza_id': restaurant_pizza.pizza_id,
        'restaurant_id': restaurant_pizza.restaurant_id,
        'pizza': {
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        },
        'restaurant': {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address
        }
    }), 201