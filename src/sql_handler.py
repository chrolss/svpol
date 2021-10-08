from sqlalchemy import create_engine

class SqlHandler:
    def __init__(self) -> None:
        self.engine = create_engine("sqlite:////home/chrolss/PycharmProjects/svpol/data/tweets.db")
        self.con = self.engine.connect()

    def get_engine(self):
        return self.engine

    def get_connection(self):
        return self.con
    