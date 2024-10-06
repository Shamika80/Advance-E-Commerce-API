# E-commerce API

This is a RESTful API for an e-commerce application built with Flask and Flask-SQLAlchemy.

## Features

* Customer management (CRUD operations)
* Customer account management with secure password hashing
* Product catalog management (CRUD operations)
* Order placement and retrieval
* JWT authentication with role-based access control
* Caching for improved performance
* Rate limiting for security
* Swagger documentation

## Setup

1. Clone the repository: `git clone <your_github_repository_url>`
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
    * Windows: `venv\Scripts\activate`
    * macOS/Linux: `source venv/bin/activate`   

4. Install dependencies: `pip install -r requirements.txt`   

5. Configure the database connection and other settings in `config.py`
    * Update the `SQLALCHEMY_DATABASE_URI` to connect to your MySQL database.
    * Set a strong secret key for `SECRET_KEY` and `JWT_SECRET_KEY`.
6. Run the app: `python app.py`

## API Documentation

The API documentation is available through Swagger UI: [http://localhost:5000/apidocs](http://localhost:5000/apidocs)

## Project Structure

* `app.py`: Main application file
* `config.py`: Configuration settings
* `controllers/`: API controllers
* `models/`: Database models
* `services/`: Business logic and data access
* `utils/`: Utility functions
* `tests/`: Unit tests

## Running Tests

1. Make sure you have the necessary testing dependencies installed (e.g., `pytest`).
2. Run the tests from the project root directory: `python -m unittest discover`

## Contributing

Feel free to open issues or pull requests if you have any suggestions or improvements.