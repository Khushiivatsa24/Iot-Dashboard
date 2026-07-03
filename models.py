from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from extensions import db

class SensorReading(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    temp=db.Column(db.Float, nullable=False)
    humidity=db.Column(db.Float, nullable=False)
    timestamp=db.Column(db.DateTime, default=datetime.utcnow)