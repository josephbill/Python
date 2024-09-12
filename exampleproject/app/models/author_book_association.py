from sqlalchemy import Table, Column , Integer, ForeignKey
from sqlalchemy.orm import relationship
from utils import Base

author_book_association = Table('author_book_association', Base.metadata, 
                                Column('author_id', Integer, ForeignKey('authors.id')),
                                Column('book_id', Integer, ForeignKey('books.id'))
                                )