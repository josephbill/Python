from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# User model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # product = relationship("Product", back_populates="users")
    
# Product model
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    # owner_id = Column(Integer, ForeignKey('users.id'))

    # user = relationship("User", back_populates="products")
    
# Database setup
DATABASE_URL = 'sqlite:///app.db'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Create tables
def create_db():
    Base.metadata.create_all(engine)
    
    
'''
migrations steps 
1. Initialize alembic migrations 
2. change sqlalchemy.url link 
3. in .env set Base metadata for the target.none value 
4. applying the migration : python -m alembic upgrade head 
5. to delete a migration then run : python -m alembic downgrade 
'''