from sqlalchemy import String,Integer,ForeignKey
from db.database import Base
from sqlalchemy.orm import Mapped,mapped_column,relationship

class Team(Base):
    __tablename__="teams"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True)
    name:Mapped[str] = mapped_column(String,unique=True)
    players:Mapped[list["Player"]] = relationship(back_populates="team",cascade="all,delete-orphan")


class Player(Base):
    __tablename__="players"

    id:Mapped[int]=mapped_column(Integer,primary_key=True,unique=True)
    name: Mapped[str] = mapped_column(String)
    team_id:Mapped[int]=mapped_column(ForeignKey("teams.id"))
    team:Mapped["Team"]=relationship(back_populates="players")


