import pyodbc
pyodbc.dataSources()
import json

from Configurations import Configurations


class Database:
    def __init__(self, database):
        print(self)
        Config = Configurations()
        self.Config = Config.GetConfig()
        self.database = database
        self.conn = None

    def Connect(self):
        driver = self.Config["SQL"]["driver"]
        server = self.Config["SQL"]["server"]
        database = self.Config["SQL"]["database"]
        user = self.Config["SQL"]["user"]
        password = self.Config["SQL"]["password"]
        database_default = self.Config["SQL"]["database_default"]
        cnx = "DRIVER={};SERVER={};DATABASE={};UID={};PWD={}".format(
            driver, server, database, user, password)
        print(cnx)
        print(server)
        if self.database != database:
            self.database = database_default
        if self.conn is None:
            # self.conn = pymssql.connect(server=str(server).strip(),
            #                            port=1433,
            #                            user=user,
            #                            password=password,
            #                            database=self.database)
            self.conn = pyodbc.connect(cnx)
        return self.conn

    def Close(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None
