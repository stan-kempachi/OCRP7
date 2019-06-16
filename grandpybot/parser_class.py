#! /usr/bin/env python

import json
import string

from grandpybot.utils import *
from grandpybot.vocabulary import *


class Parser ():
    """
    Class defining the method of parser before appel aux APIs
    """
    def __init__(self, sentance : str):
        """constructor"""
        self.sentance = sentance



    def extract_information_request(self, sentance : str):
        """
        Extract good information from search
        :param sentance:
        :return: dict_request
        """
        with open('grandpybot/stop_words.json', 'r') as json_data:
            STOP_WORDS = json.load(json_data)
        list_words = sentance.split(' ')
        list_words_for_search = list_words
        for word in list_words:
            if "d'" in word:
                list_words_for_search = list_words[list_words.index(word):]
                break
            if word in WORD_ABOUT_EMPLACEMENT and WORD_ABOUT_WHAT:
                list_words_for_search = list_words[list_words.index(word) + 1:]
                break
            if word in STOP_WORDS:
                list_words_for_search = list_words[list_words.remove(word):]
            else:
                list_words_for_search = list_words
        information = " ".join(list_words_for_search)
        information = information.replace("d'", '')
        return information

    def remove_punctuation(self, information: str):
        translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))  # punctuation to space
        information = information.translate(translator)
        return information

    def remove_word_please(self, information : str ):
        information = information.split(' ')
        dict_request = {}
        for elt in information:
            if elt in WORD_PLEASE:
                information.remove(elt)
        information_to_search = " ".join(information)
        dict_request['information'] = information_to_search
        dict_request['type_search'] = get_type_search(information_to_search)
        return dict_request
