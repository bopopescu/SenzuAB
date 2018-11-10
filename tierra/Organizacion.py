

from google.appengine.ext import ndb
from Contacto import Contacto

def validarNombre(prop, value):
    print(prop)
    if (value == "") or (value == None):
        raise ValueError("Debe tener un nombre")

def calcultar_mitad_de_precio(entity):
    return entity.precio / 2

class Organizacion(Contacto):
    nombre = ndb.StringProperty(required=True, repeated=False,validator=validarNombre)
    correo = ndb.StringProperty(required=True, repeated=False)
    creado = ndb.DateTimeProperty(auto_now_add=True)
    precio = ndb.IntegerProperty(default=1)
    mitad = ndb.ComputedProperty(calcultar_mitad_de_precio)

org = Organizacion(nombre='REFCA',correo='', precio=50)
print org.mitad
org.put()
