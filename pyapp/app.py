from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configurer la connexion à la base de données via la variable d'environnement
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Créer l'objet SQLAlchemy
db = SQLAlchemy(app)

# Définir le modèle de la table
class DockerTable(db.Model):
    __tablename__ = 'dockertest'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)

# Route pour afficher les données de la table
@app.route('/')
def index():
    data = DockerTable.query.all()
    results = [{"id": row.id, "email": row.email} for row in data]
    return jsonify(results)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)