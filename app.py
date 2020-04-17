import os, json
from flask import Flask, jsonify, request, abort, redirect, url_for

app = Flask(__name__)

@app.route('/', methods = ["GET","POST"])
def index():
	print(request)
	return request.data
	
@app.route('/login', methods = ["POST"])
def login():
	print(request.data)
	data = json.loads(request.data)
	if data["user"] == "admin" and data["pwd"] == "admin":
		auth = {
			"auth": True,
			"token": "token",
			"message": "Logged in succesfully."
		}
		return jsonify(auth)
	auth = {
		"auth": False,
		"token": None,
		"message": "Invalid credentials."
	}
	return jsonify(auth)


def verifyToken(token):
	return token == "token"

def checkLogin(request):
	if not verifyToken(request.headers.get('access-token')):
		abort(401)
	
@app.route('/teste', methods = ["GET"])
def teste():
	checkLogin(request)
	um = int(request.args.get('um', '0') or '0', 10)
	dois = int(request.args.get('dois', '0') or '0', 10)
	tres = int(request.args.get('tres', '0') or '0', 10)
	quatro = int(request.args.get('quatro', '0') or '0', 10)
	lista = [ um*2, dois*2, tres*2, quatro*2 ]
	return jsonify(lista)
		
if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)