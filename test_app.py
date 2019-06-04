def test_http_return(monkeypatch):
    results = {
        "description": "OpenClassrooms est une \u00e9cole en ligne qui propose \u00e0 ses membres des cours certifiants et des parcours d\u00e9bouchant sur un m\u00e9tier d'avenir, r\u00e9alis\u00e9s en interne, par des \u00e9coles, des universit\u00e9s, ou encore par des entreprises partenaires comme Microsoft ou IBM",
        "emplacement": {
        "adresse": "7 Cit\u00e9 Paradis, 75010 Paris, France",
        "latitude": 48.8748465,
        "longitude": 2.3504873
        },
        "type_search": "place description",
        "wiki_url": "https://fr.wikipedia.org/wiki/OpenClassrooms"
}

    # def mockreturn(request):
    #     return results
    # monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    # assert script.get_user_request() == results
    #     # script.request = request
    #     # script.type_search = 'place description'
    #     # script.information = 'OpenClassrooms  '
    #     # return BytesIO(json.dumps(results).encode())

