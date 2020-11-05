class Book(object):

    def __init__(self, book_name, number_of_paragraph, number_of_words, number_of_letters, words_with_capital_letters, words_in_lowercase):
        self.book_name = book_name
        self.number_of_paragraph = number_of_paragraph
        self.number_of_words = number_of_words
        self.number_of_letters = number_of_letters
        self.words_with_capital_letters = words_with_capital_letters
        self.words_in_lowercase = words_in_lowercase


class Word(object):

    def __init__(self, word, count, count_uppercase):
        self.word = word
        self.count = count
        self.count_uppercase = count_uppercase
