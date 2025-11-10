from pathlib import Path

class Book:
  ISBN_FILE = Path('ISBN_counter.txt')

  if not ISBN_FILE.exists():
    with open('ISBN_counter.txt', 'w') as books_counter:
      books_counter.write('1000')
  with open('ISBN_counter.txt', 'r') as books_counter:
    ISBN = int(books_counter.read()) +1
  with open('ISBN_counter.txt', 'w') as books_counter:
    books_counter.write(f'{ISBN}')
  
  def __init__(self, title, author, is_available=True):
    self.title = title
    self.author = author
    self.ISBN = Book.ISBN
    self.is_available = is_available
  def __str__(self):
    return f'Book Info\nISBN: {self.ISBN}\ntitle: {self.title}\nauthor: {self.author}\nbook is {'available' if self.is_available else 'not available'}'


