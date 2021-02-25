import os

from python_modules.classes.DBEntity import dbConnect, MovieFileEntity, MovieVideoEntity, SerieFileEntity, SeasonFileEntity, EpisodeFileEntity, EpisodeVideoEntity
from python_modules.classes.video import Video
from python_modules.classes.file import File
from python_modules.src.hashcode import get_dir_hashcode, get_file_hashcode



def update_all():
    db_connection = dbConnect()

    update_serie(db_connection)
    update_movies(db_connection)

    db_connection.close_connection()


def update_serie(db_connection):

    serie_entity            = SerieFileEntity(db_connection.connection)


    path = 'media/Series'
    all_series = list_series(path)

    for serie in all_series:
        full_path = find_dir(serie, path)
        serie_hashcode = get_dir_hashcode(full_path)

        serie_file = File(serie, serie_hashcode)

        if not serie_entity.serie_file_exists_by_hashcode(serie_file) :
            serie_entity.insert_serie_file(serie_file)

            db_connection.commit_db()

        update_season(db_connection, full_path)

    return 


def update_season(db_connection, serie_path):

    season_entity = SeasonFileEntity(db_connection.connection)

    all_seasons = list_season(serie_path)

    for season in all_seasons:
        full_path = find_dir(season, serie_path)
        season_hashcode = get_dir_hashcode(full_path)

        season_file = File(season, season_hashcode)
        
        if not season_entity.season_file_exists_by_hashcode(season_file):
            season_entity.insert_season_file(season_file)
        
            db_connection.commit_db()


        update_episode(db_connection, full_path)


def update_episode(db_connection, season_path):

    episode_file_entity     = EpisodeFileEntity(db_connection.connection)
    episode_video_entity    = EpisodeVideoEntity(db_connection.connection)

    all_episodes = list_episode(season_path)

    for episode in all_episodes:
        full_path = find_file(episode, season_path)
        episode_hashcode = get_file_hashcode(full_path)
        episode_file = File(episode, episode_hashcode)
        
        if not episode_file_entity.episode_file_exists_by_hashcode(episode_file) :
            episode_name = get_file_name(episode)
            episode_duration = get_duration(full_path)
            episode_video = Video(episode_name, episode_duration)

            episode_video_id = episode_video_entity.insert_episode_video(episode_video)

            episode_file.set_link(episode_video_id)

            episode_file_entity.insert_episode_file(episode_file)

            db_connection.commit_db()


def update_movies(db_connection):

    movie_file_entity       = MovieFileEntity(db_connection.connection)
    movie_video_entity      = MovieVideoEntity(db_connection.connection)

    path = 'media/Film'
    all_movies = list_movies(path)

    for movie in all_movies:
        full_path = find_file(movie, path)
        movie_hashcode = get_file_hashcode(full_path)
        movie_file = File(movie, movie_hashcode)

        if not movie_file_entity.movie_file_exists_by_hashcode(movie_file) :
            movie_name = get_file_name(movie)
            movie_duration = get_duration(full_path)
            movie_video = Video(movie_name, movie_duration)

            movie_video_id = movie_video_entity.insert_movie_video(movie_video)

            movie_file.set_link(movie_video_id)

            movie_file_entity.insert_movie_file(movie_file)

            db_connection.commit_db()


    return 


def list_series(path):
    all_series = []
    for serie in os.listdir(path):
        all_series.append(serie)
    
    return all_series


def list_season(path):
    all_season = []
    for season in os.listdir(path):
        all_season.append(season)
    
    return all_season


def list_episode(path):
    all_episode = []
    for (repertoire, sous_repertoires, fichiers) in os.walk(path):
        for files in fichiers:
            all_episode.append(files)

    return all_episode


def find_dir(dirname, search_path):
    for root, dir, files in os.walk(search_path):
        if dirname in dir:
            return os.path.join(root, dirname)
    
    return None


def find_file(file_name, search_path):
    for root, dir, files in os.walk(search_path):
        if file_name in files:
            return os.path.join(root, file_name)
    
    return None


def list_movies(path):
    all_movies = []
    for (repertoire, sous_repertoires, fichiers) in os.walk(path):
        for files in fichiers:
            all_movies.append(files)

    return all_movies


def get_file_name(file):
    return os.path.splitext(file)[0]


def get_duration(file):
    video = TinyTag.get(path)
    duration = time.strftime('%H:%M:%S', time.gmtime(video.duration))
    return duration

