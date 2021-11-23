from app import db
from models.game import Game
from flask_restful import Resource
from flask import request


class TicTacToeGame(Resource):
    def post(self):
        body = request.get_json(force=True)
        print(body)

        player_x_id = int(body['player_x_id'])
        player_o_id = int(body['player_o_id'])

        new_game = Game(player_x_id=player_x_id, player_o_id=player_o_id, winner=None) 

        db.session.add(new_game)
        db.session.commit()
    
        if not new_game:
            return {"error": f"Could not create game"}, 500


        return {
            "game": {
                "id": new_game.id, 
                "winner": new_game.winner,
                "player_x_id": new_game.player_x_id,
                "player_o_id": new_game.player_o_id
            }
        }, 201


    def get(self):
        game_id = request.args['game_id']
        game = Game.query.get(game_id)

        if not game:
            return {"error": f"Could not find game {game_id}"}, 404
        
        return {
            "game": {
                "id": game.id, 
                "winner": game.winner,
                "player_x_id": game.player_x_id,
                "player_o_id": game.player_o_id
            }
        }, 200


    def put(self):
        game_id = request.args['game_id']
        body = request.get_json(force=True)

        game = Game.query.get(game_id)
        if not game:
            return {"error": f"Could not find game {game_id}"}, 404
        
        game.winner = int(body["winner"])
        game.player_x_id = body["player_x_id"]
        game.player_o_id = body["player_o_id"]
        db.session.commit()

        return {
            "game": {
                "id": game.id,
                "winner": int(game.winner),
                "player_x_id": game.player_x_id,
                "player_o_id": game.player_o_id,
            }
        }, 200


    def delete(self):
        game_id = request.args['game_id']
        game = Game.query.get(game_id)

        if game: 
            db.session.delete(game)
            db.session.commit()
            return {"message": f"Game {game_id} between player {game.player_x_id} and player {game.player_o_id} has been deleted"}, 200

        return {"error": f"Could not find game {game_id}"}, 404


