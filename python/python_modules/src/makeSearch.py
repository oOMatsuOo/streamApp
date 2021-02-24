from python_modules.classes.serie import Serie
from python_modules.classes.season import Season
from python_modules.classes.episode import Episode
from python_modules.classes.movie import Movie
from python_modules.classes.file import File
from python_modules.TMDB import *
from python_modules.DBConnect import *


def get_movie_search(search_string):
    search_response = search_movie(search_string)

    return search_response


def get_movie(movie_searched):
    movie_id = parse_movie_id_from_search_request(movie_searched)
    movie = search_movie_by_id(movie_id)
    movie = create_movie_from_id_search(movie)
    movie = Movie(movie)

    return movie


def get_serie_search(search_string):
    search_response = search_serie(search_string)

    return search_response


def get_all_serie(serie_searched):
    serie = get_serie(serie_searched)
    get_seasons(serie)
    get_episodes(serie)

    return serie


def get_serie(serie_searched):
    serie_id = parse_serie_id_from_search_request(serie_searched)
    serie = search_serie_by_id(serie_id)
    serie = create_serie_from_id_search(serie)
    serie = Serie(serie)
    
    return serie


def get_seasons(serie):
    for season in range(1,serie.number_of_seasons + 1):
        searched_season = search_season_by_seasonNumber(serie.id, season)
        created_season = create_season_from_season_number_search(searched_season)
        created_season.set_serie_id(serie.id)
        serie.add_season(created_season)


def get_episodes(serie):
    for season in serie.season:
        for episodes in range(1,season.number_of_episodes):
            searched_episodes = search_episode_by_episode_number(serie.id, season.season_number, episodes)
            created_episode = create_episodes_from_episode_number_search(searched_episodes)
            created_episode.set_serie_id(serie.id)
            created_episode.set_season_id(season.number_of_episodes)
            season.add_episode(created_episode)
