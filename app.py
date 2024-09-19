from flask import Flask
from flask_cors import CORS
from models import db
from routes import main_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hackathon.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
CORS(app)

with app.app_context():
    db.create_all()

app.register_blueprint(main_routes)

if __name__ == '__main__':
    app.run(debug=True)

