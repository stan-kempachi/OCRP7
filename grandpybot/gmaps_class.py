#! /usr/bin/env python

from gmaps import Geocoding

from config import *


class Gmaps:
    """ Classe definissant  la méthode de l'appel a l'API Gmaps.
    """
    def __init__(self, gmaps):
        """constructor"""
        self.gmaps = gmaps(api_key=MAP_API_KEY)


    def geo(search):
        """
        Get a dict_location from gmaps.
        :param search:
        :return: dict_location
        """
        try:
            gmaps = Geocoding(api_key=MAP_API_KEY)
            geocode_result = gmaps.geocode(search, language='fr')[0]
            dict_location = {}
            for libelle, item in geocode_result.items():
                if libelle == 'formatted_address':
                    dict_location['adresse'] = item
                elif libelle == 'geometry':
                    dict_location['latitude'] = item['location']['lat']
                    dict_location['longitude'] = item['location']['lng']
            return dict_location
        except:
            return False
