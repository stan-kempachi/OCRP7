#! /usr/bin/env python
"""
file testing utils.py
"""
import grandpybot.utils as utils


def test_get_type_search():
    """ return type of search : place, description or twice """
    assert utils.get_type_search('Openclassrooms ') == 'place description'
    assert utils.get_type_search('Obélix') == 'description'
    assert utils.get_type_search('4 rue renard, 945100 La Queue en Brie') == 'place'
    assert utils.get_type_search(' ') == 'error'
    assert utils.get_type_search('-_,;:!()') == 'error'


def test_get_if_error():
    """ Check (and return if it is) error for a search """
    assert utils.get_if_error('place description') == \
           {'error_place': False, 'error_description': False}
    assert utils.get_if_error('description') == {'error_place': True, 'error_description': False}
    assert utils.get_if_error('place') == {'error_place': False, 'error_description': True}
    assert utils.get_if_error('error') == {'error_place': True, 'error_description': True}
