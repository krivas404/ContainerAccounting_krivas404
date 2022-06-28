from sqlalchemy import create_engine
from db_config import db_path


engine = create_engine('sqlite://' + db_path, echo=True)

pool_recycle = 7200

engine.connect()


