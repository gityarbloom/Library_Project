from user import User
from book import Book

class Library:
  def __init__(self, books_list, users_list):
    self.books_list = books_list
    self.users_list = users_list

  def add_book(self, book):
    self.books_list.append(book)

  def add_user(self, user):
    self.users_list.append(user)

  def borrow_book(self, user_id, book_isbn):
    return
  def return_book(self, user_id, book_isbn):
    return
  def list_available_books(self):
    return
  def search_book(self, search_by):
    return
