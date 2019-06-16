#! /usr/bin/env python

from grandpybot.parser_class import *

class Params:
    # sentance 1
    search = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms stp ?"
    extracted_information = 'OpenClassrooms stp ?'
    removed_punctuation = 'OpenClassrooms stp  '
    dict_request = {'information': 'OpenClassrooms  ', 'type_search': 'place description'}
    # sentance 2
    search_1 = "La tour Eiffel please ?"
    extracted_information_1  = 'La tour Eiffel please ?'
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
    random_search_dict  = {'information': 'cmFuZG9tIGRhdGEgZm9yIGZha2Ugc2VhcmNo', 'type_search': 'error'}
    punctuation = '-_,;:!()'
    punctuation_removed_punctuation = '        '
    punctuation_dict_request = {'information': '        ', 'type_search': 'error'}
    empty_search = ' '
    empty_dict_request = {'information': ' ', 'type_search': 'error'}

class TestParser:
    def test_extract_information_request(search):
        """Extract good information from search and return information"""
        params = Params()
        parser = Parser(params.search)
        assert parser.extract_information_request(params.search) == params.extracted_information
        assert parser.extract_information_request(params.search_1) == params.extracted_information_1
        assert parser.extract_information_request(params.search_2) == params.extracted_information_2
        assert parser.extract_information_request(params.bleach) == params.bleach_extracted_information
        assert parser.extract_information_request(params.random_search) == params.random_search
        assert parser.extract_information_request(params.punctuation) == params.punctuation
        assert parser.extract_information_request(params.empty_search) == params.empty_search


    def test_remove_punctuation(extracted_information):
        params = Params()
        parser = Parser(params.extracted_information)
        assert parser.remove_punctuation(params.extracted_information) == params.removed_punctuation
        assert parser.remove_punctuation(params.extracted_information_1) == params.removed_punctuation_1
        assert parser.remove_punctuation(params.extracted_information_2) == params.removed_punctuation_2
        assert parser.remove_punctuation(params.bleach_extracted_information) == params.bleach_removed_punctuation
        assert parser.remove_punctuation(params.random_search) == params.random_search
        assert parser.remove_punctuation(params.punctuation) == params.punctuation_removed_punctuation
        assert parser.remove_punctuation(params.empty_search) == params.empty_search


    def test_remove_word_please(removed_punctuation):
        params = Params()
        parser = Parser(params.removed_punctuation)
        assert parser.remove_word_please(params.removed_punctuation) == params.dict_request
        assert parser.remove_word_please(params.removed_punctuation_1) == params.dict_request_1
        assert parser.remove_word_please(params.removed_punctuation_2) == params.dict_request_2
        assert parser.remove_word_please(params.bleach_removed_punctuation) == params.bleach_dict_request
        assert parser.remove_word_please(params.random_search) == params.random_search_dict
        assert parser.remove_word_please(params.empty_search) == params.empty_dict_request
