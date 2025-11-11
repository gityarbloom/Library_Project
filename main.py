from library.library import *


def library_menu(library):
    choice = input("\nWelcom to 'NIMRODY LIBRARY' \nTo signin press on the 'ENTER KEY', \nTo Save & Exit Enter 7: ") 
    while choice != "7": 
        print("Enter 1 to add a book \nEnter 2 for adding new user \nEnter 3 to borrow a book")
        choice = input("\nPlease enter your choice: ") 
        if choice == "1":
            print("\nNew book! Grate!")
            author = input("Please write the author name: ")
            title = input("We are almost there... All thet remains is to apdate the book title: ")
            new_book = Book(author, title)
            library.add_book(new_book)
            print(f"\n*****************************\nGrate! We add a new book to library! \n{new_book}\n*****************************\n")
            print("To Save & Exit Enter 7 \nFor return to menu press on the 'ENTER KEY'")
            choice = input()
        elif choice == "2": 
            print("\nNew user! So exciting!")
            name = input("Please choice a user name: ")
            id = input("We are almost there... All thet remains is to apdate the ID user: ")
            new_user = library.add_user(name, id)
            print(f"\n*****************************\nWelcome {name}! \nYor {new_user}\n*****************************\n")
            print("To Save & Exit Enter 7 \nFor return to menu press on the 'ENTER KEY'")
            choice = input()
        elif choice == "7":
            print("\nGood Bye! Have a nice day!")
            break 
        else: 
            print("Invalid choice, try again.")


if __name__ == "__main__":
    SIVATA_LIBRARY = Library()
    library_menu(SIVATA_LIBRARY)