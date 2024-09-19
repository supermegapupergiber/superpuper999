# superpuper999
this application provides the opportunity to fully learn everything you need to know about the hackaton leaguee  
hackathon_app/
├── app.py
└── models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    profiles = db.relationship('Profile', backref='team', lazy=True)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, default=0)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=True)
from flask import Flask, jsonify, request
from flask_cors import CORS
from models import db, Team, Profile

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hackathon.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
CORS(app)

with app.app_context():
    db.create_all()

@app.route('/teams', methods=['GET'])
def get_teams():
    teams = Team.query.all()
    return jsonify([{'id': team.id, 'name': team.name} for team in teams])

@app.route('/profiles', methods=['GET'])
def get_profiles():
    profiles = Profile.query.all()
    return jsonify([{'id': profile.id, 'username': profile.username, 'rating': profile.rating} for profile in profiles])

@app.route('/search', methods=['GET'])
def search_profiles():
    query = request.args.get('query', '')
    profiles = Profile.query.filter(Profile.username.contains(query)).all()
    return jsonify([{'id': profile.id, 'username': profile.username} for profile in profiles])

if __name__ == '__main__':
    app.run(debug=True)
