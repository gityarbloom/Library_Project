import os
from library.user import User
from library.book import Book
from library.json_handeling import JsonHandeling


USERS_PATH_FILE = 'data/users.json'
BOOKS_PATH_FILE = 'data/books.json'


class Library:
  for file in [USERS_PATH_FILE, BOOKS_PATH_FILE]:
    if not os.path.exists(file):
      JsonHandeling.write_json(file)

  def __init__(self, books_file =BOOKS_PATH_FILE, users_file =USERS_PATH_FILE):
    self.books_file = books_file
    self.users_file = users_file

  def get_books_list(self):
      return JsonHandeling.read_json(self.books_file)

  def get_users_list(self):
      return JsonHandeling.read_json(self.users_file)

  def add_book(self, book):
    books = self.get_books_list()
    books[book.ISBN] = vars(book)
    JsonHandeling.write_json(BOOKS_PATH_FILE, books)

  def add_user(self, name, id):
    user = User(name, id)
    users = self.get_users_list()
    if not str(user.id) in users.keys():
      users[user.id] = vars(user)
      JsonHandeling.write_json(USERS_PATH_FILE, users)
      return user.get_info()
  
  def borrow_book(self, user_id, book_isbn):
    users = self.get_users_list()
    books = self.get_books_list()
    if books[book_isbn]['is_available']:
      users[user_id]['borrowed_books'].append(books[book_isbn])
      JsonHandeling.write_json(USERS_PATH_FILE, users)
      books[book_isbn]['is_available'] = False
      JsonHandeling.write_json(BOOKS_PATH_FILE, books)

  def return_book(self, user_id, book_isbn):
    users = self.get_users_list()
    books = self.get_books_list()
    to_remove = books[book_isbn].copy()
    to_remove['is_available'] = True
    users[user_id]['borrowed_books'].remove(to_remove)
    JsonHandeling.write_json(USERS_PATH_FILE, users)
    books[book_isbn]['is_available'] = True
    JsonHandeling.write_json(BOOKS_PATH_FILE, books)
  
  def list_available_books(self): 
    return [book['title'] for k,book in self.get_books_list().items() if book['is_available']]
  # search by 'title', or 'author'
  def search_book(self, search_by, search_value):
    books = self.get_books_list()
    if search_by == 'title':
      return [{book['title'], book['author']} for k,book in books.items() if search_value.lower() in book['title'].lower()]
    elif search_by == 'author':
      return [{book['title'], book['author']} for k,book in books.items() if search_value.lower() in book['author'].lower()]