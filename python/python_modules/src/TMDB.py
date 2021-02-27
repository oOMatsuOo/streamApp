import requests
from python_modules.classes.movie import Movie
from python_modules.classes.serie import Serie
from python_modules.classes.season import Season
from python_modules.classes.episode import Episode

API_KEY = "4e839db120a9d7d78ae2473ca11b6833"
LANGUAGE = "fr-FR"


# Make a search in TMDB


def search_movie(search):
    url = "https://api.themoviedb.org/3/search/movie"

    querystring = {
        'query':search,
        'api_key': API_KEY,
        'language': LANGUAGE,
        'page': "1",
        'include_adult': "false"
        }

    search_request = requests.request("GET", url, params=querystring)

    # Transform json response into python format
    search_request = search_request.json()

    return search_request


def search_serie(search):
    url = "https://api.themoviedb.org/3/search/tv"

    querystring = {
        'query':search,
        'api_key': API_KEY,
        'language': LANGUAGE,
        'page': "1",
        'include_adult': "false"
        }

    search_request = requests.request("GET", url, params=querystring)

    # Transform json response into python format
    search_request = search_request.json()

    return search_request


def search_movie_by_id(id):
    url = get_movie_url(id)

    querystring = {
        'api_key': API_KEY,
        'language': LANGUAGE
    }

    search_request = requests.request("GET", url, params=querystring)

    # Transform json response into python format
    search_request = search_request.json()

    return search_request


def search_serie_by_id(id):
    url = get_serie_url(id)

    querystring = {
        'api_key': API_KEY,
        'language': LANGUAGE
        }

    search_request = requests.request("GET", url, params=querystring)

    # Transform json response into python format
    search_request = search_request.json()

    return search_request


def search_season_by_seasonNumber(serie_id, season_number):
    url = get_seasons_url(serie_id, season_number)

    querystring = {
        'api_key': API_KEY,
        'language': LANGUAGE
        }

    search_request = requests.request("GET", url, params=querystring)

    # Transform json response into python format
    search_request = search_request.json()

    return search_request


def search_episode_by_episode_number(serie_id, season_number, episode_number):
    url = get_episode_url(serie_id, season_number, episode_number)

    querystring = {
        'api_key': API_KEY,
        'language': LANGUAGE
        }

    search_request = requests.request("GET", url, params=querystring)

    # Transform json response into python format
    search_request = search_request.json()

    return search_request


# Parse result form research


def parse_movie_id_from_search_request(search_results):
    return search_results['id']


def create_movie_from_id_search(search_results):
    search_id = search_results['id']
    search_genres = []
    for genres in search_results['genres']:
        search_genres.append(genres['name'])
    search_name = search_results['title']
    search_overview = search_results['overview']

    movie = Movie([search_id, search_genres, search_name, search_overview])

    return movie


def parse_serie_id_from_search_request(search_results):
    return search_results['id']


def create_serie_from_id_search(search_results):
    search_id = search_results['id']
    search_name = search_results['name']
    search_genre = []
    for genres in search_results['genres']:
        search_genre.append(genres['name'])
    search_number_of_episodes = search_results['number_of_episodes']
    search_number_of_seasons = search_results['number_of_seasons']
    search_overview = search_results['overview']

    serie = Serie([search_id, search_name, search_genre, search_number_of_episodes, search_number_of_seasons, search_overview])

    return serie


def create_season_from_season_number_search(search_results):
    search_name = search_results['name']
    search_overview = search_results['overview']
    search_season_number = search_results['season_number']
    search_number_of_episodes = 0
    for episodes in search_results['episodes']:
        search_number_of_episodes += 1

    season = Season([search_name, search_overview, search_season_number, search_number_of_episodes])

    return season


def create_episodes_from_episode_number_search(search_results):
    search_name = search_results['name']
    search_overview = search_results['overview']
    search_episode_number = search_results['episode_number']

    episode = Episode([search_name, search_episode_number, search_overview])

    return episode


# Get All URL


def get_movie_url(movie_id):
    return "https://api.themoviedb.org/3/movie/%d" % movie_id


def get_serie_url(serie_id):
    return "https://api.themoviedb.org/3/tv/%d" % serie_id


def get_seasons_url(serie_id, season_number):
    return "%s%s%s" % (get_serie_url(serie_id), "/season/", season_number)


def get_episode_url(serie_id, season_number, episode_number):
    return "%s%s%s" % (get_seasons_url(serie_id, season_number), "/episode/", episode_number)
