from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from utils import Base

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    # One-to-Many relationship with User
    user = relationship('User', back_populates='posts')

    def __repr__(self):
        return f'<Post(title={self.title}, content={self.content}, user_id={self.user_id})>'
