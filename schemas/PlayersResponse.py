from pydantic import BaseModel


class PlayerBase(BaseModel):
    name: str

class PlayerCreate(PlayerBase):
    team_id: int

class PlayerResponse(PlayerBase):
    id: int
    team_id: int

    class Config:
        from_attributes = True

