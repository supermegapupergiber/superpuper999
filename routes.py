from flask import Blueprint, jsonify, request
from models import db, Team, Profile

main_routes = Blueprint('main', __name__)

@main_routes.route('/teams', methods=['GET'])
def get_teams():
    teams = Team.query.all()
    return jsonify([{'id': team.id, 'name': team.name, 'rating': team.rating} for team in teams])

@main_routes.route('/profiles', methods=['GET'])
def get_profiles():
    profiles = Profile.query.all()
    return jsonify([{'id': profile.id, 'username': profile.username, 'rating': profile.rating} for profile in profiles])

@main_routes.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    profiles = Profile.query.filter(Profile.username.contains(query)).all()
    return jsonify([{'id': profile.id, 'username': profile.username} for profile in profiles])

@main_routes.route('/ratings', methods=['GET'])
def get_ratings():
    teams = Team.query.order_by(Team.rating.desc()).all()
    profiles = Profile.query.order_by(Profile.rating.desc()).all()
    return jsonify({
        'team_ratings': [{'name': team.name, 'rating': team.rating} for team in teams],
        'profile_ratings': [{'username': profile.username, 'rating': profile.rating} for profile in profiles]
    })

