from server import app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

def seed_data():
    # Clear existing data
    db.drop_all()
    db.create_all()

    # Sample data for Restaurants
    restaurants = [
        Restaurant(name= "Pizza Palace", address="123 Main St", phone="123-456-7890"),
        Restaurant(name="Italian Bistro ", address="456 Elm St", phone="987-654-3210"),
        Restaurant(name="Slice of Heaven", address="789 Oak St", phone="555-555-5555"),
    ]

    pizzas = [
        Pizza(name="Margherita", ingredients= "Tomato sauce, Mozzarella, Basil"),
        Pizza(name="Pepperoni", ingredients="Tomato sauce, Mozzarella, Pepperoni"),
        Pizza(name="Vegetarian", ingredients="Tomato sauce, Mozzarella, Bell peppers, Onions, Mushrooms")
    ]

    db.session.add_all(restaurants + pizzas)
    db.session.commit()

    