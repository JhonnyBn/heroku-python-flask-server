from flask import Flask, request app = Flask(__name__)@app.route('/', methods = ["GET","POST"])def index():    print(request)    print("oi")    return 'oi' @app.route('/post', methods = ["POST"])def post():    print(request.data)    return '' app.run(host='0.0.0.0')