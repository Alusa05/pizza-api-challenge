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

        