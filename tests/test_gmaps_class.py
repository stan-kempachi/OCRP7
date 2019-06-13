#! /usr/bin/env python

"""
file testing gmaps_class.py
"""

from grandpybot.gmaps_class import Gmaps

class Params:
    """
    Class defining the params for Gmaps()
    """

    search_1 = "la tour Eiffel"
    response_1 = {'adresse': 'Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France',
                  'latitude': 48.85837009999999, 'longitude': 2.2944813}
    search_2 = "le Sacré-Coeur"
    response_2 = {'adresse': '35 Rue du Chevalier de la Barre, 75018 Paris, France',
                  'latitude': 48.88670459999999, 'longitude': 2.3431043}
    search_3 = "l'arc de triomphe"
    response_3 = {'adresse': 'Place Charles de Gaulle, 75008 Paris, France',
                  'latitude': 48.8737917, 'longitude': 2.2950275}

    #wrong search:
    tintin_et_milou = "Tintin et Milou"
    bleach = "Zaraki Kenpachi"
    random_search = 'cmFuZG9tIGRhdGEgZm9yIGZha2Ugc2VhcmNo'
    punctuation = '-_,;:!()'
    empty_search = ' '
    return_false = False


class TestGmaps:
    """
    Class defining the method of calling the Gmaps API
    """
    def test_geo(self):
        """
        Get a dict_location from gmaps
        """
        self.params = Params()
        self.gmaps = Gmaps()
        assert self.gmaps.geo(self.params.search_1) == self.params.response_1
        assert self.gmaps.geo(self.params.search_2) == self.params.response_2
        assert self.gmaps.geo(self.params.search_3) == self.params.response_3
        # bad search who return False
        assert self.gmaps.geo(self.params.tintin_et_milou) == self.params.return_false
        assert self.gmaps.geo(self.params.bleach) == self.params.return_false
        assert self.gmaps.geo(self.params.random_search) == self.params.return_false
        assert self.gmaps.geo(self.params.punctuation) == self.params.return_false
        assert self.gmaps.geo(self.params.empty_search) == self.params.return_false
