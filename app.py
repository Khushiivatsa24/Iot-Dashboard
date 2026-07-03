from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iot.db'
from extensions import db
db.init_app(app)

from models import SensorReading

@app.route('/')
def index():
    return render_template('index.html')

with app.app_context():
    db.create_all()

@app.route('/data', methods=['POST'])
def readings():
    data = request.get_json()
    new_readings = SensorReading(temp=data['temp'], humidity=data['humidity'])
    db.session.add(new_reading)
    db.session.commit()
    return {'message': 'saved'}, 200

@app.route('/readings', methods=['GET'])
def get_readings():
    readings = SensorReading.query.all()
    return {'readings': [{'temp': r.temp, 'humidity': r.humidity, 'timestamp': str(r.timestamp)} for r in readings]}
   

if __name__ == '__main__':
    app.run(debug=True)