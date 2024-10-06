from flask import request, jsonify, Blueprint
from services.customer_service import CustomerService
from utils.auth import token_required

# --- Blueprint (optional) ---
# bp = Blueprint('customer_controller', __name__)

# --- Controller functions ---
# @bp.route('/', methods=['POST'])  # If using blueprints
@app.route('/customers', methods=['POST'])
@token_required(role="admin")
def create_customer(current_user):
    """
    Create a new customer (Admin only)
    ---
    # ... (Swagger documentation)
    """
    # ... (Implementation)

# ... (Other controller functions with Swagger documentation)