class Book:
    def _init_(self, title: str, author: str, year: int):
        """Initialize a Book instance with title, author, and year.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year
        """
        self.title = title
        self.author = author
        self.year = year

    def _del_(self):
        """Destructor that prints a message when the object is deleted."""
        print(f"Deleting {self.title}")

    def _str_(self) -> str:
        """Return a user-friendly string representation of the book.
        
        Returns:
            str: String in format "Title by Author, published in Year"
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def _repr_(self) -> str:
        """Return an official string representation that can recreate the object.
        
        Returns:
            str: String that looks like a Book constructor call
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
