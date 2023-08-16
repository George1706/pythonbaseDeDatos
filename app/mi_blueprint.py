from flask import Blueprint
mi_blueprint = Blueprint('mi_blueprint',
                         __name__,
                         url_prefix='/ejemplo')
@mi_blueprint.route('/prueba')
def index():
    return "hola , me encuentro en blueprint"