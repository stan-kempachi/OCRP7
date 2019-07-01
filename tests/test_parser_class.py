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
    # sentance 3 : place
    search_2 = '4 rue renard, 94510 La Queue en Brie'
    extracted_information_2 = 'renard, 94510 La Queue en Brie'
    # sentance 4 : description
    bleach = "Zaraki Kenpachi"
    bleach_extracted_information = "Zaraki Kenpachi"
    # error requests
    random_search = 'cmFuZG9tIGRhdGEgZm9yIGZha2Ugc2VhcmNo'
    punctuation = '-_,;:!()'
    punctuation_removed_punctuation = '        '
    empty_search = ' '


class TestParser:
    """
    Test the methode who parsing the search
    """
    def setup(self: str):
        self.params = Params()
        self.parser = Parser(self)

    def test_extract_info_request(self: str):
        """
        Extract good information from search and return information
        """
        self.params = Params()
        self.parser = Parser(self)
        assert self.parser.extract_information_request(self.params.search) == \
               self.params.extracted_information

    def test_extract_infoormation_otherrequest(self):
        assert self.parser.extract_information_request(self.params.search_1) == \
               self.params.extracted_information_1

    def test_extract_information_forplace(self):
        assert self.parser.extract_information_request(self.params.search_2) == \
               self.params.extracted_information_2

    def test_extract_information_fordescription(self):
        assert self.parser.extract_information_request(self.params.bleach) == \
                self.params.bleach_extracted_information

    def test_extract_information_forrandomsearch(self):
        assert self.parser.extract_information_request(self.params.random_search) == \
               self.params.random_search

    def test_extract_information_forpunctuation(self):
        assert self.parser.extract_information_request(self.params.punctuation) == \
               self.params.punctuation

    def test_extract_information_foremptysearch(self):
        assert self.parser.extract_information_request(self.params.empty_search) == \
               self.params.empty_search

    def test_remove_punctuation(self: str):
        """
        remove punctuation from search and return whitespace*
        """
        self.params = Params()
        self.parser = Parser(self)
        extracted_information = self.params.extracted_information
        assert self.parser.remove_punctuation(extracted_information) == \
               self.params.removed_punctuation

    def test_remove_only_punctuation(self):
        assert self.parser.remove_punctuation(self.params.punctuation) == \
               self.params.punctuation_removed_punctuation


    def test_remove_word_please(self: str):
        """
        remove word in word please from search and return dict_request
        """
        self.params = Params()
        self.parser = Parser(self)
        assert self.parser.remove_word_please(self.params.removed_punctuation) == \
               self.params.dict_request

