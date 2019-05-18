#! /usr/bin/env python
"""File containing function utilised by the app"""
import gmaps
import wikipedia
from geopy.geocoders import Nominatim

from config import *
from grandpybot.vocabulary import *


def geo(search):
    """
    Get a description from wikipedia.
    :param search:
    :return: dict_location
    """
    gmaps.configure(api_key=MAP_API_KEY)
    try:
        geolocator = Nominatim(user_agent="app.py")
        location = geolocator.geocode(search)
        location_raw = location.raw
        dict_location = {}
        for key, item in location_raw.items():
            if key == 'display_name':
                dict_location['adresse'] = item
            elif key == 'lat':
                dict_location['latitude'] = item
            elif key == 'lon':
                dict_location['longitude'] = item
            elif key == 'type':
                dict_location['types'] = item
        return dict_location
    except:
        return False


def get_wiki_url(search):
    """
    Get a description from wikipedia.
    :param search:
    :return: wiki_url
    """
    try:
        wikipedia.set_lang("fr")
        wiki_page = wikipedia.page(search)
        wiki_url = wiki_page.url
        return wiki_url
    except:
        return False


def get_description_wiki(search):
    """
    Get a description from wikipedia.
    :param search:
    :return:description
    """
    try:
        wikipedia.set_lang("fr")
        srch = wikipedia.search(search, "html.parser")
        data = wikipedia.page(srch, "html.parser").content
        data = data.split('.')
        description = ''
        for sentance in data[:3]:
            description = description + sentance
        return description
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
    description = get_description_wiki(information)

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
