# sqlite3
import sqlite3

# define the db execution, db cursor (object used to execute sql commands and fetch data from the db) . Methods : execute commands , fetchall, fetchone, delete 
class Database:
    def __init__(self,db_name):
        # attribute to establish connection to my db 
        self.conn = sqlite3.connect(db_name)
        # attribute pointing to the current instance in query 
        self.cursor = self.conn.cursor()
    
    # SELECT, INSERT , UPDATE , DELETE 
    # helper
    def execute(self,query,params=None):
        if params:
            self.cursor.execute(query,params)
        else:
            self.cursor.execute(query)
            
        self.conn.commit()
     
    # SELECT STATEMENTS 'SELECT * FROM users'   
    def fetchall(self,query,params=None):
        # self.execute (self: instance) .execute
        self.execute(query,params)
        # return all records from execution , return list of data 
        return self.cursor.fetchall()
    
    def fetchOne(self,query,params=None):
        self.execute(query,params)
        # fetchone returns the single entity (object)
        return self.cursor.fetchone()
    
    def close(self):
        self.conn.close()
        