# blueprint for the users table in my db 
class User:
    def __init__(self,db,name,email,user_id=None):
        self.db = db 
        self.name = name
        self.email = email
        self.user_id = user_id
    
    
    # method to create the table in my db 
    @classmethod
    def create_table(cls,db):
        query = """
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        ) 
        """
        db.execute(query)
        
    def save(self):
        if self.user_id is None:
            # insert new user 
            # SQL INJECTIONS ? prevent via use of parameterized queries.
            query = "INSERT INTO users (name,email) VALUES (?,?)"
            self.db.execute(query,(self.name,self.email))
        else:
            # updating an existing user 
            query = "UPDATE users SET name = ?, email = ? WHERE id = ?"
            self.db.execute(query,(self.name,self.email,self.user_id))
            
    @classmethod
    def get_by_id(cls,db,user_id):
        query = "SELECT * FROM users WHERE id = ?"
        result = db.fetchOne(query,(user_id,))
        if result:
            return User(db, user_id=result[0], name=result[1], email=result[2])
        return None
    
    @classmethod
    def get_all(cls,db):
        query = "SELECT * FROM users"
        results = db.fetchall(query)
        return [User(db, user_id=row[0] , name=row[1], email=row[2]) for row in results]
    
    def delete(self):
        if self.user_id:
            query = "DELETE FROM users WHERE id = ?"
            self.db.execute(query, (self.user_id,))