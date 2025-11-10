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
  # search by 'title', or 'author'
  def search_book(self, search_by, search_value):
    with open('data/books.json', 'r') as books_file:
      books = json.load(books_file)
    if search_by == 'title':
      return [{book['title'], book['author']} for k,book in books.items() if search_value.lower() in book['title'].lower()]
    elif search_by == 'author':
      return [{book['title'], book['author']} for k,book in books.items() if search_value.lower() in book['author'].lower()]
b = Library([], 'data/users.json')

b.add_user('efraim', '326080025')
b.add_book(Book('Book1', 'Author1',True))
print(b.list_available_books())

print(b.list_available_books())