#! /usr/bin/env python
"""
file testing wiki_class.py
"""
from grandpybot.wiki_class import Wikipedia


class Params:
    """
    Class defining the params for Wikipedia()
    """
    description = \
        "OpenClassrooms est un site web de formation en ligne qui propose à ses membres des cours certifiants et des " \
        "parcours débouchant sur des métiers en croissance."
    search = 'Openclassrooms', \
             'La tour Eiffel', \
             'La pyramide du Louvre'
    len_result_for_search = len(description)
    search_2 = '4 rue renard, 945100 La Queue en Brie'
    punctuation = '-_,;:!()'
    no_return = False
    empty_search = ' '
    search_url = 'https://fr.wikipedia.org/wiki/OpenClassrooms'
    search_url_2 = 'https://fr.wikipedia.org/wiki/Tour_Eiffel'
    search_url_3 = 'https://fr.wikipedia.org/wiki/Pyramide_du_Louvre'


class TestWikipedia:
    """
    Test the methode who get description and url from wikipedia
    """

    def test_get_description_wiki(self):
        """
        Get a description from wikipedia.
        """
        self.params = Params()
        self.wiki = Wikipedia()
        # check if return the description
        assert self.wiki.get_description_wiki(self.params.search[0]) == self.params.description
        # check how many characters of the description
        assert len(self.params.description) == self.params.len_result_for_search
        # check if return False for bad searches
        assert self.wiki.get_description_wiki(self.params.search_2) == self.params.no_return
        assert self.wiki.get_description_wiki(self.params.punctuation) == self.params.no_return
        assert self.wiki.get_description_wiki(self.params.empty_search) == self.params.no_return

    def test_get_wiki_url(self):
        """
        Get a url from wikipedia.
        """
        self.params = Params()
        self.wiki = Wikipedia()
        # check if return the url for search
        assert self.wiki.get_wiki_url(self.params.search[0]) == self.params.search_url
        assert self.wiki.get_wiki_url(self.params.search[1]) == self.params.search_url_2
        assert self.wiki.get_wiki_url(self.params.search[2]) == self.params.search_url_3
        # check if return the False for bad search
        assert self.wiki.get_description_wiki(self.params.search_2) == self.params.no_return
        assert self.wiki.get_description_wiki(self.params.punctuation) == self.params.no_return
        assert self.wiki.get_description_wiki(self.params.empty_search) == self.params.no_return
