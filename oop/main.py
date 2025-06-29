from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the _str_ method
    print(my_book)  # Expected: 1984 by George Orwell, published in 1949

    # Demonstrating the _repr_ method
    print(repr(my_book))  # Expected: Book('1984', 'George Orwell', 1949)

    # Deleting a book instance to trigger _del_
    del my_book

if _name_ == "_main_":
    main()
