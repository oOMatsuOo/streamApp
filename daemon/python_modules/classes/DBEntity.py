import mariadb

from python_modules.classes.video import Video
from python_modules.classes.file import File

class dbConnect:

    # Try to init the connection with the DB
    # Raise an Exception if a problem occure

    def __init__(self):
        try:
            self.connection = self.create_connection()
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            raise Exception("Impossible to connect to DB.")
    

    # Create a connection with the principal DB 

    def create_connection(self):
        conn = mariadb.connect(
            user="user",
            password="pwd",
            host="streamapp_mariadb_1",
            database="video"
        )

        return conn


    def commit_db(self):
        self.connection.commit()


    def close_connection(self):
        self.connection.close()


class MovieFileEntity:

    def __init__(self, conn):
        self.conn = conn


    def insert_movie_file(self, movie):
        cur = self.conn.cursor()

        query = "INSERT INTO files (file_name, hashcode, video_link, quality) VALUES (?, ?, ?, ?)"
        cur.execute(query,(movie.name, movie.hashcode, movie.link, movie.quality))

        cur.close()


    def movie_file_exists_by_hashcode(self, movie):
        cur = self.conn.cursor()

        query = "SELECT * FROM files WHERE hashcode=?"
        cur.execute(query,(movie.hashcode,))

        response = cur.fetchall()

        if response:
            return True

        return False


class MovieVideoEntity:

    def __init__(self, conn):
        self.conn = conn
    

    def insert_movie_video(self, movie):
        cur = self.conn.cursor()
    
        query = "INSERT INTO videos (title, duration, video_type) VALUES (?, ?, ?) RETURNING id;"
        cur.execute(query,(movie.name, movie.duration, 'movie'))
        movie_video_id = cur.fetchone()[0]

        cur.close()

        return movie_video_id
    

    def movie_video_exists(self, movie):
        cur = self.conn.cursor()

        if (movie.name == "Logan"):
            print(movie)

        query = "SELECT * FROM videos vd WHERE vd.title = ?"
        cur.execute(query, (movie.name,))

        response = cur.fetchall()

        cur.close()

        if response:
            return True

        return False


    def get_movie_video_id(self, movie):
        cur = self.conn.cursor()

        query = "SELECT vd.id FROM videos vd WHERE vd.title = ?"
        cur.execute(query, (movie.name,))

        response = cur.fetchone()[0]

        cur.close()

        return response


class EpisodeFileEntity:

    def __init__(self, conn):
        self.conn = conn


    def insert_episode_file(self, episode):
        cur = self.conn.cursor()

        query = "INSERT INTO files (file_name, hashcode, video_link, season_dir_link, quality) VALUES (?, ?, ?, ?, ?)"
        cur.execute(query,(episode.name, episode.hashcode, episode.link, episode.second_link, episode.quality))

        cur.close()


    def episode_file_exists_by_hashcode(self, episode):
        cur = self.conn.cursor()

        query = "SELECT * FROM files WHERE hashcode=?"
        cur.execute(query,(episode.hashcode,))

        response = cur.fetchall()

        if response:
            return True

        return False


class EpisodeVideoEntity:
    
    def __init__(self, conn):
        self.conn = conn
    

    def insert_episode_video(self, episode):
        cur = self.conn.cursor()

        query = "INSERT INTO videos (title, duration, video_type) VALUES (?, ?, ?) RETURNING id;"
        cur.execute(query,(episode.name, episode.duration, 'serie'))
        episode_video_id = cur.fetchone()[0]

        cur.close()

        return episode_video_id
    

    def episode_video_exists(self, episode, season_id):
        cur = self.conn.cursor()

        query = "SELECT * FROM videos vd, files fl WHERE vd.id = fl.video_link and fl.season_dir_link = ? and vd.title = ?"
        cur.execute(query, (season_id, episode.name))

        response = cur.fetchall()

        cur.close()

        if response:
            return True

        return False


    def get_episode_video_id(self, episode, season_id):
        cur = self.conn.cursor()

        query = "SELECT vd.id FROM videos vd, files fl WHERE vd.id = fl.video_link and fl.season_dir_link = ? and vd.title = ?"
        cur.execute(query, (season_id, episode.name))

        response = cur.fetchone()[0]

        cur.close()

        return response


class SeasonFileEntity:

    def __init__(self, conn):
        self.conn = conn
    

    def insert_season_file(self, season):
        cur = self.conn.cursor()

        query = "INSERT INTO directory (dir_name, hashcode, serie_dir_link, file_type) VALUES (?, ?, ?, ?)"
        cur.execute(query,(season.name, season.hashcode, season.link, 'season'))

        cur.close()


    def season_file_exists_by_hashcode(self, season):
        cur = self.conn.cursor()

        query = "SELECT * FROM directory WHERE hashcode=?"
        cur.execute(query,(season.hashcode,))

        response = cur.fetchall()

        if response:
            return True

        return False


    def get_season_id(self, season):
        cur = self.conn.cursor()

        query = "SELECT id FROM directory WHERE hashcode=?"
        cur.execute(query,(season.hashcode,))
        season_id = cur.fetchone()[0]

        cur.close()

        return season_id


class SerieFileEntity:

    def __init__(self, conn):
        self.conn = conn
    

    def insert_serie_file(self, serie):
        cur = self.conn.cursor()

        query = "INSERT INTO directory (dir_name, hashcode, file_type) VALUES (?, ?, ?);"
        cur.execute(query,(serie.name, serie.hashcode, 'serie'))

        cur.close()


    def serie_file_exists_by_hashcode(self, serie):
        cur = self.conn.cursor()

        query = "SELECT * FROM directory WHERE hashcode=?"
        cur.execute(query,(serie.hashcode,))

        response = cur.fetchall()
        cur.close()

        if response:
            return True

        return False


    def get_serie_id(self, serie):
        cur = self.conn.cursor()

        query = "SELECT id FROM directory WHERE hashcode=?"
        cur.execute(query,(serie.hashcode,))
        serie_id = cur.fetchone()[0]

        cur.close()

        return serie_id
