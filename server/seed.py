# server/seed.py
import sys
from os.path import dirname, abspath


project_root = dirname(dirname(abspath(__file__)))
sys.path.insert(0, project_root)

from server.app import app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

def seed_data():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Create sample restaurants
        restaurants = [
            Restaurant(name="Pizza Palace", address="123 Main St"),
            Restaurant(name="Italian Bistro", address="456 Oak Ave")
        ]
        
        # Create sample pizzas
        pizzas = [
            Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil"),
            Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")
        ]
        
        db.session.add_all(restaurants + pizzas)
        db.session.commit()
        
        # Create associations
        restaurant_pizzas = [
            RestaurantPizza(price=10, restaurant_id=1, pizza_id=1),
            RestaurantPizza(price=12, restaurant_id=1, pizza_id=2)
        ]
        
        db.session.add_all(restaurant_pizzas)
        db.session.commit()

if __name__ == '__main__':
    seed_data()
    print("Database seeded successfully!")