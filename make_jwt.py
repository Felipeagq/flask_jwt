from http.client import ResponseNotReady
from urllib import response

from flask import jsonify
from jwt import exceptions
from jwt import encode, decode
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

def expire_date(days:int):
    now = datetime.now()
    new_date = now + timedelta(days)
    return new_date


def write_token(data:dict):
    token = encode(payload={**data,"exp":expire_date(2)}, key=SECRET_KEY,algorithm="HS256")
    return token.encode("utf-8")


def validate_token(token, output=False):
    try:
        if output:
            return decode(token, key=SECRET_KEY,algorithms=["HS256"])
        return decode(token, key=SECRET_KEY,algorithms=["HS256"])
    except exceptions.DecodeError:
        response = jsonify({"msg":"Invalid Token"})
        response.status_code = 404
        return response 
    except exceptions.ExpiredSignatureError:
        response = jsonify({"msg":"Token Expired"})
        response.status_code = 401
        return response 