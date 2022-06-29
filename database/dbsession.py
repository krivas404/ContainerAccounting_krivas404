from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from db_config import db_path
from datetime import datetime


pool_recycle = 7200
Base = declarative_base()


class Courier(Base):
    __tablename__ = "Couriers"
    courier_id = Column(String(15), primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    name_from_father = Column(String(30))
    create_date = Column(String(100))

    def __init__(self, courier_id, first_name, last_name, name_from_father):
        self.courier_id = courier_id
        self.first_name = first_name
        self.last_name = last_name
        self.name_from_father = name_from_father
        self.fullname = self.first_name + self.name_from_father + self.last_name
        self.create_date = str(datetime.now())

    def __repr__(self):
        return f"<Курьер. {self.courier_id}, {self.fullname}"


class Container(Base):
    """Class for accounting containers movement between couriers and storage"""
    __tablename__ = "Containers_movement"
    key = Column(Integer, primary_key=True)
    container_id = Column(Integer, nullable=False)
    courier_id = Column(String(15), nullable=False)
    date_hand_over = Column(String)

    def __init__(self, container_id, courier_id):
        self.container_id = container_id
        self.courier_id = courier_id

    def __repr__(self):
        return f"<Контейнер id: {self.container_id}"

def main:
    pass

engine = create_engine('sqlite://' + db_path, echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
