#Dependencia para hacer un blueprint
from flask import Blueprint

#Definimos paquete 'products'
products = Blueprint('products',
                     __name__,
                     url_prefix='/products',
                     template_folder='templates')

from . import routes