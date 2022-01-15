from crypt import methods
from flask import Blueprint, jsonify, request
from itsdangerous import json
from make_jwt import write_token, validate_token

routes_auth = Blueprint("routes_auth",__name__)

@routes_auth.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        data = request.get_json()
        if data.get("username",None) == "Felipe":
            return write_token(data=request.get_json())
        else:
            response = jsonify({"msg":"User not found"})
            response.status_code = 404
            return response
    return jsonify({"msg":"make a POST witn the username"})


@routes_auth.route("/verify/token")
def verify_token():
    print(request.headers["Authorization"].split(" "))
    token = request.headers["Authorization"].split(" ")[1]
    print(token)
    return validate_token(token, output=True)
