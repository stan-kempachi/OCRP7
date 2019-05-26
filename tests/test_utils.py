from grandpybot.utils import *


def get_wiki_url(search):
    """
    Get a description from wikipedia.
    :param search:
    :return: wiki_url
    """
    try:
        wikipedia.set_lang("fr")
        wiki_page = wikipedia.page(search)
        wiki_url = wiki_page.url
        return wiki_url
    except:
        return False

def test_get_wiki_url():
    assert get_wiki_url('Openclassrooms') == 'https://fr.wikipedia.org/wiki/OpenClassrooms'



def get_type_search(information):
    """
    return type of search : place, description or twice
    :param information:
    :return: type of search
"""
    emplacement = geo(information)
    description = get_description_wiki(information)

    if not emplacement and description:
        return 'description'
    elif emplacement and not description:
        return 'place'
    elif emplacement and description:
        return 'place description'
    else:
        return 'error'


def test_get_type_search():
    assert get_type_search('Openclassrooms') == 'place description'



def extract_information_request(sentance):
    """
    Extract good information from search
    :param sentance:
    :return: dict_request
    """
    sentance = sentance.replace('?', '')
    sentance = sentance.replace('.', '')
    dict_request = {}
    list_words = sentance.split(' ')
    list_words_for_search = list_words
    for word in list_words:
        if "d'" in word:
            list_words_for_search = list_words[list_words.index(word):]
            break
        if word in WORD_ABOUT_EMPLACEMENT and WORD_ABOUT_WHAT:
            list_words_for_search = list_words[list_words.index(word) + 1:]
            break
        else: list_words_for_search = list_words
    information = " ".join(list_words_for_search)
    information = information.replace("d'", '')
    for word in WORD_PLEASE:
        information = information.replace(word, '')
    dict_request['information'] = information
    dict_request['type_search'] = get_type_search(information)
    return dict_request



def test_extract_information_request():
    sentance = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ? "
    assert extract_information_request(sentance) == {'information': 'OpenClassrooms  ', 'type_search': 'place description'}


