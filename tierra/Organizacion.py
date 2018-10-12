

from google.appengine.ext import ndb
from Contacto import Contacto

def validarNombre(prop, value):
    print(prop)
    if (value == "") or (value == None):
        raise ValueError("Debe tener un nombre")


class Organizacion(Contacto):
    nombre = ndb.StringProperty(required=True,validator=validarNombre)
    correo = ndb.StringProperty(required=True)
    creado = ndb.DateTimeProperty(auto_now_add=True)

org = Organizacion(nombre='REFCA',correo='')
org.put()
