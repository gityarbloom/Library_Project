class User:
    def __init__(self, name, id):
        self. name = name
        self.id = id
        self.borrowed_books = []
        # self.book_lending_history = []
    
    def borrow_books(self, *books):
        for book in books:
            self.borrowed_books.append(book)
    #        self.book_lending_history.append(book for book in books)

    def __str__(self):
        return f"\nUSER DETAILS: \nNAME: {self.name} \nID; {self.id} \nBORROWED BOOKS: {self.borrowed_books}\n"

    def get_info(self):
        return self.__str__()


# a1 = User("israel")
# a1.borrow_books("aaa", "bbb", "ccc")
# print(a1)
# print(a1.get_info())