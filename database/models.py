from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.orm import relationship, backref
from db_config import db_path


engine = create_engine('sqlite://'+ db_path)

engine.connect()

class Courier(Base):
    __tablename__ = "Courier"
    courier_id = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    name_from_father = Column(String)
    create_date = Column(String)

class Container(Base):
    __tablename__ = "Container"
    container_id = Column(Integernteger, primary_key=True)
    courier_id = Column(String)
    date_hand_over = Column(String)
