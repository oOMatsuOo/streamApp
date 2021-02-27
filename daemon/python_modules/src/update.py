import os
from tinytag import TinyTag
from videoprops import get_video_properties
import time
import mariadb

from python_modules.classes.DBEntity import dbConnect, MovieFileEntity, MovieVideoEntity, SerieFileEntity, SeasonFileEntity, EpisodeFileEntity, EpisodeVideoEntity
from python_modules.classes.video import Video
from python_modules.classes.file import File
from python_modules.src.hashcode import get_dir_hashcode, get_file_hashcode



def update_all(path):
    db_connection = dbConnect()

    serie_path = os.path.join(path, 'Series')
    movie_path = os.path.join(path, 'Film')

    update_serie(db_connection, serie_path)
    update_movies(db_connection, movie_path)

    db_connection.close_connection()


def update_serie(db_connection, path):

    serie_entity = SerieFileEntity(db_connection.connection)

    all_series = list_series(path)

    for serie in all_series:
        full_path = find_dir(serie, path)
        serie_hashcode = get_dir_hashcode(full_path)

        serie_file = File(serie, serie_hashcode, 'null')

        if not serie_entity.serie_file_exists_by_hashcode(serie_file) :
            print("Add Serie : " + str(serie))
            try:
                serie_entity.insert_serie_file(serie_file)
            except mariadb.IntegrityError as e:
                print(f"Error adding serie to MariaDB Plateform: {e}")
                print("Serie : " + str(serie_file))

            db_connection.commit_db()
        
        serie_id = serie_entity.get_serie_id(serie_file)

        update_season(db_connection, full_path, serie_id)

    return 


def update_season(db_connection, serie_path, serie_id):

    season_entity = SeasonFileEntity(db_connection.connection)

    all_seasons = list_season(serie_path)

    for season in all_seasons:
        full_path = find_dir(season, serie_path)
        season_hashcode = get_dir_hashcode(full_path)

        season_file = File(season, season_hashcode, 'null')
        season_file.set_link(serie_id)
        
        if not season_entity.season_file_exists_by_hashcode(season_file):
            print("Add season : " + str(season))
            try:
                season_entity.insert_season_file(season_file)
            except mariadb.IntegrityError as e:
                print(f"Error adding season to MariaDB Plateform: {e}")
                print("Season : " + str(season_file))
            
            db_connection.commit_db()

        season_id = season_entity.get_season_id(season_file)

        update_episode(db_connection, full_path, season_id)


def update_episode(db_connection, season_path, season_id):

    episode_file_entity     = EpisodeFileEntity(db_connection.connection)
    episode_video_entity    = EpisodeVideoEntity(db_connection.connection)

    all_episodes = list_episode(season_path)

    for episode in all_episodes:
        full_path = find_file(episode, season_path)
        episode_hashcode = get_file_hashcode(full_path)
        episode_quality = get_quality(full_path)
        episode_file = File(episode, episode_hashcode, episode_quality)
        episode_file.set_second_link(season_id)
        
        if not episode_file_entity.episode_file_exists_by_hashcode(episode_file) :
            print("Add episode : " + str(episode))
            episode_name = get_file_name(episode)
            episode_duration = get_duration(full_path)
            episode_video = Video(episode_name, episode_duration)

            if not episode_video_entity.episode_video_exists(episode_video, season_id):
                try:
                    episode_video_id = episode_video_entity.insert_episode_video(episode_video)
                except Exception as e:
                    print(f"Error adding episode video to MariaDB Plateform: {e}")
                    print("Episode video : " + str(episode_file))
            else:
                episode_video_id = episode_video_entity.get_episode_video_id(episode_video, season_id)

            try:
                episode_file.set_link(episode_video_id)

                episode_file_entity.insert_episode_file(episode_file)
            except Exception as e:
                print(f"Error adding episode file to MariaDB Plateform: {e}")
                print("Episode file : " + str(episode_file))

            db_connection.commit_db()


def update_movies(db_connection, path):

    movie_file_entity       = MovieFileEntity(db_connection.connection)

    all_movies = list_movies(path)

    for movie in all_movies:
        full_path = find_file(movie, path)
        movie_hashcode = get_file_hashcode(full_path)
        movie_quality = get_quality(full_path)
        movie_file = File(movie, movie_hashcode, movie_quality)

        if not movie_file_entity.movie_file_exists_by_hashcode(movie_file) :
            add_movie(db_connection, movie, full_path, movie_file, movie_file_entity)


    return 


def add_movie(db_connection, movie, full_path, movie_file, movie_file_entity):
    
    movie_video_entity      = MovieVideoEntity(db_connection.connection)

    print("Add movie : " + str(movie))
    movie_name = get_file_name(movie)
    movie_duration = get_duration(full_path)
        
    movie_video = Video(movie_name, movie_duration)

    if not movie_video_entity.movie_video_exists(movie_video):
        try :
            movie_video_id = movie_video_entity.insert_movie_video(movie_video)
        except mariadb.IntegrityError as e:
            print(f"Error adding movie video to MariaDB Plateform: {e}")
            print("Movie video : " + str(movie_file))
    else :
        movie_video_id = movie_video_entity.get_movie_video_id(movie_video)

    try:
        movie_file.set_link(movie_video_id)
        movie_file_entity.insert_movie_file(movie_file)
    except mariadb.IntegrityError as e:
        print(f"Error adding movie file to MariaDB Plateform: {e}")
        print("Movie file : " + str(movie_file))
    
    db_connection.commit_db()


def list_series(path):
    all_series = []
    for serie in os.listdir(path):
        all_series.append(serie)
    
    return all_series


def list_season(path):
    all_season = []
    for season in os.listdir(path):
        if season != "ID.txt":
            all_season.append(season)
    
    return all_season


def list_episode(path):
    all_episode = []
    for (repertoire, sous_repertoires, fichiers) in os.walk(path):
        for files in fichiers:
            if files != "ID.txt":
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
    file_name = os.path.splitext(file)[0]
    file_name = file_name.split('[')[0]
    return file_name


def get_duration(file):
    video = TinyTag.get(file)
    duration = time.strftime('%H:%M:%S', time.gmtime(video.duration))
    return duration


def get_quality(file):
    video = get_video_properties(file)

    if video['width'] >=3800 :
        video_quality = "4K"
    elif video['width'] >= 2000 and video['width'] < 3800:
        video_quality = "2K"
    elif video['width'] >= 1700 and video['width'] < 2000:
        video_quality = "FullHD"
    elif video['width'] >= 1000 and video['width'] < 1700:
        video_quality = "HD"
    elif video['width'] < 1000:
        video_quality = "SD"

    return video_quality
