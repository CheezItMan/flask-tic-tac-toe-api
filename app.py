
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Initialize SQL Alchemy
db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app(test_config=None):
    # Import routes
    from routes.User import User
    from routes.TicTacToeGame import TicTacToeGame
    
    app = Flask(__name__)
    CORS(app)
    api = Api(app)

    # Config App and SQL Alchemy
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Add Resources
    api.add_resource(User, '/tictactoe/player/v1', '/tictactoe/player/v1/<int:player_id>')
    api.add_resource(TicTacToeGame, '/tictactoe/game/v1/<int:game_id>', '/tictactoe/game/v1', )

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATABASE_CONNECTION_STRING')

    # Import Models Here!
    from models.player import Player
    from models.game import Game

    # Hook up Flask & SQL Alchemy
    db.init_app(app)
    migrate.init_app(app, db)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

