from flask import request, jsonify
from flask_login import login_user, login_required, logout_user
import re

from app.auth import auth_bp
from app.models import db, bcrypt, User

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def _validate_credentials(username, password, email=None):
    if not username or not password:
        return "Username and password are required."
    if not 4 <= len(username) <= 20:
        return "Username must be between 4 and 20 characters."
    if email is not None:
        if not EMAIL_RE.match(email):
            return "A valid email address is required."
        if len(email) > 120:
            return "Email must be at most 120 characters."
    if not 8 <= len(password) <= 20:
        return "Password must be between 8 and 20 characters."
    return None


# POST /auth/signup  endpoint to signup a user
@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json(silent=True) or {}
    username = (data.get("username") or "").strip()
    email = (data.get("email") or "").strip().lower()
    password = data.get("password") or ""

    err = _validate_credentials(username, password, email)
    if err:
        return jsonify({"error": err}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists. Please choose a different one."}), 409

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already registered. Please use a different one."}), 409

    hashed = bcrypt.generate_password_hash(password)
    user = User(username=username, email=email, password=hashed)
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "User created. Please log in.", "username": username, "email": email}), 201


# POST /auth/login  endpoint to login a user
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}
    username = (data.get("username") or "").strip()
    password = data.get("password") or ""

    err = _validate_credentials(username, password)
    if err:
        return jsonify({"error": err}), 400

    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user)
        return jsonify({"msg": "Logged in.", "username": user.username}), 200
    return jsonify({"error": "Invalid username or password."}), 401


# POST /auth/logout  the endpoint to logout a user
@auth_bp.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"msg": "Logged out."}), 200
