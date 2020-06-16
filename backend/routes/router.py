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
        return send_from_directory('./static/html/','login.html')
    else:
        oauth.login({'usuario':'lol'})
        return "login"

@app.route('/register', methods=['GET', 'POST'])
def create_dev():
    if request.method == 'GET':
        return send_from_directory('./static/html/','register.html')
    else:
        print("NO ES GET")
        return "NO GET"
