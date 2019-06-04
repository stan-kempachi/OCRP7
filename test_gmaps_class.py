#! /usr/bin/env python

from grandpybot.gmaps_class import *

class Params:
    search_1 = "la tour Eiffel"
    response_1 = {'adresse': 'Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France',
                  'latitude': 48.85837009999999, 'longitude': 2.2944813}
    search_2 =  "le Sacré-Coeur"
    response_2 = {'adresse': '35 Rue du Chevalier de la Barre, 75018 Paris, France',
                  'latitude': 48.88670459999999, 'longitude': 2.3431043}
    search_3 = " " \
               "la cathédrale Notre Dame de Paris"
    response_3 = {'adresse': '6 Parvis Notre-Dame - Pl. Jean-Paul II, 75004 Paris, France',
                  'latitude': 48.85296820000001, 'longitude': 2.3499021}
    #wrong search:
    tintin_et_milou = "Tintin et Milou"
    bleach = "Zaraki Kenpachi"
    random_search = 'cmFuZG9tIGRhdGEgZm9yIGZha2Ugc2VhcmNo'
    punctuation = '-_,;:!()'
    empty_search = ' '
    return_false = False


class TestGmaps:
    """ Class defining the method of calling the Gmaps API"""
    def test_geo(self):
        """Get a dict_location from gmaps"""
        params = Params()
        gmaps = Gmaps()
        assert gmaps.geo(params.search_1) == params.response_1
        assert gmaps.geo(params.search_2) == params.response_2
        assert gmaps.geo(params.search_3) == params.response_3
        # bad search who return False
        assert gmaps.geo(params.tintin_et_milou) == params.return_false
        assert gmaps.geo(params.bleach) == params.return_false
        assert gmaps.geo(params.random_search) == params.return_false
        assert gmaps.geo(params.punctuation) == params.return_false
        assert gmaps.geo(params.empty_search) == params.return_false




