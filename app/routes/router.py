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
        obj = oauth.login(request.form.to_dict())
        if(len(obj)>0):
            return "login exitoso!, adelante " + str(obj[0]['full_name']) + " :D"
        else:
            return "Credenciales erroneas"

@app.route('/register', methods=['GET', 'POST'])
def create_dev():
    if request.method == 'GET':
        return send_from_directory('./static/html/','register.html')
    else:
        usrId = oauth.register(request.form.to_dict())
        if(usrId > 0):
            return "registro exitoso!, adelante :D - Tu usuario tiene el id: " + str(usrId)
        else:
            return "Error desconocido en el registro"
