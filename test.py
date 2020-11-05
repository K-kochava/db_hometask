import logging

from book import Book
from book import Word


def get_books(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM INPUT_FILES_INFO")
    rows = cur.fetchall()
    books_list = []
    for row in rows:
        books_list.append(Book(row[0], row[1], row[2], row[3], row[4], row[5]))
    return books_list


def get_words(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM BOOK_INFO")
    rows = cur.fetchall()
    words_list = []
    for row in rows:
        words_list.append(Word(row[0], row[1], row[2]))
    return words_list


def test_size(words_list):
    assert len(words_list) > 0


def test_book_size(books_list):
    assert len(books_list) > 0


def test_count_more_than_0(words_list):
    for word in words_list:
        assert len(word.word) > 0


def assert_rows(rows, assert_type):
    for row in rows:
        logging.info('Assert type of %s', str(row[0]))
        assert isinstance(row[0], assert_type)


def test_type_book_name(books_list):
    for book in books_list:
        assert type(book.book_name) == str


def test_type_number_of_paragraph(books_list):
    for book in books_list:
        assert type(book.number_of_paragraph) == int


def test_type_number_of_words(books_list):
    for book in books_list:
        assert type(book.number_of_words) == int


def test_type_number_of_letters(books_list):
    for book in books_list:
        assert type(book.number_of_letters) == int


def test_type_words_with_capital_letters(books_list):
    for book in books_list:
        assert type(book.words_with_capital_letters) == int


def test_type_words_in_lowercase(books_list):
    for book in books_list:
        assert type(book.words_in_lowercase) == int


def test_type_word(words_list):
    for word in words_list:
        assert type(word.word) == str


def test_type_count(words_list):
    for word in words_list:
        assert type(word.count) == int


def test_type_count_uppercase(words_list):
    for word in words_list:
        assert type(word.count_uppercase) == int
