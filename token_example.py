import jwt
SECRET_KEY="llave secreta"

token = jwt.encode({"id":"Felipe"},
key=SECRET_KEY,
algorithm="HS256")
print(f"token : {token}")
print("-"*50)

de_token = jwt.decode(token,key=SECRET_KEY,algorithms=["HS256"])
print(f"token decodificado : {de_token}")
