from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

def get_engine(use_memory=True):
    if use_memory:
        # create an in-memory sqlite engine 
        return create_engine('sqlite:///:memory:', echo=True)
    else:
        return create_engine('sqlite:///sqlalchemyblog.db', echo=True)
    
# create an engine and connect to sqlite 
# use in-memory
engine = get_engine(use_memory=False)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    # attributes , columns 
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    
    def __repr__(self):
        return f"<User(name={self.name}, email={self.email})>"
    

# create the table
Base.metadata.create_all(engine)
# create sessions to interact with the db 
Session = sessionmaker(bind=engine)
# session object (methods, attributes)
session = Session()

user1 = User(name='Joseph', email="joseph.mbugua@moringaschool.com")
user2 = User(name='Alice', email="alice.mbugua@moringaschool.com")

# session object 
session.add_all([user1,user2])
session.commit()

# query the table 
users = session.query(User).all()
for user in users:
    print(user)
    
# update 
result1 = session.query(User).filter_by(name='Joseph').first()
result1.name = "Bill"
session.commit()

# delete a record 
# result1 = session.query(User).filter_by(name='Joseph').first()
# session.delete(result1)
# session.commit()

# close sessions 
session.close()

