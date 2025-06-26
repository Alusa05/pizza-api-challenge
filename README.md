## Project description
Pizza Restaurant API

## Project Author
This project was developed/implemented by Lisa Alusa

## SetUp Instructions
1. Clone the repository:
git clone https://github.com/Alusa05/pizza-api-challenge
cd pizza-api-challenge

2. Set up a virtual environment and install dependencies
pipenv install 
pipenv shell

3. Set up the database:
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

4. Seed the database with sample data:
python server/seed.py

5. Run the application:
flask run


## Database Schema
Restaurant
id: Integer (Primary Key)
name: String (Unique, Not Null)
address: String (Not Null)

Pizza
id: Integer (Primary Key)
name: String (Not Null)
ingredients: String (Not Null)

RestaurantPizza (Join Table)
id: Integer (Primary Key)
price: Integer (Between 1 and 30, Not Null)
restaurant_id: Integer (Foreign Key)
pizza_id: Integer (Foreign Key)

## Technologies used
Python 3
Flask
SQLAlchemy
Flask-Migrate
PostgreSQL/SQLite
Postman (for testing)

## License
This project is under the MIT License
