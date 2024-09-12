from utils import get_session,create_table
from models.author import Author
from models.book import Book 

create_table()
session = get_session()

author1 = Author(name="Author A")
author2 = Author(name="Author B")

book1 = Book(name="Book A")
book2 = Book(name="Book B")

# establishing the relationships 
author1.books.append(book1)
author1.books.append(book2)
author2.books.append(book2)

session.add_all([author1,author2,book1,book2])
session.commit()

authors = session.query(Author).all()
for author in authors:
    print(author)
    for book in author.books:
        print(f' {book}')
        
books = session.query(Book).all()
for book in books:
    print(book)
    for author in book.authors:
        print(f' {author}')