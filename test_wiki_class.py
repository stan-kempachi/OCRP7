#! /usr/bin/env python
from grandpybot.wiki_class import *

class Params:
    description = "OpenClassrooms est une école en ligne qui propose à ses membres des cours certifiants et des parcours débouchant sur un métier d'avenir, réalisés en interne, par des écoles, des universités, ou encore par des entreprises partenaires comme Microsoft ou IBM"
    search = 'Openclassrooms', \
             'La tour Eiffel' , \
             'La pyramide du Louvre'
    len_result_for_search = 255
    search_2 = '4 rue renard, 945100 La Queue en Brie'
    punctuation = '-_,;:!()'
    no_return = False
    empty_search = ' '
    search_url = 'https://fr.wikipedia.org/wiki/OpenClassrooms'
    search_url_2 ='https://fr.wikipedia.org/wiki/Tour_Eiffel'
    search_url_3 ='https://fr.wikipedia.org/wiki/Pyramide_du_Louvre'

class TestWikipedia:

    def test_get_description_wiki(self):
        """
        Get a description from wikipedia.
        """
        params = Params()
        wiki = Wikipedia()
        # check if return the description
        assert wiki.get_description_wiki(params.search[0]) == params.description
        # check how many characters of the description
        assert len(params.description) == params.len_result_for_search
        # check if return False for bad searches
        assert wiki.get_description_wiki(params.search_2) == params.no_return
        assert wiki.get_description_wiki(params.punctuation) == params.no_return
        assert wiki.get_description_wiki(params.empty_search) == params.no_return

    def test_get_wiki_url(self):
        """
        Get a url from wikipedia.
        """
        params = Params()
        wiki = Wikipedia()
        # check if return the url for search
        assert wiki.get_wiki_url(params.search[0]) == params.search_url
        assert wiki.get_wiki_url(params.search[1]) == params.search_url_2
        assert wiki.get_wiki_url(params.search[2]) == params.search_url_3
        # check if return the False for bad search
        assert wiki.get_description_wiki(params.search_2) == params.no_return
        assert wiki.get_description_wiki(params.punctuation) == params.no_return
        assert wiki.get_description_wiki(params.empty_search) == params.no_return

