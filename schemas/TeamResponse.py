from pydantic import BaseModel
from typing import List, Optional
from schemas.PlayersResponse import  PlayerResponse

class TeamBase(BaseModel):
    name: str

class TeamCreate(TeamBase):
    pass

class TeamResponse(TeamBase):
    id: int
    players: Optional[List[PlayerResponse]] = []

    class Config:
        from_attributes = True
