from flask import current_app as app
from flask import request
from flask import send_from_directory
from ..procedures import oauth

@app.route('/')
def index():
    return send_from_directory('./static/html/','index.html')
    

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return send_from_directory('./static/html/','login.html')
    else:
        if(oauth.login(request.form.to_dict())):
            return "login exitoso!, adelante :D"
        else:
            return "Credenciales erroneas"

@app.route('/register', methods=['GET', 'POST'])
def create_dev():
    if request.method == 'GET':
        return send_from_directory('./static/html/','register.html')
    else:
        if(oauth.register(request.form.to_dict())):
            return "registro exitoso!, adelante :D"
        else:
            return "Error desconocido en el registro"
