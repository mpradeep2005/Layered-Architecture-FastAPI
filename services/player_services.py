from sqlalchemy.orm import Session
from db import models
from schemas import PlayersResponse as schemas


def create_player(db: Session, player: schemas.PlayerCreate):
    new_player = models.Player(name=player.name, team_id=player.team_id)
    db.add(new_player)
    db.commit()
    db.refresh(new_player)
    return new_player


def get_players_by_team(db: Session, team_id: int):
    return db.query(models.Player).filter(models.Player.team_id == team_id).all()


def get_all_players(db: Session):
    return db.query(models.Player).all()