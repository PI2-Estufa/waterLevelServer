import datetime 
from sqlalchemy import create_engine, Column, Integer, Float, Unicode, Sequence, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql://greenhouse:greenhouse@postgres:5432/greenhouse", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class WaterLevel(Base):

    __tablename__ = 'water_level'

    id = Column(Integer, 
            Sequence('water_level_id_seq'), primary_key=True)
    value = Column(Integer)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

Base.metadata.create_all(engine)