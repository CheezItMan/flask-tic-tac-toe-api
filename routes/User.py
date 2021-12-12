from app import db
from models.player import Player
from models.game import Game
from flask_restful import Resource
from flask import request


class User(Resource):
    def post(self):
        body = request.get_json()

        if "name" in body:
            # player = Player.query.filter(Player.name == body["name"])
            player = Player.query.filter_by(name=body["name"])

            if player.count() >= 1:
                return player[0].to_dict(), 200
            elif player.count() == 0:
                new_player = Player(name=body["name"])
                Player.query.session.add(new_player)
                Player.query.session.commit()
                return new_player.to_dict(), 201
        else:
            return {"error": "name is required"}, 400


    def get(self, player_id):
        player = Player.query.get(player_id)

        if not player:
            return {"error": f"Could not find player {player_id}"}, 404

        return player.to_dict(), 200


    def put(self, player_id):
        body = request.get_json()
        player = Player.query.get(player_id)

        if not player:
            return {"error": f"Could not find player {player_id}"}, 404
        
        player.name = body["name"]
        db.session.commit()

        return player.to_dict(), 200


    def delete(self, player_id):
        player = Player.query.get(player_id)

        if player: 
            db.session.delete(player)
            db.session.commit()
            return {"message": f"Player {player_id} has been deleted"}, 200

        return {"error": f"Could not find player {player_id}"}, 404
