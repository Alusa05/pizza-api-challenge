from server import create_app, db
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)

# Import models after app creation to avoid circular imports
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

# Import and register blueprints
from server.controllers.restaurant_controller import restaurants_bp
from server.controllers.pizza_controller import pizzas_bp
from server.controllers.restaurant_pizza_controller import restaurant_pizzas_bp

app.register_blueprint(restaurants_bp)
app.register_blueprint(pizzas_bp)
app.register_blueprint(restaurant_pizzas_bp)

@app.route('/')
def home():
    return "Welcome to the Pizza Restaurant API!"