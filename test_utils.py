from grandpybot.utils import *

def test_get_type_search():
    """
    return type of search : place, description or twice
    :param information:
    :return: type of search
    """
    assert get_type_search('Openclassrooms') == 'place description'
    assert get_type_search('Obélix') == 'description'
    assert get_type_search('4 rue renard, 945100 La Queue en Brie') == 'place'
    assert get_type_search(' ') == 'error'



def test_get_if_error():
    """
    Check (and return if it is) error for a search
    :param type_search:
    :return: dict_error
    """
    assert get_if_error('place description') == {'error_place': False, 'error_description': False}
    assert get_if_error('description') == {'error_place': True, 'error_description': False}
    assert get_if_error('place') == {'error_place': False, 'error_description': True}
    assert get_if_error('error') == {'error_place': True, 'error_description': True}