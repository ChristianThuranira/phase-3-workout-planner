from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
DATABASE_URL = "sqlite:///workout_planner.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)