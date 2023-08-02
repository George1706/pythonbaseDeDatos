#dependencia de flask 
from flask import Flask
#dependencia de modelo
from flask_sqlalchemy import SQLAlchemy
#dependencia para las migraciones 
from flask_migrate import Migrate
#depencia para fecha y hora del sistema
from datetime import datetime

#crear el objeto python
app = Flask(__name__)
#definir 'cadena de conexion (conectionstring)'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/flask-shopy-2687340'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
 

#Crear el objetto de Moldelos
db = SQLAlchemy(app)

#Crear objeto de migración
migrate = Migrate(app,db)

#crear los modelos:
class Cliente(db.Model):
    #definir los atributos 
    __tablename__="clientes"
    id = db.Column(db.Integer, primary_key = True )
    username = db.Column(db.String(120), nullable = True)
    password = db.Column(db.String(128), nullable = True)
    email = db.Column(db.String(128), nullable = True)
    
    
    
class Producto(db.Model):
    __tablename__="productos"
    id = db.Column(db.Integer, primary_key = True )
    nombre = db.Column(db.String(100))
    precio = db.Column(db.Numeric(precision = 10, scale = 2))
    imagen = db.Column(db.String(200))
    
class Venta(db.Model):
    __tablename__="ventas"
    id = db.Column(db.Integer, primary_key = True )
    fecha = db.Column(db.DateTime, default = datetime.utcnow)
    #clave fóranea:
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id')) 
    
class Detalle(db.Model):
    __tablename__="detalles"
    id = db.Column(db.Integer, primary_key = True )
    venta_id = db.Column(db.Integer, db.ForeignKey('ventas.id')) 
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id')) 
    cantidad = db.Column(db.Integer)