import pymssql
import logging
class conn_sql:
    def __init__(self,server,user,password,database):
         logging.info('Initializer')
         self.server = server
         self.user = user
         self.password = password
         self.database = database
         self.conn = None
    
    def connect(self):
        logging.debug('Connecting to BD {} on server {}'.format(self.server, self.database))
        if self.conn is None:           
            self.conn = pymssql.connect(server=self.server, user=self.user, password=self.password, database=self.database)
        return self.conn
    def close(self):
        self.close()
        return self.connect()
    