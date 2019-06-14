#! /usr/bin/env python

from gmaps import Geocoding

from config import MAP_API_KEY


class Gmaps:
    """ Class defining the method of calling the Gmaps API.
    """
    def __init__(self):
        """constructor"""

    def geo(self, search):
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
