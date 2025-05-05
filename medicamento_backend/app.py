from flask import Flask
from config import MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB, MYSQL_HOST
from database import db
from routes import routes
from flask_cors import CORS
from scheduler import iniciar_scheduler

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(routes)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    iniciar_scheduler(app)
    app.run(debug=True)