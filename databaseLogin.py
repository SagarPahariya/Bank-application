from sqlalchemy import create_engine
from config import *


class DBLogin:
    def __init__(self):
        self.user = DBUSER
        self.password = DBPASSWORD
        self.host = DBHOST
        self.port = DBPORT
        self.database = DBDATABASE

    def db_connection(self):
        try:
            db_url = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
                self.user, self.password, self.host, self.port, self.database
            )
            print(db_url)
            engine = create_engine(db_url)
            print("Database connection successful")
            return engine

        except Exception as e:
            print("Failed to connect to DB: {}".format(e))
            return None
