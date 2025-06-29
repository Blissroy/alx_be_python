class Book:
    """Base class representing a book."""
    def __init__(self, title: str, author: str):
        """
        Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author

    def __str__(self) -> str:
        """Return basic book information."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initialize an EBook instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            file_size (int): Size of the eBook file in KB
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self) -> str:
        """Return eBook information including file size."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a physical printed book."""
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initialize a PrintBook instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            page_count (int): Number of pages in the book
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self) -> str:
        """Return print book information including page count."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class demonstrating composition by managing a collection of books."""
    def __init__(self):
        """Initialize a Library with an empty list of books."""
        self.books = []

    def add_book(self, book: Book):
        """
        Add a book to the library.
        
        Args:
            book (Book): A Book, EBook, or PrintBook instance
        """
        self.books.append(book)

    def list_books(self):
        """Print details of all books in the library."""
        for book in self.books:
            print(book)
