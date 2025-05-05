from database import db

class Medicamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    fecha_inicio = db.Column(db.Date)
    fecha_fin = db.Column(db.Date)
    hora = db.Column(db.Time)
    frecuencia_diaria = db.Column(db.Integer)  # veces por día
    dias_semana = db.Column(db.String(50))  # ejemplo: "lunes,miércoles,viernes"
    cantidad = db.Column(db.Integer)  # cantidad a tomar