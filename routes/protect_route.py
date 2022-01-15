from flask import Blueprint, jsonify
from make_jwt import validate_token
from flask import request


show = Blueprint("show",__name__)


@show.before_request
def verify_token_middleware():
    token = request.headers["Authorization"].split(" ")[1]
    validate_token(token, output=False)
    # si el token es valido, NO RETORNAR NADA


@show.route("/show")
def show_route():
    return jsonify({"msg":"This route its protected"})