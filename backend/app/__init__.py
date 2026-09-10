from flask import Flask, send_from_directory
import os

FRONTEND_DIST = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../frontend/dist"))

app = Flask(__name__, static_folder=FRONTEND_DIST, static_url_path="")

@app.route("/api/hello")
def hello():
    return {"msg": "initial page test"}

                                                
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_react(path):
    full_path = os.path.join(FRONTEND_DIST, path)
    if path != "" and os.path.exists(full_path):
        return send_from_directory(FRONTEND_DIST, path)
    return send_from_directory(FRONTEND_DIST, "index.html")