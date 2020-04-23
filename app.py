import os, json
from flask import Flask, jsonify, request#, abort, redirect, url_for
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False
jwt = JWTManager(app)

# test route
@app.route('/', methods = ["GET","POST"])
def index():
	print(request)
	return request.data

# Provide a method to create access tokens. The create_access_token()
# function is used to actually generate the token, and you can return
# it to the caller however you choose.
@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({ "auth": False, "token": None, "message": "Missing JSON in request" }), 200

    username = request.json.get('user', None)
    password = request.json.get('pwd', None)
    if not username:
        return jsonify({ "auth": False, "token": None, "message": "Missing username parameter"}), 200
    if not password:
        return jsonify({ "auth": False, "token": None, "message": "Missing password parameter"}), 200

    if username != 'admin' or password != 'admin':
        return jsonify({ "auth": False, "token": None, "message": "Bad username or password"}), 200

    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=username)
    return jsonify({ "auth": True, "token": access_token, "message": "Logged in succesfully."}), 200


# Protect a view with jwt_required, which requires a valid access token
# in the request to access.
@app.route('/teste', methods=['GET'])
@jwt_required
def teste():
	um = int(request.args.get('um', '0') or '0', 10)
	dois = int(request.args.get('dois', '0') or '0', 10)
	tres = int(request.args.get('tres', '0') or '0', 10)
	quatro = int(request.args.get('quatro', '0') or '0', 10)
	cinco = int(request.args.get('cinco', '0') or '0', 10)
	seis = int(request.args.get('seis', '0') or '0', 10)
	return jsonify(	um=um,
					dois=dois,
					tres=tres,
					quatro=quatro,
					cinco=cinco,
					seis=seis), 200
    # Access the identity of the current user with get_jwt_identity
    #current_user = get_jwt_identity()
    #return jsonify(logged_in_as=current_user), 200


if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)