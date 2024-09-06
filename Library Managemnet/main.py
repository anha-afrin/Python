class Library:
    def __init__(self, list):
        self.booklist=list
    def display_books(self):
        print("We have the following books in our library.")
        for i in self.booklist:
            print(i)
    
books= Library(["Harry Poter p1", "The Dark Title", "You Can Win p1", "The professionals", "All about science"])
while True:

    print("Welcome to the library management system.\nPlease enter your name: ")

    username = input()

    print(f"Hello, {username}! Please select an option.")

    print("1. Display Books")

    print("2. Borrow Book")

    print("3. Return Book")

    print("4. Add a Book")

    print("5. Exit")

    user_choice = input("Please enter the number of your choice: ")

    if user_choice == "1":

        books.display_books()

    elif user_choice == "2":

        print("What book do you want to borrow?")

    elif user_choice == "3":

        print("Which book do you want to return?")

    elif user_choice == "4":

        print("Which book do you want to add?")

    elif user_choice == "5":

        print("Thank you for using the library management system. Goodbye!")

        break

    else:

        print("Please enter a valid choice.")