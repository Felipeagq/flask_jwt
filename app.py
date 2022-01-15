from flask import Flask, jsonify
from dotenv import load_dotenv
import os 
from routes.auth import routes_auth
from routes.protect_route import show

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

app = Flask(__name__)

app.config["SECRET_KEY"] = SECRET_KEY

app.register_blueprint(routes_auth, url_prefix="/api" )
app.register_blueprint(show, url_prefix="/api" )

@app.route("/")
def index():
    return jsonify({
        "msg":"ok",
        "data":"Index page"
    }),202

if __name__ == "__main__":
    app.run(debug=True)
