from app import db
from models.player import Player

class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    winner = db.Column(db.String(16), nullable=True)
    player_x_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    player_x = db.relationship("Player", foreign_keys="Game.player_x_id")
    player_o_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    player_o = db.relationship("Player", foreign_keys="Game.player_o_id")


def to_dict(self):
    return {
        "id": self.id,
        "winner": self.winner,
        "player_x": self.player_x.to_dict(),
        "player_o": self.player_o.to_dict()
    }
