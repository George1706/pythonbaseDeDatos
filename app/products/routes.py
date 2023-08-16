from flask import render_template
from . import products

@products.route('/create')
def crear_producto():
    return render_template('new.html')