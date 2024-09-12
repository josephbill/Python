from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def get_engine(use_memory=True):
    if use_memory:
        # create an in-memory sqlite engine 
        return create_engine('sqlite:///:memory:', echo=False)
    else:
        return create_engine('sqlite:///example.db', echo=False)
    
# create an engine and connect to sqlite 
# use in-memory
engine = get_engine(use_memory=False)

Base = declarative_base()
Session = sessionmaker(bind=engine)

# create the table 
def create_table():
    '''utility to create all tables using BASE'''
    Base.metadata.create_all(engine)
    
def get_session():
    '''utility to get a new session'''
    return Session()