#! /usr/bin/env python
"""File containing function utilised by the app"""

from grandpybot.gmaps_class import Gmaps
from grandpybot.wiki_class import Wikipedia


def get_type_search(information):
    """
    return type of search : place, description or twice
    :param information:
    :return: type of search
    """
    emplacement = Gmaps.geo(information)
    description = Wikipedia.get_description_wiki(information)

    if not emplacement and description:
        return 'description'
    elif emplacement and not description:
        return 'place'
    elif emplacement and description:
        return 'place description'
    else:
        return 'error'


def get_if_error(type_search):
    """
    Check (and return if it is) error for a search
    :param type_search:
    :return: dict_error
    """
    dict_error = {'error_place': False, 'error_description': False}
    if type_search == 'place':
        dict_error['error_description'] = True
    elif type_search == 'description':
        dict_error['error_place'] = True
    elif type_search == 'error':
        dict_error['error_place'] = True
        dict_error['error_description'] = True
    return dict_error
