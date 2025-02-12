import LibraryFunctions

def main():
    filename = "Library.txt"
    books = LibraryFunctions.load_record(filename)


    print("Hello there! Welcome to the library.\n")
    print("What book would you like to explore today?\n")

    while True:

        print("1. Add a book to the library")
        print("2. View all books")
        print("3. Borrow a book")
        print("4 Return a book")
        print("5.Exit")

        choice = input("Choose an option from 1-5:")

        if choice == "1":
            title = input("Enter the book's title:").strip().lower()
            author = input("Enter the book's author:").strip().lower()
            status = "available"

            book = LibraryFunctions.add_books(title, author, status)

            content = f"{book['title']} by {book['author']} added to the library"
            LibraryFunctions.append_records(filename, content)

            print(f"Book added: {book}")
        elif choice == "2":
            books = LibraryFunctions.view_books()

            if books:
                print("Here are the books in the library:\n")
                for i, book in enumerate(books, start=1):
                    print(f"{i}. {book['title']} by {book['author']}. Status: {book['status']}")
            else:
                print("No books are currently in the library")
        elif choice == "3":
            title = input("Enter a book title:").strip().lower()

            book = LibraryFunctions.borrow_books(title)

            if book:
                if book['status'] == "available":
                    print(f"You have borrowed {book['title']} by {book['author']}.")


                    content = f"{book['title']} by {book['author']} borrowed"
                    LibraryFunctions.append_records(filename, content)

                    book['status'] = "borrowed"


                elif book["status"] == "borrowed":
                    print("This book is yet to be returned as you had already borrowed it.")
            else:
                print("Book is not in the library")
        elif choice == "4":
            title = input("Enter a book title:")

            book = LibraryFunctions.return_books(title)

            if book:
                if book['status'] == "borrowed":
                    print(f"You have returned {book['title']} by {book['author']}")

                    content = f"{book['title']} by {book['author']} returned"
                    LibraryFunctions.append_records(filename, content)

                    book['status'] = "available"
                elif book['status'] == "available":
                    print("Book wasn't borrowed")
            else:
                print("Book is not in the library")
        elif choice == "5":
            print("Thank you for using the library\n")
            print("Hope to see you soon!")
            break
        else:
            print("Invalid choice. Please choose between 1-5")







if __name__ == "__main__":
    main()