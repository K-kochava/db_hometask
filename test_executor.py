import logging
import sqlite3

from test import get_words, get_books, test_size, test_book_size, test_count_more_than_0, test_type_book_name, \
    test_type_number_of_paragraph, test_type_number_of_words, test_type_number_of_letters, \
    test_type_words_with_capital_letters, test_type_words_in_lowercase, test_type_word, test_type_count, \
    test_type_count_uppercase


def execute_tests():
    try:
        conn = sqlite3.connect('test.db')
        words_list = get_words(conn)
        books_list = get_books(conn)
        test_size(words_list)
        test_book_size(books_list)
        test_count_more_than_0(words_list)
        test_type_book_name(books_list)
        test_type_number_of_paragraph(books_list)
        test_type_number_of_words(books_list)
        test_type_number_of_letters(books_list)
        test_type_words_with_capital_letters(books_list)
        test_type_words_in_lowercase(books_list)
        test_type_word(words_list)
        test_type_count(words_list)
        test_type_count_uppercase(words_list)
    except sqlite3.Error as e:
        print(e)
    finally:
        logging.info('Closed connection')
        conn.close()


def main():
    execute_tests()


main()


