from flask import current_app as app
from flask import request
from flask import send_from_directory
from ..procedures import oauth

@app.route('/')
def index():
    return send_from_directory('./static/html/','index.html')
    

@app.route('/login')
def login():
    if request.method == 'GET':
        oauth.login({'usuario':'lol'})
        return "hala login"

@app.route('/register', methods=['GET', 'POST'])
def create_dev():
    if request.method == 'GET':
        print("GET")
        return "get"
    else:
        print("NO ES GET")
        return "NO GET"
