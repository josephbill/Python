from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from utils import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    # One-to-Many relationship with Post
    posts = relationship('Post', back_populates='user')

    # One-to-One relationship with Profile
    profile = relationship('Profile', uselist=False, back_populates='user')

    def __repr__(self):
        return f'<User(name={self.name}, email={self.email})>'
