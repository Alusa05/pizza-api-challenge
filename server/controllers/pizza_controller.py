from flask import jsonify
from server import app
from server.models.pizza import Pizza

@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([{
        "id": p.id,
        "name": p.name,
        "ingredients": p.ingredients
     
        }
        for p in pizzas])