from app import db
from models.player import Player
from models.game import Game
from flask_restful import Resource
from flask import request


class User(Resource):
    def post(self):
        body = request.get_json(force=True)

        if "name" in body:
            new_player = Player(name=body["name"])
            Player.query.session.add(new_player)
            Player.query.session.commit()
            return new_player.to_dict(), 201
        else:
            return {"error": "name is required"}, 400


    def get(self):
        player_id = request.args['player_id']
        player = Player.query.get(player_id)

        if not player:
            return {"error": f"Could not find player {player_id}"}, 404
        
        return {
            "player": {
                "id": player.id, 
                "name": player.name,
                "uid": player.uid,
            }
        }, 200


    def put(self):
        body = request.get_json(force=True)
        player_id = request.args['player_id']
        player = Player.query.get(player_id)
        
        if not player:
            return {"error": f"Could not find player {player_id}"}, 404
        
        player.name = body["name"]
        db.session.commit()

        return {
            "player": {
                "id": player.id,
                "name": player.name,
                "uid": player.uid
            }
        }, 200


    def delete(self):
        player_id = request.args['player_id']
        player = Player.query.get(player_id)

        if player: 
            db.session.delete(player)
            db.session.commit()
            return {"message": f"Player {player_id} has been deleted"}, 200

        return {"error": f"Could not find player {player_id}"}, 404
