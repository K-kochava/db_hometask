import os
import shutil
import sqlite3
import logging
from xml.dom import minidom
from book import Book, Item
logging.basicConfig(level=logging.INFO)


def main(path, incorrect_folder_path):
    create_dir()
    db_create()
    for f_name in os.listdir(path):
        try:
            if f_name.endswith('.fb2'):
                item = get_item(path + f_name)
                books = get_book(path + f_name)
                db_add_item(item)
                for book in books:
                    db_add_book(book)
            else:
                try:
                    shutil.move(path + f_name, incorrect_folder_path)
                except OSError as err:
                    print('Process stopped')
                else:
                    logging.warning('File is not fb2. File is:' + f_name)
        except KeyboardInterrupt as err:
            print('process aborted')
        finally:
            logging.info('Book and item created')
    conn = sqlite3.connect('test.db')
    with conn:
        print("1. All items&info:")
        select_all_input_file_info(conn)

        print("2. Book info:")
        select_all_book_info(conn)


def create_dir():
    dir = os.path.join('/Users/c-halaks/Documents/incorrect_input')
    if not os.path.exists(dir):
        os.mkdir(dir)
        logging.info('Created directory:' + dir)


def get_text(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
        else:
            rc.append(get_text(node.childNodes))
    return ''.join(rc)


def get_item(file_path):
    xmldoc = minidom.parse(file_path)
    itemlist = xmldoc.getElementsByTagName('section')
    book_name = xmldoc.getElementsByTagName('book-title')[0].firstChild.nodeValue
    logging.info('Book name is:' + book_name)
    text = get_text(itemlist)
    words = text.split()
    count_p = xmldoc.getElementsByTagName('p').length
    count_words = len(words)
    count_letters = len(text)
    words_with_capital_letter = 0
    words_without_capital_letter = 0
    for word in words:
        if word.istitle():
            words_with_capital_letter += 1
        else:
            words_without_capital_letter += 1

    return Item(book_name, count_p, count_words, count_letters, words_with_capital_letter, words_without_capital_letter)
    logging.info('Count of words in lowercase is: ' + str(words_without_capital_letter))
    logging.info('Count of words with capital letter is:' + str(words_with_capital_letter))


def get_book(file_path):
    xmldoc = minidom.parse(file_path)
    itemlist = xmldoc.getElementsByTagName('section')
    text = get_text(itemlist)
    words = text.split()

    words_list = []
    for word in words:
        words_list.append(Book(word, words.count(word), sum(1 for c in word if c.isupper())))
    print(words_list)
    return words_list
    logging.info('Book info is' + words_list)


def db_create():
    try:
        conn = sqlite3.connect('test.db')
        conn.execute('''CREATE TABLE IF NOT EXISTS INPUT_FILES_INFO
                 (BOOK_NAME  CHAR(155) PRIMARY KEY     NOT NULL,
                 NUMBER_OF_PARAGRAPH            INT,
                 NUMBER_OF_WORDS        INT,
                 NUMBER_OF_LETTERS        INT,
                 WORDS_WITH_CAPITAL_LETTERS        INT,
                 WORDS_IN_LOWERCASE        INT);''')
        logging.info('Table INPUT_FILES_INFO created successfully');

        conn.execute('''CREATE TABLE IF NOT EXISTS BOOK_INFO
                    (WORD CHAR(155)     NOT NULL,
                    COUNT           INT,
                    COUNT_UPPERCASE            INT);''')
        logging.info('Table BOOK_INFO created successfully');
    except sqlite3.Error as e:
        print(e)
    finally:
        logging.info('Opened database successfully');
        conn.close()
    # conn.execute('''DROP TABLE INPUT_FILES_INFO;''')
    # conn.close()


def db_add_item(item):
    try:
        conn = sqlite3.connect('test.db')
        sql = '''INSERT INTO INPUT_FILES_INFO(BOOK_NAME, NUMBER_OF_PARAGRAPH, NUMBER_OF_WORDS, NUMBER_OF_LETTERS, 
        WORDS_WITH_CAPITAL_LETTERS, WORDS_IN_LOWERCASE) VALUES(?,?,?,?,?,?) '''
        records_to_insert = (item.book_name, item.number_of_paragraph, item.number_of_words, item.number_of_letters,
                             item.words_with_capital_letters, item.words_in_lowercase)
        cur = conn.cursor()
        cur.execute(sql, records_to_insert)
        conn.commit()
        logging.info('Inserted into INPUT_FILES_INFO successfully');
        return cur.lastrowid
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()


def db_add_book(book):
    try:
        conn = sqlite3.connect('test.db')
        sql = ''' INSERT INTO BOOK_INFO(WORD, COUNT, COUNT_UPPERCASE)
                          VALUES(?,?,?) '''
        records_to_insert = (book.word, book.count, book.count_uppercase)
        cur = conn.cursor()
        cur.execute(sql, records_to_insert)
        conn.commit()
        logging.info('Inserted into BOOK_INFO successfully');
        return cur.lastrowid
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()


def select_all_input_file_info(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM INPUT_FILES_INFO")
    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_all_book_info(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM BOOK_INFO")
    rows = cur.fetchall()

    for row in rows:
        print(row)


main('/Users/c-halaks/Documents/task/', '/Users/c-halaks/Documents/incorrect_input/')