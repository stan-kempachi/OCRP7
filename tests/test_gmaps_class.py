#! /usr/bin/env python

"""
file testing gmaps_class.py
"""

from grandpybot.gmaps_class import Gmaps
import urllib.request


class Params:
    """
    Class defining the params for Gmaps()
    """
    search_1 = "la tour Eiffel"
    response_1 = {'adresse': 'Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France',
                  'latitude': 48.85837009999999, 'longitude': 2.2944813}    # wrong search:
    tintin_et_milou = "Tintin et Milou"
    random_search = 'cmFuZG9tIGRhdGEgZm9yIGZha2Ugc2VhcmNo'
    punctuation = '-_,;:!()'
    empty_search = ' '
    return_false = False


class TestGmaps:
    """
    Class defining the method of calling the Gmaps API
    """
    def setup(self):
        self.params = Params()
        self.gmaps_object = Gmaps()

    def test_geo(self, monkeypatch):
        """
        Get a dict_location from gmaps
        """
        def mockreturn():
            """return mock result"""

            return self.params
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

        assert self.gmaps_object.geo(self.params.search_1) == self.params.response_1

    def test_geo_wrong_search(self):
        # bad search who return False
        assert self.gmaps_object.geo(self.params.tintin_et_milou) == self.params.return_false

    def test_geo_random_search(self):
        assert self.gmaps_object.geo(self.params.random_search) == self.params.return_false

    def test_geo_punctuation_search(self):
        assert self.gmaps_object.geo(self.params.punctuation) == self.params.return_false

    def test_geo_empty_search(self):
        assert self.gmaps_object.geo(self.params.empty_search) == self.params.return_false


