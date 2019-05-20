#! /usr/bin/env python
"""File containing function utilised by the app"""
from gmaps import Geocoding

from config import *
from grandpybot.vocabulary import *
from grandpybot.wiki_classe import Wikipedia


def geo(search):
    """
    Get a dict_location from gmaps.
    :param search:
    :return: dict_location
    """
    gmaps = Geocoding(api_key=MAP_API_KEY)
    try:
        geocode_result = gmaps.geocode(search, language='fr')[0]
        dict_location = {}
        for libelle, item in geocode_result.items():
            if libelle == 'formatted_address':
                dict_location['adresse'] = item
            elif libelle == 'geometry':
                dict_location['latitude'] = item['location']['lat']
                dict_location['longitude'] = item['location']['lng']
            elif libelle == 'types':
                dict_location['types'] = '/'.join(item)
        print(dict_location)
        return dict_location
    except:
        return False


def extract_information_request(sentance):
    """
    Extract good information from search
    :param sentance:
    :return: dict_request
    """
    sentance = sentance.replace('?', '')
    sentance = sentance.replace('.', '')
    dict_request = {}
    list_words = sentance.split(' ')
    list_words_for_search = list_words
    for word in list_words:
        if "d'" in word:
            list_words_for_search = list_words[list_words.index(word):]
            break
        if word in WORD_ABOUT_EMPLACEMENT and WORD_ABOUT_WHAT:
            list_words_for_search = list_words[list_words.index(word) + 1:]
            break
        else: list_words_for_search = list_words
    information = " ".join(list_words_for_search)
    information = information.replace("d'", '')
    for word in WORD_PLEASE:
        information = information.replace(word, '')
    dict_request['information'] = information
    dict_request['type_search'] = get_type_search(information)
    return dict_request


def get_type_search(information):
    """
    return type of search : place, description or twice
    :param information:
    :return: type of search
    """
    emplacement = geo(information)
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
