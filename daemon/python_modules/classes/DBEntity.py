import mariadb

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
            host="mariadb_mariadb_1",
            database="video"
        )

        return conn


    def commit_db(self):
        self.conn.commit()


    def close_connection(self):
        self.connection.close()


class MovieFileEntity:

    def __init__(self, conn):
        self.conn = conn


    def insert_movie_file(self, movie):
        cur = self.conn.cursor()

        query = "INSERT INTO files (file_name, hashcode, video_link, file_type) VALUES (?, ?, ?, ?)"
        cur.execute(query,(movie.name, movie.hashcode, movie.link, 'video'))

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


class EpisodeFileEntity:

    def __init__(self, conn):
        self.conn = conn


    def insert_episode_file(self, episode):
        cur = self.conn.cursor()

        query = "INSERT INTO files (file_name, hashcode, video_link, file_type) VALUES (?, ?, ?, ?)"
        cur.execute(query,(episode.name, episode.hashcode, episode.link, 'video'))

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


class SeasonFileEntity:

    def __init__(self, conn):
        self.conn = conn
    

    def insert_season_file(self, season):
        cur = self.conn.cursor()

        query = "INSERT INTO files (file_name, hashcode, file_type) VALUES (?, ?, ?)"
        cur.execute(query,(season.name, season.hashcode, 'season'))

        cur.close()


    def season_file_exists_by_hashcode(self, season):
        cur = self.conn.cursor()

        query = "SELECT * FROM files WHERE hashcode=?"
        cur.execute(query,(season.hashcode,))

        response = cur.fetchall()

        if response:
            return True

        return False


class SerieFileEntity:

    def __init__(self, conn):
        self.conn = conn
    

    def insert_serie_file(self, serie):
        cur = self.conn.cursor()

        query = "INSERT INTO files (file_name, hashcode, file_type) VALUES (?, ?, ?)"
        cur.execute(query,(serie.name, serie.hashcode, 'serie'))

        cur.close()


    def serie_file_exists_by_hashcode(self, serie):
        cur = self.conn.cursor()

        query = "SELECT * FROM files WHERE hashcode=?"
        cur.execute(query,(serie.hashcode,))

        response = cur.fetchall()

        if response:
            return True

        return False


