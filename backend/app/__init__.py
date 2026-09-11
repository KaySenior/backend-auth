import os

from flask import Flask, send_from_directory
from flask_login import LoginManager

from app.models import db, bcrypt, User

FRONTEND_DIST = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../frontend/dist"))

app = Flask(__name__, static_folder=FRONTEND_DIST, static_url_path="")
app.config.from_object("config.Config")

db.init_app(app)
bcrypt.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@login_manager.unauthorized_handler
def unauthorized():
    return {"error": "Login required."}, 401


from app.auth import auth_bp              

app.register_blueprint(auth_bp, url_prefix="/auth")

with app.app_context():
    db.create_all()


@app.route("/api/hello")
def hello():
    return {"msg": "initial page test"}


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_react(path):
    if path.startswith(("auth/", "api/")):
        return {"error": "Not found."}, 404
    full_path = os.path.join(FRONTEND_DIST, path)
    if path != "" and os.path.exists(full_path):
        return send_from_directory(FRONTEND_DIST, path)
    return send_from_directory(FRONTEND_DIST, "index.html")
