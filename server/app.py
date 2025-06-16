from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('server.config.Config')
    
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
       
        
        db.create_all()

        from server.controllers.restaurant_controller import restaurant_bp
        from server.controllers.pizza_controller import pizza_bp
        from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp

        app.register_blueprint(restaurant_bp)
        app.register_blueprint(pizza_bp)
        app.register_blueprint(restaurant_pizza_bp)

    @app.cli.command("seed")
    def seed_command():
        from server.seed import seed_data
        seed_data()
        print("Database seeded successfully!")

    return app

app = create_app()