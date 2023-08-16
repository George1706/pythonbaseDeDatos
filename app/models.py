from app import db
from datetime import datetime

#crear los modelos:
class Cliente(db.Model):
    #definir los atributos 
    __tablename__="clientes"
    id = db.Column(db.Integer, primary_key = True )
    username = db.Column(db.String(120), nullable = True)
    password = db.Column(db.String(128), nullable = True)
    email = db.Column(db.String(128), nullable = True)
    
    #Relaciones SQL alchemy
    
    ventas = db.relationship('Venta', 
                             backref = "cliente", 
                             lazy = "dynamic")
    
    
    
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