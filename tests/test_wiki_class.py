#! /usr/bin/env python
"""
file testing wiki_class.py
"""
from grandpybot.wiki_class import Wikipedia
import urllib.request



class Params:
    """
    Class defining the params for Wikipedia()
    """
    description = \
        "OpenClassrooms est une école en ligne qui propose à ses membres des cours " \
        "certifiants et des parcours débouchant sur un métier d'avenir, réalisés " \
        "en interne, par des écoles, des universités, ou encore par des entreprises" \
        " partenaires comme Microsoft ou IBM"
    search = 'Openclassrooms'
    len_result_for_search = 255
    search_2 = '4 rue renard, 945100 La Queue en Brie'
    no_return = False
    search_url = 'https://fr.wikipedia.org/wiki/OpenClassrooms'



class TestWikipedia:
    """
    Test the methode who get description and url from wikipedia
    """
    def setup(self):
        self.params = Params()
        self.wiki_object = Wikipedia()

    def test_get_description_wiki(self, monkeypatch):
        """
        Get a description from wikipedia.
        """
        def mockreturn():
            """
            return mock result
            """
            return self.params
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        # check if return the description
        assert self.wiki_object.get_description_wiki(self.params.search) == self.params.description

    def test_how_many_characters_are_returned(self):
        assert len(self.params.description) == self.params.len_result_for_search

    def test_if_return_false_for_wrong_search(self):
        assert self.wiki_object.get_description_wiki(self.params.search_2) == self.params.no_return

    def test_get_wiki_url(self, monkeypatch):
        """
        Get a url from wikipedia.
        """
        def mockreturn():
            """
            return mock result
            """
            return self.params
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        # check if return the url for search
        assert self.wiki_object.get_wiki_url(self.params.search) == self.params.search_url

    def test_if_return_false_for_bad_search(self):
        # check if return the False for bad search
        assert self.wiki_object.get_description_wiki(self.params.search_2) == self.params.no_return

