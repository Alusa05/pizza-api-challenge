from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object('Config') 

db = SQLAlchemy()
migrate = Migrate()


from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza
     
    

    # Register blueprints
from server.controllers import restaurant_controller
from server.controllers  import pizza_controller
from server.controllers import restaurant_pizza_controller
 
    # Add seed command
@app.cli.command("seed")
def seed_command():
        """Seed the database with sample data."""
        from server.seed import seed_data
        seed_data()
        print("Database seeded successfully!")

   