from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine, select
from sqlalchemy import text

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


engine = create_engine("sqlite:///database.db")

# filtrando
with Session(engine) as session:
    statement = select(Hero).where(Hero.name == "Spider-Boy")
    hero = session.exec(statement).first()
    print(hero)

print('-'*20)
# pegando todos
with Session(engine) as session:
    # statement = select(Hero).where(Hero.name == "Spider-Boy")
    statement = select(Hero)
    # hero = session.exec(statement).first()
    hero = session.exec(statement).all()
    print(hero)

print('-'*20)
with Session(engine) as session:
    statement = text("SELECT * FROM Hero;")
    results = session.exec(statement)
    heroes = results.fetchall()
    print(heroes)