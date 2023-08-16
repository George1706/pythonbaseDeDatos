#dependencia de flask 
from flask import Flask
#Dependencia de configuración
from .config import Config
#dependencia de modelo
from flask_sqlalchemy import SQLAlchemy
#dependencia para las migraciones 
from flask_migrate import Migrate



#crear el objeto python
app = Flask(__name__)

#Configuracion objeto flask
app.config.from_object(Config)

#Crear el objetto de Moldelos
db = SQLAlchemy(app)

#Crear objeto de migración
migrate = Migrate(app,db)

#impoertar los modelos  de .models
from .models import Cliente, Producto, Venta,Detalle