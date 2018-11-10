
from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel

class Solitudes(polymodel.PolyModel):
    lugar = ndb.GeoPtProperty()
    creado = ndb.DateTimeProperty(auto_now_add=True)

class Plantas(Solitudes):
    tipo = ndb.StringProperty(required=True)

class Tierra(Solitudes):
    detalle = ndb.StringProperty(required=True)
