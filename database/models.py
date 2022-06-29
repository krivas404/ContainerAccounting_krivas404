# from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
# from sqlalchemy.orm import relationship, backref
# from sqlalchemy.orm import mapper
#
# from database.dbsession import engine
# from datetime import datetime
#
# engine.connect()
#
#
# from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
#
# metadata_couriers = MetaData()
# courier_table = Table('Couriers', metadata_couriers,
#                     Column('courier_id', String, primary_key=True),
#                     Column('first_name', String),
#                     Column('last_name', String),
#                     Column('name_from_father', String),
#                     Column('create_date', String)
#                       )
#
# metadata_containers = MetaData()
# container_table = Table('Containers', metadata_containers,
#                     Column('key_id', Integer, primary_key=True),
#                     Column('container_id', Integer),
#                     Column('courier_id', String),
#                     Column('date', String),
#                         )
#
#
# class Courier(Base):
#     __tablename__ = "Couriers"
#     courier_id = Column(String(15), primary_key=True)
#     first_name = Column(String(30), nullable=False)
#     last_name = Column(String(30), nullable=False)
#     name_from_father = Column(String(30))
#     create_date = Column(String(100))
#
# class Container(Base):
#     __tablename__ = "Containers"
#     key = Column(Integer, primary_key=True)
#     container_id = Column(Integer, nullable=False)
#     courier_id = Column(String(15), nullable=False)
#     date_hand_over = Column(String)
#
#
# class Courier(object):
#     def __init__(self, courier_id, first_name, last_name, name_from_father):
#         self.courier_id = courier_id
#         self.first_name = first_name
#         self.last_name = last_name
#         self.name_from_father = name_from_father
#         self.fullname = self.first_name + self.name_from_father + self.last_name
#         self.create_date = str(datetime.now())
#
#     def __repr__(self):
#         return f"<Курьер. {self.courier_id}, {self.fullname}"
#
#
# class Container(object):
#     def __init__(self, container_id, last_name, name_from_father):
#         self.container_id = container_id
#
#     def __repr__(self):
#         return f"<Контейнер id: {self.container_id}"
#
#
# mapper(Courier, courier_table)
#
#
