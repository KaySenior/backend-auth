from flask import jsonify
from flask_login import login_required, current_user
from app.main import main_bd
from app.models import User
from app.auth.decorators import role_required

@main_bd.route("/users", methods=["GET"])
@login_required
@role_required("admin")
def get_all_users():
    users = User.query.all()
    return jsonify([{
        "id" : usr.id,
        "username" : usr.username,
        "role" : usr.role
    } for usr in users
    ])

@main_bd.route("/user-info", methods=["GET"])
@login_required
def user_data():
    return jsonify({
        "message" : f"User : {current_user.username}\n Role : {current_user.role}"
    })