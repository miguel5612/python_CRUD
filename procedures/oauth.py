import sys
sys.path.append('../middlewares')
import crud
def login(credentials):
    resultado = Crud('usuarios').read({user:'mi usuario', password:'myPass'})
    print(resultado)

login()
print('hala')