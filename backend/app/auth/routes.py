from flask import request, jsonify
from flask_login import login_user, login_required, logout_user, current_user

from app.auth import auth_bp
from app.models import db, bcrypt, User


def _validate_credentials(username, password):
    """Mirror zip's WTForms rules: SignUpForm/LoginForm + validate_username."""
    if not username or not password:
        return "Username and password are required."
    if not 4 <= len(username) <= 20:
        return "Username must be between 4 and 20 characters."
    if not 8 <= len(password) <= 20:
        return "Password must be between 8 and 20 characters."
    return None


# POST /auth/signup  (zip: /signUp with SignUpForm)
@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json(silent=True) or {}
    username = (data.get("username") or "").strip()
    password = data.get("password") or ""

    err = _validate_credentials(username, password)
    if err:
        return jsonify({"error": err}), 400

    if User.query.filter_by(username=username).first():
        # zip app.py:50-52
        return jsonify({"error": "Username already exists. Please choose a different one."}), 409

    hashed = bcrypt.generate_password_hash(password).decode("utf-8")
    user = User(username=username, password=hashed)
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "User created. Please log in.", "username": username}), 201


# POST /auth/login  (zip: /login with LoginForm)
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


# POST /auth/logout  (zip: /logout)
@auth_bp.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"msg": "Logged out."}), 200


# GET /auth/me  (zip: /dashboard, @login_required -> dashboard.html)
@auth_bp.route("/me", methods=["GET"])
@login_required
def me():
    return jsonify({"username": current_user.username}), 200
