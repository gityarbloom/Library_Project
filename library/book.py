from pathlib import Path

class Book:
  ISBN_FILE = Path('data/ISBN_counter.txt')
  if not ISBN_FILE.exists():
    with open(ISBN_FILE, 'w') as f:
      f.write('1000')

  def __init__(self, title, author, is_available=True):

    with open(Book.ISBN_FILE, 'r') as books_counter:
      self.ISBN = int(books_counter.read()) +1

    self.title = title
    self.author = author
    self.is_available = is_available

    with open(Book.ISBN_FILE, 'w') as books_counter:
      books_counter.write(f'{self.ISBN}')

  def __str__(self):
    return f'Book Info\nISBN: {self.ISBN}\ntitle: {self.title}\nauthor: {self.author}\nbook is {'available' if self.is_available else 'not available'}'
