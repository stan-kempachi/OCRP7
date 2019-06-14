#! /usr/bin/env python
"""
File containing function main
"""
import random
from datetime import datetime

from flask import Flask, render_template, request, json

import config as conf
from grandpybot.gmaps_class import Gmaps
from grandpybot.parser_class import Parser
from grandpybot.utils import get_if_error
from grandpybot.vocabulary import SENTANCE_PLACE_GRANDPY, SENTANCE_DESCRIPTION_GRANDPY
from grandpybot.wiki_class import Wikipedia

APP = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
APP.config.from_object('config')
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


@APP.context_processor
def inject_now():
    """return datetime"""
    return dict(now=datetime.now())

@APP.route('/index', methods=['GET', 'POST'])
@APP.route('/', methods=['GET', 'POST'])
def home():
    """define homepage"""
    return render_template('pages/home.html', google_key=conf.MAP_API_KEY)

@APP.errorhandler(404)
def page_not_found():
    """define error page"""
    return render_template('errors/404.html'), 404

@APP.route('/get_user_request', methods=['GET'])
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
            dict_information = \
                {'wiki_url': wiki_url, 'emplacement': emplacement,
                 'description': description, 'type_search': type_search}
        dict_information.update({'sentance_place': random.choice(SENTANCE_PLACE_GRANDPY),
                                 'sentance_description': random.choice\
                                     (SENTANCE_DESCRIPTION_GRANDPY)})
        dict_information.update(error)

        return json.dumps(dict_information)
