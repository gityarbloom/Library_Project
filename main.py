from library.library import *

def library_menu(library):
    choice = None 
    while choice != "7": 
        print("\n\nWelcom to 'NIMRODY LIBRARY': \nEnter 1 to add  a book \nEnter 2 for adding new user \nEnter 3 Borrow Book \nto Save & Exit Enter 7 ") 
        choice = input("\nPlease enter your choice: ") 
    
        if choice == "1":
            print("\nNew book! So exciting!")
            author = input("Please write the author name: ")
            title = input("We are almost there... All thet remains is to apdate the book title: ")
            new_book = Book(author, title)
            library.add_book(new_book)
            print(new_book)
            
        #     pass 
        # elif choice == "2": 
        #     # ask for user info and add user 
        #     pass 
    
        # elif choice == "7": 
        #     # save data and exit 
        #     break 
        # else: 
        #     print("Invalid choice, try again.")


if __name__ == "__main__":
    SIVATA_LIBRARY = Library()
    library_menu(SIVATA_LIBRARY)
