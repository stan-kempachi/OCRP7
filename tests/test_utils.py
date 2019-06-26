#! /usr/bin/env python
"""
file testing utils.py
"""
import grandpybot.utils as utils


def test_get_type_search():
    """ return type of search : place, description or twice """
    assert utils.get_type_search('Openclassrooms ') == 'place description'

def test_get_type_searchfordescription():
    assert utils.get_type_search('Obélix') == 'description'

def test_get_type_searchforplace():
    assert utils.get_type_search('4 rue renard, 945100 La Queue en Brie') == 'place'

def test_get_if_error():
    """ Check (and return if it is) error for a search """
    assert utils.get_if_error('place description') == \
           {'error_place': False, 'error_description': False}

def test_get_if_errordescription():
    assert utils.get_if_error('description') == {'error_place': True, 'error_description': False}

def test_get_if_errorplace():
    assert utils.get_if_error('place') == {'error_place': False, 'error_description': True}

def test_get_if_errordescriptionplace():
    assert utils.get_if_error('error') == {'error_place': True, 'error_description': True}
