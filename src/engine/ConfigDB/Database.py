import pymssql
import json

from Configurations import Configurations


class Database:
    def __init__(self, database):
        Config = Configurations()
        self.Config = Config.GetConfig()
        self.database = database
        self.conn = None

    def Connect(self):
        if self.database != self.Config["SQL"]["database"]:
            self.database = self.Config["SQL"]["database_default"]
        if self.conn is None:
            self.conn = pymssql.connect(
                server=self.Config["SQL"]["server"],
                user=self.Config["SQL"]["user"],
                password=self.Config["SQL"]["password"],
                database=self.database)
        return self.conn

    def Close(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None
