#! /usr/bin/env python
"""
File containing function main
"""
import random
from datetime import datetime

from flask import Flask, render_template, request, json

import config as conf
from grandpybot.parser_class import Parser
from grandpybot.utils import get_if_error
from grandpybot.vocabulary import SENTANCE_DESCRIPTION_GRANDPY, SENTANCE_PLACE_GRANDPY
from grandpybot.wiki_class import Wikipedia
from grandpybot.gmaps_class import Gmaps

app = Flask(__name__)

"""Config option """
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


@app.context_processor
def inject_now():
    """return datetime"""
    return dict(now=datetime.now())


@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home():
    """define homepage"""
    return render_template('pages/home.html', google_key=conf.MAP_API_KEY)


@app.errorhandler(404)
def page_not_found():
    """define error page"""
    return render_template('errors/404.html'), 404


@app.route('/get_user_request', methods=['GET'])
def get_user_request():
    """define get user request methode"""
    if request.method == "GET":
        request_user = request.args.get('question')
        parser = Parser(request_user)
        information_extracted = parser.extract_information_request(request_user)
        information_extracted = parser.remove_punctuation(information_extracted)
        information_extracted = parser.remove_word_please(information_extracted)
        type_search = information_extracted['type_search']
        information = information_extracted['information']
        wiki = Wikipedia()
        description = wiki.get_description_wiki(information)
        wiki_url = wiki.get_wiki_url(information)
        gmaps = Gmaps()
        emplacement = gmaps.geo(search=information)
        error = get_if_error(type_search)
        if type_search == 'error':
            dict_information = {'type_search': 'error'}
        else:
            dict_information = {'wiki_url': wiki_url, 'emplacement': emplacement, 'description': description,
                                'type_search': type_search}
        dict_information.update({'sentance_place': random.choice(SENTANCE_PLACE_GRANDPY),
                                 'sentance_description': random.choice(SENTANCE_DESCRIPTION_GRANDPY)})
        dict_information.update(error)
        return json.dumps(dict_information)
