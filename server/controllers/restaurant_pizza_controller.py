from flask import jsonify, request
from server import app, db
from server.models.restaurant_pizza import RestaurantPizza

@app.route('/restaurant_pizzas', methods=['POST'])

def create_restaurant_pizza():
    data = request.get_json()

    try:
        rp = RestaurantPizza(
            price=data['price'],
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
        db.session.add(rp)
        db.session.commit()

        pizza = rp.pizza
        restaurant = rp.restaurant

        return jsonify({
            "id": rp.id,
            "price": rp.price,
            "pizza": {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients
            },
            "restaurant": {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address
            }
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400