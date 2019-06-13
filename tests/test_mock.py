import urllib
import urllib.request

from grandpybot.gmaps_class import Gmaps
from grandpybot.utils import get_type_search
from grandpybot.wiki_class import Wikipedia
from grandpybot.app import get_user_request


class Params:
        results = {
            "description": "OpenClassrooms est une école en ligne qui propose à ses membres "
            "des cours certifiants et des parcours débouchant sur un métier d'avenir, "
                      "réalisés en interne, par des écoles, des universités, ou encore par "
            "des entreprises partenaires comme Microsoft ou IBM",
            "emplacement": {
                "adresse": "7 Cit\u00e9 Paradis, 75010 Paris, France",
                "latitude": 48.8748465,
                "longitude": 2.3504873
            },
            "type_search": "place description",
            "wiki_url": "https://fr.wikipedia.org/wiki/OpenClassrooms"
        }


class TestGetRequest:
    """initializes test class for the Media Wiki API with its attributes and methods"""

    def test_search(self, monkeypatch):
        """tests media wiki search and asserts results"""
        self.search = "Openclassrooms"
        self.gmaps_object = Gmaps()
        self.wiki_object = Wikipedia()
        self.type_search = get_type_search(self.search)

        def mockreturn():
            """returns mock results"""
            return Params.results
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

        assert self.gmaps_object.geo(self.search) == Params.results['emplacement']
        assert self.wiki_object.get_description_wiki(self.search) == Params.results['description']
        assert self.wiki_object.get_wiki_url(self.search) == Params.results['wiki_url']
        assert self.type_search == Params.results['type_search']
        assert mockreturn() == Params.results

