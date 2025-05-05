from apscheduler.schedulers.background import BackgroundScheduler
from models import Medicamento
from database import db
from datetime import datetime, time
import threading

def revisar_medicamentos():
    with scheduler_app.app_context():
        hoy = datetime.today().strftime('%A').lower()  # Ej: 'monday'
        ahora = datetime.now().time()

        medicamentos = Medicamento.query.all()
        for m in medicamentos:
            if hoy in m.dias_semana.lower() and m.hora.hour == ahora.hour and m.hora.minute == ahora.minute:
                print(f"🔔 Alarma: Te toca tomar {m.nombre} - {m.descripcion}")

def iniciar_scheduler(app):
    global scheduler_app
    scheduler_app = app
    scheduler = BackgroundScheduler()
    scheduler.add_job(revisar_medicamentos, 'interval', minutes=1)
    scheduler.start()
