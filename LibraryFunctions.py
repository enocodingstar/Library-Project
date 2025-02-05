def load_record(filename):
    """Load the file when the program starts"""
    try:
        with open(filename, "w") as file:
            file.write("All library records are saved here./n")
    except FileExistsError:
        print(f"File {filename} already exists")
    return[]


books = []
def add_books(title, author, status):
    """Add books to the library"""
    global books
    book ={"title": title, "author": author, "status": status}
    books.append(book)
    return book

def view_books():
    """Return all saved books"""
    return books

def borrow_books(title):
    """Borrow a book from the library"""
    for book in books:
        if book["title"] == title:
            return book
    return None
        
def return_books(title):
    """Return a book to the library"""
    for book in books:
        if book["title"] == title:
            return book
    return None
        

        
def append_records(filename, content):
    """Add records to a file"""
    try:
        with open(filename, "a") as file:
            file.write(content + "/n")
    except Exception as e:
        print("An error occured")
    return filename, content