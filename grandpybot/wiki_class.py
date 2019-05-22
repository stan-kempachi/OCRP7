#! /usr/bin/env python

import wikipedia

class Wikipedia:
    """
    Class defining the call to the Wikipedia API characterized by:
     - wikipedia page content
     - link of the wikipedia page
    """
    def __init__(self):
        """constructor"""
        wikipedia.set_lang("fr")

    def get_description_wiki(search):
        """
        Get a description from wikipedia.
        :param search:
        :return:description
        """
        try:
            srch = wikipedia.search(search, "html.parser")
            data = wikipedia.page(srch, "html.parser").content
            data = data.split('.')
            description = ''
            for sentance in data[:3]:
                description = description + sentance
            return description
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