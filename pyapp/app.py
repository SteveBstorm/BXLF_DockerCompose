from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class DockerTable(db.Model):
    __tablename__ = 'dockertest'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    
@app.route('/')
def index():
    data = DockerTable.query.all()
    results = ({"id": row.id, "email": row.email} for row in data)
    return jsonify(results)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)