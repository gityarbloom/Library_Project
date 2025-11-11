class User:
    def __init__(self, name, id):
        self. name = name
        self.id = id
        self.borrowed_books = []

    def __str__(self):
        return f"USER DETAILS: \nNAME: {self.name} \nID; {self.id} \nBORROWED BOOKS: {self.borrowed_books}\n"

    def get_info(self):
        return self.__str__()