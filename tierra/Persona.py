
from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel
from Contacto import Contacto

class Persona(Contacto):
    nombre = ndb.StringProperty()
    apellido = ndb.StringProperty()
    correo = ndb.StringProperty()
    nickname = ndb.StringProperty()
    avatar = ndb.BlobProperty()
    creado = ndb.DateTimeProperty(auto_now_add=True)
    admin = ndb.BooleanProperty()

class Voluntario(Persona):
    #persona = ndb.UserProperty()
    rango = ndb.GeoPtProperty()
    disponibilidad = ndb.StringProperty() # disponibilidad de dias y tiempo

class Admin(Persona):
    asignado = ndb.DateTimeProperty(auto_now_add=True)

class Solitudes(ndb.Model):
    lugar = ndb.GeoPtProperty()
