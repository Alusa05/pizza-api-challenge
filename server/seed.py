from server import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    # Clear existing data
    db.drop_all()
    db.create_all()

    # Create restaurants
    restaurants = [
        Restaurant(name="Pizza Palace", address="123 Main St"),
        Restaurant(name="Italian Bistro", address="456 Oak Ave"),
        Restaurant(name="Slice of Heaven", address="789 Pine Rd")
    ]
    db.session.add_all(restaurants)
    db.session.commit()

    # Create pizzas
    pizzas = [
        Pizza(name="Margherita", ingredients="Tomato sauce, mozzarella, basil"),
        Pizza(name="Pepperoni", ingredients="Tomato sauce, mozzarella, pepperoni"),
        Pizza(name="Vegetarian", ingredients="Tomato sauce, mozzarella, bell peppers, mushrooms, onions")
    ]
    db.session.add_all(pizzas)
    db.session.commit()

    # Create restaurant pizzas
    restaurant_pizzas = [
        RestaurantPizza(price=10, pizza_id=1, restaurant_id=1),
        RestaurantPizza(price=12, pizza_id=2, restaurant_id=1),
        RestaurantPizza(price=15, pizza_id=3, restaurant_id=2),
        RestaurantPizza(price=8, pizza_id=1, restaurant_id=3),
        RestaurantPizza(price=11, pizza_id=2, restaurant_id=3)
    ]
    db.session.add_all(restaurant_pizzas)
    db.session.commit()

    print("Database seeded successfully!")