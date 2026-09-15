from functools import wraps
from flask import jsonify
from flask_login import current_user

def role_required(required_role):
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):

            if not current_user.is_authenticated:
                return jsonify({
                    "error" : "Login required!!"
                }), 401

            if current_user.role != required_role:
                return jsonify({
                    "error" : "You are not authorized to access..!!"
                }), 403
            
            return func(*args, **kwargs)
        return decorated_function
    return decorator