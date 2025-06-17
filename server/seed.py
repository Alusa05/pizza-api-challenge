from server import app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

with app.app_context():
    # Clear existing data
    db.drop_all()
    db.create_all()

    # Create restaurants
    restaurant1 = Restaurant(name="Pizza Palace", address="123 Main St")
    restaurant2 = Restaurant(name="Italian Bistro", address="456 Oak Ave")
    restaurant3 = Restaurant(name="Slice House", address="789 Pine Rd")

    # Create pizzas
    pizza1 = Pizza(name="Margherita", ingredients="Tomato sauce, Mozzarella, Basil")
    pizza2 = Pizza(name="Pepperoni", ingredients="Tomato sauce, Mozzarella, Pepperoni")
    pizza3 = Pizza(name="Vegetarian", ingredients="Tomato sauce, Mozzarella, Bell peppers, Mushrooms")

    # Add to session
    db.session.add_all([restaurant1, restaurant2, restaurant3, pizza1, pizza2, pizza3])
    db.session.commit()

    # Create restaurant_pizzas
    rp1 = RestaurantPizza(price=10, restaurant_id=1, pizza_id=1)
    rp2 = RestaurantPizza(price=12, restaurant_id=1, pizza_id=2)
    rp3 = RestaurantPizza(price=15, restaurant_id=2, pizza_id=1)
    rp4 = RestaurantPizza(price=14, restaurant_id=2, pizza_id=3)
    rp5 = RestaurantPizza(price=11, restaurant_id=3, pizza_id=2)
    rp6 = RestaurantPizza(price=13, restaurant_id=3, pizza_id=3)

    db.session.add_all([rp1, rp2, rp3, rp4, rp5, rp6])
    db.session.commit()

    print("Database seeded successfully!")