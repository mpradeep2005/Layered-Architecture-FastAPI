from sqlalchemy.orm import Session
from db import models
from schemas import TeamResponse as schemas

def create_team(db: Session, team: schemas.TeamCreate):
    new_team = models.Team(name=team.name)
    db.add(new_team)
    db.commit()
    db.refresh(new_team)
    return new_team


def get_all_teams(db: Session):
    return db.query(models.Team).all()


def get_team_by_id(db: Session, team_id: int):
    return db.query(models.Team).filter(models.Team.id == team_id).first()
