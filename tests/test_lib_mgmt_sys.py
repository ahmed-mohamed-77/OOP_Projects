import pytest
from oo_projects.source.lib_mgmt_sys import FictionBook, NonFictionBook, Library


@pytest.fixture
def library_with_books():
    library = Library()
    books = [
        FictionBook(
            "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997, "Fantasy"
        ),
        FictionBook(
            "Harry Potter and the Chamber of Secrets", "J.K. Rowling", 1998, "Fantasy"
        ),
        FictionBook(
            "Harry Potter and the Prisoner of Azkaban", "J.K. Rowling", 1999, "Fantasy"
        ),
        FictionBook(
            "Harry Potter and the Goblet of Fire", "J.K. Rowling", 2000, "Fantasy"
        ),
        FictionBook(
            "Harry Potter and the Order of the Phoenix", "J.K. Rowling", 2003, "Fantasy"
        ),
        FictionBook(
            "Harry Potter and the Half-Blood Prince", "J.K. Rowling", 2005, "Fantasy"
        ),
        FictionBook(
            "Harry Potter and the Deathly Hallows", "J.K. Rowling", 2007, "Fantasy"
        ),
        NonFictionBook("The Theory of Everything", "Stephen Hawking", 1988, "Physics"),
        NonFictionBook(
            "The Immortal Life of Henrietta Lacks", "Rebecca Skloot", 2010, "Science"
        ),
        NonFictionBook(
            "Sapiens: A Brief History of Humankind",
            "Yuval Noah Harari",
            2011,
            "History",
        ),
        NonFictionBook("The Selfish Gene", "Richard Dawkins", 1976, "Biology"),
    ]

    for book in books:
        library.add_book(book)

    return library


@pytest.mark.parametrize(
    "author, expected_value",
    [
        (
            "J.K. Rowling",
            [
                "Harry Potter and the Philosopher's Stone",
                "Harry Potter and the Chamber of Secrets",
                "Harry Potter and the Prisoner of Azkaban",
                "Harry Potter and the Goblet of Fire",
                "Harry Potter and the Order of the Phoenix",
                "Harry Potter and the Half-Blood Prince",
                "Harry Potter and the Deathly Hallows",
            ],
        ),
        ("Stephen Hawking", ["The Theory of Everything"]),
        ("Rebecca Skloot", ["The Immortal Life of Henrietta Lacks"]),
        ("Yuval Noah Harari", ["Sapiens: A Brief History of Humankind"]),
        ("Richard Dawkins", ["The Selfish Gene"]),
    ],
)
def test_search_by_author(library_with_books, author, expected_value):
    result = library_with_books.search_by_author(author)
    assert [book.title for book in result] == expected_value


@pytest.mark.parametrize(
    "start_year, end_year, expected_value",
    [
        (
            1976,
            2000,
            [
                "Harry Potter and the Philosopher's Stone",
                "Harry Potter and the Chamber of Secrets",
                "Harry Potter and the Prisoner of Azkaban",
                "Harry Potter and the Goblet of Fire",
                "The Theory of Everything",
                "The Selfish Gene",
            ],
        ),
        (
            2001,
            2005,
            [
                "Harry Potter and the Order of the Phoenix",
                "Harry Potter and the Half-Blood Prince",
            ],
        ),
        (
            2006,
            2011,
            [
                "Harry Potter and the Deathly Hallows",
                "The Immortal Life of Henrietta Lacks",
                "Sapiens: A Brief History of Humankind",
            ],
        ),
    ],
)
def test_search_by_year(library_with_books, start_year, end_year, expected_value):
    result = library_with_books.search_by_year(start_year, end_year)
    assert [book.title for book in result] == expected_value


# Test adding a book to the library
def test_add_book(library_with_books):
    new_book = FictionBook("New Book", "New Author", 2023, "New Genre")
    initial_book_count = len(library_with_books.books)
    library_with_books.add_book(new_book)
    assert len(library_with_books.books) == initial_book_count + 1
    assert new_book in library_with_books.books


# Test removing a book from the library
def test_remove_book(library_with_books):
    book_to_remove = library_with_books.books[0]  # Remove the first book in the library
    initial_book_count = len(library_with_books.books)
    library_with_books.remove_book(book_to_remove)
    assert len(library_with_books.books) == initial_book_count - 1
    assert book_to_remove not in library_with_books.books
