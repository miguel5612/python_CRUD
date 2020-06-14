import sys
sys.path.append('../middlewares')
from ..middlewares import crud

def login(credentials):    
    crud.Crud('usuarios').index()
    crud.Crud('usuarios').create({'user':'mi usuario', 'password':'myPass'})
    crud.Crud('usuarios').read({'user':'mi usuario', 'password':'myPass'})
    crud.Crud('usuarios').update({'user': 'nuevousuario', 'password': 'lol'}, {'id':10})
    crud.Crud('usuarios').delete({'id':10})
    #print(resultado)

#cred = {'user':'mi usuario', 'password':'myPass'}
#print(list(cred.keys())[0])
#login({'user':'mi usuario', 'password':'myPass'})