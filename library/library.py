import os
from user import User
from book import Book
import json

USERS_LIST = 'data/users.json'
BOOKS_LIST = 'data/books.json'

class Library:
  if not os.path.exists(USERS_LIST):
    with open(USERS_LIST, 'w') as users_file:
      users_file.write('{}')
  if not os.path.exists(BOOKS_LIST):
    with open(BOOKS_LIST, 'w') as books_file:
      books_file.write('{}')

  def __init__(self, books_list =BOOKS_LIST, users_list =USERS_LIST):
    self.books_list = books_list
    self.users_list = users_list

  def add_book(self, book):
    with open(self.books_list, 'r') as books_file:
      books = json.load(books_file)
      books[book.ISBN] = vars(book)
      with open(self.books_list, 'w') as books_list:
        json.dump(books, books_list, indent='\t')

  def add_user(self, name, id):
    user = User(name, id)
    with open(self.users_list, 'r') as users_file:
      users = json.load(users_file)
      if not str(user.id) in users.keys():
        users[user.id] = vars(user)
        with open(self.users_list, 'w') as users_list:
          json.dump(users, users_list, indent="\t")
  
  def borrow_book(self, user_id, book_isbn):
    with open()
  
  def return_book(self, user_id, book_isbn):
    return
  
  def list_available_books(self):
    with open(self.books_list, 'r') as books_file:
      books = json.load(books_file)
    return [book['title'] for k,book in books.items() if book['is_available']]
  # search by 'title', or 'author'
  def search_book(self, search_by, search_value):
    with open(self.books_list, 'r') as books_file:
      books = json.load(books_file)
    if search_by == 'title':
      return [{book['title'], book['author']} for k,book in books.items() if search_value.lower() in book['title'].lower()]
    elif search_by == 'author':
      return [{book['title'], book['author']} for k,book in books.items() if search_value.lower() in book['author'].lower()]


if __name__ == "__main__":
  b = Library()

  b.add_user('efraim', '326080025')
  b.add_book(Book('Tora', 'gad', True))
  print(b.list_available_books())

  print(b.list_available_books())