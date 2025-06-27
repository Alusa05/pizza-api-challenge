from flask import Blueprint, jsonify, request
from server.models import RestaurantPizza, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza

restaurant_pizzas_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizzas_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    
    # Validate price
    price = data.get('price')
    if not (1 <= price <= 30):
        return jsonify({'errors': ['Price must be between 1 and 30']}), 400
    
    # Check if restaurant and pizza exist
    restaurant = Restaurant.query.get(data.get('restaurant_id'))
    pizza = Pizza.query.get(data.get('pizza_id'))
    
    if not restaurant or not pizza:
        return jsonify({'errors': ['Restaurant or Pizza not found']}), 400
    
    # Create new RestaurantPizza
    try:
        rp = RestaurantPizza(
            price=price,
            pizza_id=pizza.id,
            restaurant_id=restaurant.id
        )
        db.session.add(rp)
        db.session.commit()
        
        return jsonify({
            'id': rp.id,
            'price': rp.price,
            'pizza_id': rp.pizza_id,
            'restaurant_id': rp.restaurant_id,
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
    except Exception as e:
        db.session.rollback()
        return jsonify({'errors': [str(e)]}), 400