import logging
import sqlite3


def execute_tests():
    try:
        conn = sqlite3.connect('test.db')
        test_size(conn)
        test_book_size(conn)
        test_count_more_than_0(conn)
        test_type_book_name(conn)
        test_type_number_of_paragraph(conn)
        test_type_number_of_words(conn)
        test_type_number_of_letters(conn)
        test_type_words_with_capital_letters(conn)
        test_type_words_in_lowercase(conn)
        test_type_word(conn)
        test_type_count(conn)
        test_type_count_uppercase(conn)
    except sqlite3.Error as e:
        print(e)
    finally:
        logging.info('Closed connection')
        conn.close()


def test_size(conn):
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM BOOK_INFO")
    rows = cur.fetchall()
    assert len(rows) != 0


def test_book_size(conn):
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM INPUT_FILES_INFO")
    rows = cur.fetchall()
    assert len(rows) != 0


def test_count_more_than_0(conn):
    cur = conn.cursor()
    cur.execute("SELECT COUNT(DISTINCT WORD) FROM BOOK_INFO")
    rows = cur.fetchall()
    assert len(rows) >= 0


def assert_rows(rows, assert_type):
    for row in rows:
        logging.info('Assert type of %s', str(row[0]))
        assert isinstance(row[0], assert_type)


def test_type_book_name(conn):
    cur = conn.cursor()
    rows = cur.execute("SELECT BOOK_NAME FROM INPUT_FILES_INFO").fetchall()
    assert_rows(rows, str)


def test_type_number_of_paragraph(conn):
    cur = conn.cursor()
    rows = cur.execute("SELECT NUMBER_OF_PARAGRAPH FROM INPUT_FILES_INFO")
    assert_rows(rows, int)


def test_type_number_of_words(conn):
    cur = conn.cursor()
    rows = cur.execute("SELECT NUMBER_OF_WORDS FROM INPUT_FILES_INFO")
    assert_rows(rows, int)


def test_type_number_of_letters(conn):
    cur = conn.cursor()
    rows = cur.execute("SELECT NUMBER_OF_LETTERS FROM INPUT_FILES_INFO")
    assert_rows(rows, int)


def test_type_words_with_capital_letters(conn):
    cur = conn.cursor()
    rows = cur.execute("SELECT WORDS_WITH_CAPITAL_LETTERS FROM INPUT_FILES_INFO")
    assert_rows(rows, int)


def test_type_words_in_lowercase(conn):
    cur = conn.cursor()
    rows = cur.execute("SELECT WORDS_IN_LOWERCASE FROM INPUT_FILES_INFO")
    assert_rows(rows, int)


def test_type_word(conn):
    cur = conn.cursor()
    rows = cur.execute("SELECT WORD FROM BOOK_INFO")
    assert_rows(rows, str)


def test_type_count(conn):
    cur = conn.cursor()
    rows = cur.execute("SELECT COUNT FROM BOOK_INFO")
    assert_rows(rows, int)


def test_type_count_uppercase(conn):
    cur = conn.cursor()
    rows = cur.execute("SELECT COUNT_UPPERCASE FROM BOOK_INFO")
    assert_rows(rows, int)



