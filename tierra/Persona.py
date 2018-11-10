
from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel
from Contacto import Contacto

class Persona(Contacto):
    nombre = ndb.StringProperty(required=True)
    apellido = ndb.StringProperty(required=True)
    correo = ndb.StringProperty(required=True, repeated=False)
    nickname = ndb.StringProperty(required=True, repeated=False)
    avatar = ndb.BlobProperty()
    creado = ndb.DateTimeProperty(auto_now_add=True)
    sexo = ndb.StringProperty(choices=['Hombre', 'Mujer'])

class Voluntario(Persona):
    #persona = ndb.UserProperty()
    rango = ndb.GeoPtProperty()
    disponibilidad = ndb.StringProperty() # disponibilidad de dias y tiempo

class Admin(Persona):
    asignado = ndb.DateTimeProperty(auto_now_add=True)
    activo = ndb.BooleanProperty(default=True)
