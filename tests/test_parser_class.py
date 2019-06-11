#! /usr/bin/env python

"""
file testing parser_class.py
"""

from grandpybot.parser_class import Parser

class Params:
    """
    Class defining the params for Parser()
    """
    # sentance 1
    search = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms stp ?"
    extracted_information = 'OpenClassrooms stp ?'
    removed_punctuation = 'OpenClassrooms stp  '
    dict_request = {'information': 'OpenClassrooms  ', 'type_search': 'place description'}
    # sentance 2
    search_1 = "La tour Eiffel please ?"
    extracted_information_1 = 'La tour Eiffel please ?'
    removed_punctuation_1 = 'La tour Eiffel please  '
    dict_request_1 = {'information': 'La tour Eiffel  ', 'type_search': 'place description'}
    # sentance 3 : place
    search_2 = '4 rue renard, 94510 La Queue en Brie'
    extracted_information_2 = 'renard, 94510 La Queue en Brie'
    removed_punctuation_2 = 'renard  94510 La Queue en Brie'
    dict_request_2 = {'information': 'renard  94510 La Queue en Brie', 'type_search': 'place'}
    # sentance 4 : description
    bleach = "Zaraki Kenpachi"
    bleach_extracted_information = "Zaraki Kenpachi"
    bleach_removed_punctuation = "Zaraki Kenpachi"
    bleach_dict_request = {'information': 'Zaraki Kenpachi', 'type_search': 'description'}
    # error requests
    random_search = 'cmFuZG9tIGRhdGEgZm9yIGZha2Ugc2VhcmNo'
    random_search_dict = \
        {'information': 'cmFuZG9tIGRhdGEgZm9yIGZha2Ugc2VhcmNo', 'type_search': 'error'}
    punctuation = '-_,;:!()'
    punctuation_removed_punctuation = '        '
    punctuation_dict_request = {'information': '        ', 'type_search': 'error'}
    empty_search = ' '
    empty_dict_request = {'information': ' ', 'type_search': 'error'}

class TestParser:
    """
    Test the methode who parsing the search
    """
    def test_extract_info_request(self):
        """
        Extract good information from search and return information
        """
        self.params = Params()
        self.parser = Parser(self)
        assert self.parser.extract_information_request(self.params.search) == \
               self.params.extracted_information
        assert self.parser.extract_information_request(self.params.search_1) == \
               self.params.extracted_information_1
        assert self.parser.extract_information_request(self.params.search_2) == \
               self.params.extracted_information_2
        assert self.parser.extract_information_request(self.params.bleach) \
               == self.params.bleach_extracted_information
        assert self.parser.extract_information_request(self.params.random_search) == \
               self.params.random_search
        assert self.parser.extract_information_request(self.params.punctuation) == \
               self.params.punctuation
        assert self.parser.extract_information_request(self.params.empty_search) == \
               self.params.empty_search


    def test_remove_punctuation(self):
        """
        remove punctuation from search and return whitespace*
        """
        self.params = Params()
        self.parser = Parser(self)
        extracted_information = self.params.extracted_information
        assert self.parser.remove_punctuation(extracted_information) == \
               self.params.removed_punctuation
        assert self.parser.remove_punctuation(self.params.extracted_information_1) == \
               self.params.removed_punctuation_1
        assert self.parser.remove_punctuation(self.params.extracted_information_2) == \
               self.params.removed_punctuation_2
        assert self.parser.remove_punctuation(self.params.bleach_extracted_information) == \
               self.params.bleach_removed_punctuation
        assert self.parser.remove_punctuation(self.params.random_search) == \
               self.params.random_search
        assert self.parser.remove_punctuation(self.params.punctuation) == \
               self.params.punctuation_removed_punctuation
        assert self.parser.remove_punctuation(self.params.empty_search) == \
               self.params.empty_search


    def test_remove_word_please(self):
        """
        remove word in wordèplease from search and return dict_request
        """
        self.params = Params()
        self.parser = Parser(self)
        assert self.parser.remove_word_please(self.params.removed_punctuation) == \
               self.params.dict_request
        assert self.parser.remove_word_please(self.params.removed_punctuation_1) == \
               self.params.dict_request_1
        assert self.parser.remove_word_please(self.params.removed_punctuation_2) == \
               self.params.dict_request_2
        assert self.parser.remove_word_please(self.params.bleach_removed_punctuation) == \
               self.params.bleach_dict_request
        assert self.parser.remove_word_please(self.params.random_search) == \
               self.params.random_search_dict
        assert self.parser.remove_word_please(self.params.empty_search) == \
               self.params.empty_dict_request
