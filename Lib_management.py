from abc import ABC, abstractmethod

class Library(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def issue(self):
        """Issue the library item."""
        pass

class Books(Library):

    def issue(self):
        """Issue the library item."""
        print("  ")
        print(f"Book '{self.name}' is issued for 14 days")

# Main program 
book_name = input("Enter the book name:")

books = Books(book_name)

books.issue()