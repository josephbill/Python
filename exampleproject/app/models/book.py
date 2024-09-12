from sqlalchemy import Column, Integer , String 
from sqlalchemy.orm import relationship
from utils import Base 
from models.author_book_association import author_book_association

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    # many to many relationships 
    authors = relationship('Author',secondary=author_book_association, back_populates='books')
    
    def __repr__(self):
        return f"<Book(name={self.name})>"