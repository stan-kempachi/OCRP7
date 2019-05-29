#! /usr/bin/env python
# -*-coding:Latin-1 -*

import json
import urllib.request
from io import BytesIO

from grandpybot import app as script


def test_http_return(monkeypatch):
    results = [{
        "description": "OpenClassrooms est une \u00e9cole en ligne qui propose \u00e0 ses membres des cours certifiants et des parcours d\u00e9bouchant sur un m\u00e9tier d'avenir, r\u00e9alis\u00e9s en interne, "
                       "par des \u00e9coles, des universit\u00e9s, ou encore par des entreprises partenaires comme Microsoft ou IBM Jusqu'en 2018, "
                       "n'importe quel membre du site pouvait \u00eatre auteur, via un outil nomm\u00e9 \"Course Lab\" De nombreux cours sont issus de la communaut\u00e9, mais ne sont plus mis en avant",
        "emplacement":
            {
                "adresse": "OpenClassRooms, 7, Cit\u00e9 Paradis, Porte-St-Denis, 10e, Paris, \u00cele-de-France, France m\u00e9tropolitaine, 75010, France",
                "latitude": "48.8747786",
                "longitude": "2.3504885",
                "types": "company"
            },
        "sentance_description": "Je vais donc t'en parler : ",
        "sentance_place": "Tu peut retrouver ce lieu l\u00e0 : ",
        "type_search": "place description",
        "wiki_url": "https://fr.wikipedia.org/wiki/OpenClassrooms"
    }
]

    def mockreturn(request):
        script.request = request
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        script.type_search = 'place description'
        script.information = 'OpenClassrooms  '
        assert script.get_user_request() == results
        return BytesIO(json.dumps(results).encode())