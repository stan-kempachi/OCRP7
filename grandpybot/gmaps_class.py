#! /usr/bin/env python
"""
File containing function who call gmaps API
"""

from gmaps import Geocoding

from config import MAP_API_KEY


class Gmaps:
    """ Class defining the method of calling the Gmaps API.
    """
    def geo(self, search):
        """
        Get a dict_location from gmaps.
        :param search:
        :return: dict_location
        """
        self.search = search
        try:
            self.gmaps = Geocoding(api_key=MAP_API_KEY)
            self.geocode_result = self.gmaps.geocode(search, language='fr')[0]
            dict_location = {}
            for libelle, item in self.geocode_result.items():
                if libelle == 'formatted_address':
                    dict_location['adresse'] = item
                elif libelle == 'geometry':
                    dict_location['latitude'] = item['location']['lat']
                    dict_location['longitude'] = item['location']['lng']
            return dict_location
        except:
            return False
