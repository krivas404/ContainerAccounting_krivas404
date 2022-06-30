from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, func
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

    def __init__(self, first_name, last_name, name_from_father):
        self.courier_id = self.create_next_courier_id()  # need to create new ID for primary_key field
        self.first_name = first_name
        self.last_name = last_name
        self.name_from_father = name_from_father
        self.create_date = str(datetime.now())


    @staticmethod
    def create_next_courier_id():
        session = Session()
        query_all_couriers = session.query(Courier).all()
        print('all: ', query_all_couriers)
        current_max_id = session.query(func.max(Courier.courier_id)).first()  # запрос в БД, узнать текущий максимальный id
        print('current_max_id: ', current_max_id, 'type: ', type(current_max_id), 'len: ', len(current_max_id))
        current_max_id = current_max_id[0]  # from sqlalchemy row take only ID
        print(current_max_id, type(current_max_id))
        if current_max_id is None:
            new_max_id = 'hm000001'  # если запрос пустой, то присваиваем самый первый id
        else:
            new_max_id_no_prefix = str(int(current_max_id[2:]) + 1)  # первые 2 символа - префикс, дальше 6 цифр.
            # Цифры слайсим, из строки переводим в integer, увеличиваем на 1, и возвращаем в string, префикс объединяем с получившейся строкой
            new_max_id = 'hm' + '000000'[:6 - len(new_max_id_no_prefix)] + new_max_id_no_prefix
            # префикс курьера + количество недостающих нулей до 6 цифер + новое число id
        return new_max_id


    def __repr__(self):
        return f"<Курьер. {self.courier_id}, {self.last_name} {self.first_name} {self.name_from_father}"


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
        self.date_hand_over = str(datetime.now())

    def __repr__(self):
        return f"<Контейнер id: {self.container_id}"

def main():
    pass

engine = create_engine('sqlite://' + db_path, echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
