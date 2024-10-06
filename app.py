from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache   
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flasgger
import Swagger

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

cache = Cache(app, config={'CACHE_TYPE': 'simple'})
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["100 per day"]
)


app.config['SWAGGER'] = {
    'title': 'E-commerce API',
    'uiversion': 3
}
swagger = Swagger(app)

# --- Import Controllers ---
from controllers import customer_controller, product_controller, order_controller

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)