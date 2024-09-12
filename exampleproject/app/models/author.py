from sqlalchemy import Column, Integer , String 
from sqlalchemy.orm import relationship
from utils import Base 
from models.author_book_association import author_book_association

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    # many to many relationships 
    books = relationship('Book',secondary=author_book_association, back_populates='authors')
    
    def __repr__(self):
        return f"<Author(name={self.name})>"