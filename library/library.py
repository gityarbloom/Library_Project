from user import User
from book import Book
import json


class Library:
  def __init__(self, books_list, users_list):
    self.books_list = books_list
    self.users_list = users_list

  def add_book(self, book):
    with open('data/books.json', 'r') as books_file:
      books = json.load(books_file)
      if not str(book.ISBN) in books.keys():
        books[book.ISBN] = vars(book)
        with open('data/books.json', 'w') as books_list:
          books_list.write(json.dumps(books, indent="\t"))

  def add_user(self, name, id):
    user = User(name, id)
    with open('data/users.json', 'r') as users_file:
      users = json.load(users_file)
      if not str(user.id) in users.keys():
        users[user.id] = vars(user)
        with open('data/users.json', 'w') as books_list:
          books_list.write(json.dumps(users, indent="\t"))
  
  def borrow_book(self, user_id, book_isbn):
    return
  
  def return_book(self, user_id, book_isbn):
    return
  
  def list_available_books(self):
    with open('data/books.json', 'r') as books_file:
      books = json.load(books_file)
    return [book['title'] for k,book in books.items() if book['is_available']]
  
  def search_book(self, search_by):
    return
  
b = Library([], 'data/users.json')
b.add_book(Book('tit', 'a', False))
b.add_book(Book('tit', 'a', False))
print(b.add_user('efraim', '123'))
print(b.add_user('efraim', '2'))
print(b.list_available_books())