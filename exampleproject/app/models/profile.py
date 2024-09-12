from sqlalchemy import Column, Integer, String , ForeignKey
from sqlalchemy.orm import relationship
from utils import Base
class Profile(Base):
    __tablename__ = 'profiles'
    
    id = Column(Integer,primary_key=True)
    bio = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    # one to one relationship with users 
    # posts = relationship('User',back_populates='profile')
    user = relationship('User', back_populates='profile')

    def __repr__(self):
        return f'<Profile({self.bio})>'