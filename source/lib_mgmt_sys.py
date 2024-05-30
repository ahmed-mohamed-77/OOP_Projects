class Book:
    """Description:
    This represents a library management system that allows you to collect books. The system 
    provides functionality for adding books, searching for books by author, and searching for 
    books within a specific year range.
    """

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
    
    def display_info(self):
        """Displays the book's information."""
        print(f"The book name: {self.title}\nThe author: {self.author}\nYear: {self.year}")


class FictionBook(Book):
    """Represents a fiction book with a specific genre."""

    def __init__(self, title: str, author: str, year: int, genre: str):
        super().__init__(title, author, year)
        self.genre = genre
    
    def info(self):
        """Displays the fiction book's information, including its genre."""
        super().display_info()
        print(f"The book genre: {self.genre}")


class NonFictionBook(Book):
    """Represents a non-fiction book with a specific topic."""

    def __init__(self, title: str, author: str, year: int, topic: str):
        super().__init__(title, author, year)
        self.topic = topic
        
    def info(self):
        """Displays the non-fiction book's information, including its topic."""
        super().display_info()
        print(f"The book topic: {self.topic}")


class Library:
    """Represents a library that can store and manage books."""

    def __init__(self) -> None:
        self.books = []
    
    def add_book(self, book: object):
        """Adds a book to the library."""
        self.books.append(book)
    
    def remove_book(self, book: object):
        """Removes a book from the library."""
        self.books.remove(book)
    
    def display_books(self):
        """Displays all books in the library."""
        for book in self.books:
            book.info()
            print()
            
    def search_by_author(self, author: str):
        """Searches for books by a specific author."""
        found_books = [book for book in self.books if book.author == author]
        
        if found_books:
            print(f"Books by {author}:")
            for book in found_books:
                book.info()
                print()
        else:
            print(f"No books found by {author}")
        return found_books
    
    def search_by_year(self, start_year: int, end_year: int):
        """Searches for books published within a specific year range."""
        found_books = [book for book in self.books if start_year <= book.year <= end_year]
        
        if found_books:
            print(f"Books between {start_year} and {end_year}:")
            for book in found_books:
                book.info()
                print()
        else:
            print(f"No books found between {start_year} and {end_year}")
        return found_books

if __name__ == "__main__":
    library = Library()
    library.add_book(FictionBook("1984", "George Orwell", 1949, "Dystopian"))
    library.add_book(NonFictionBook("Sapiens", "Yuval Noah Harari", 2011, "History"))
    library.add_book(FictionBook("1984", "George Orwell", 1949, "Dystopian"))
    library.add_book(NonFictionBook("Sapiens", "Yuval Noah Harari", 2011, "History"))
    library.add_book(FictionBook("To Kill a Mockingbird", "Harper Lee", 1960, "Drama"))
    library.add_book(NonFictionBook("The Selfish Gene", "Richard Dawkins", 1976, "Science"))
    # library.display_books()
    # library.search_by_author('Yuval Noah Harari')
    library.search_by_year(1950, 1980)

