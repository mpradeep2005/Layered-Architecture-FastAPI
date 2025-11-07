from fastapi import APIRouter
from db.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List


from services.health_check import health_check


from schemas.TeamResponse import TeamResponse, TeamCreate
from schemas.PlayersResponse import PlayerResponse, PlayerCreate

import services.player_services
import services.teams_services

router = APIRouter()

@router.get("/health_check",tags=["Health check"])
def check_api():
    return health_check()

@router.post("/teams",tags=["Teams"],response_model=TeamResponse)
def create_team(team: TeamCreate, db: Session = Depends(get_db)):
    return services.teams_services.create_team(db, team)

@router.get("/teams",tags=["Teams"], response_model=List[TeamResponse])
def list_teams(db: Session = Depends(get_db)):
    return services.teams_services.get_all_teams(db)

@router.post("/players",tags=["Players"], response_model=PlayerResponse)
def create_player(player: PlayerCreate, db: Session = Depends(get_db)):
    return services.player_services.create_player(db, player)

@router.get("/players",tags=["Players"], response_model=List[PlayerResponse])
def list_players(db: Session = Depends(get_db)):
    return services.player_services.get_all_players(db)

@router.get("/teams/{team_id}/players",tags=["Players"], response_model=List[PlayerResponse])
def list_players_by_team(team_id: int, db: Session = Depends(get_db)):
    return services.player_services.get_players_by_team(db, team_id)