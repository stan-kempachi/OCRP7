#! /usr/bin/env python

import json

from grandpybot.utils import *
from grandpybot.vocabulary import *


class Parser ():
    """
    Class defining the method of parser before appel aux APIs
    """
    def __init__(self, sentance : str):
        self.sentance = sentance.replace('?', '')
        self.sentance = sentance.replace('.', '')

    def extract_information_request(self, sentance : str):
        """
        Extract good information from search
        :param sentance:
        :return: dict_request
        """
        with open('grandpybot/stop_words.json') as json_data:
            STOP_WORDS = json.load(json_data)
        dict_request = {}
        list_words = sentance.split(' ')
        list_words_for_search = list_words
        for word in list_words:
            if "d'" in word:
                list_words_for_search = list_words[list_words.index(word):]
                break
            if word in STOP_WORDS:
                list_words_for_search = list_words[list_words.remove(word):]
                break
            if word in WORD_ABOUT_EMPLACEMENT and WORD_ABOUT_WHAT:
                list_words_for_search = list_words[list_words.index(word) + 1:]
                break
            else:
                list_words_for_search = list_words
        information = " ".join(list_words_for_search)
        information = information.replace("d'", '')
        for word in WORD_PLEASE:
            information = information.replace(word, '')
        dict_request['information'] = information
        dict_request['type_search'] = get_type_search(information)
        return dict_request
