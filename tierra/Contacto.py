
from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel

class Contacto(polymodel.PolyModel):
    numero_telefonico = ndb.StringProperty(repeated=False)
    direccion = ndb.StringProperty()
