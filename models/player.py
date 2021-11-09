
from app import db


class Player(db.Model):
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    # TODO maybe make uid and provider TOGETHER be unique
    #     UniqueConstraint('col2', 'col3', name='uix_1')

    uid = db.Column(db.String(256), unique=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "uid": self.uid,
        }
