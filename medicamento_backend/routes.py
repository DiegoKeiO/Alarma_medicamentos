from flask import Blueprint, request, jsonify
from models import Medicamento
from database import db

routes = Blueprint('routes', __name__)

@routes.route('/medicamentos', methods=['GET'])
def obtener_medicamentos():
    medicamentos = Medicamento.query.all()
    return jsonify([{
        'id': m.id,
        'nombre': m.nombre,
        'descripcion': m.descripcion,
        'fecha_inicio': m.fecha_inicio.isoformat(),
        'fecha_fin': m.fecha_fin.isoformat(),
        'hora': str(m.hora),
        'frecuencia_diaria': m.frecuencia_diaria,
        'dias_semana': m.dias_semana
    } for m in medicamentos])

@routes.route('/medicamentos', methods=['POST'])
def agregar_medicamento():
    data = request.json
    medicamento = Medicamento(**data)
    db.session.add(medicamento)
    db.session.commit()
    return jsonify({'mensaje': 'Medicamento añadido correctamente'})
