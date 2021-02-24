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
    

    # Create a connection with the DB 

    def create_connection(self):
        conn = mariadb.connect(
            user="user",
            password="pwd",
            host="mariadb_mariadb_1",
            database="video"
        )

        return conn


class MovieFileEntity:

    def __init__(self, conn):
        self.conn = conn


    # Insert a movie file class into the DB

    def insert_movie_file(self, movie):
        if not self.movie_file_already_exist(movie) :
            cur = self.conn.cursor()

            query = "INSERT INTO files (file_name, hashcode, video_link) VALUES (?, ?, ?)"
            cur.execute(query,(movie.name, movie.hashcode, movie.link))

            cur.close()
            self.conn.commit()


    def movie_file_already_exist(self, movie):
        cur = self.conn.cursor()

        query = "SELECT * FROM files WHERE video_link=?"
        cur.execute(query,(movie.link,))

        response = cur.fetchall()

        if response:
            return True

        return False


    # Return the movie video id
    # Raise Exception if no id is found

    def get_movie_video_id_from_movie_file_hashcode(self, movie):
        cur = self.conn.cursor()

        query = "SELECT video_link FROM files WHERE hashcode=?"
        cur.execute(query,(movie.hashcode,))

        movie_video_id = cur.fetchone()[0]

        if movie_video_id:
            raise Exception('No movie File with hashcode selected')
            
        return movie_video_id


class MovieVideoEntity:

    def __init__(self, conn):
        self.conn = conn
    

    # Insert a movie video class into the DB
    # Return the ID 

    def insert_movie_video(self, movie):
        if not self.movie_video_already_exists(movie):
            cur = self.conn.cursor()
    
            query = "INSERT INTO videos (title, duration, video_type, movie_link) VALUES (?, ?, ?, ?) RETURNING id;"
            cur.execute(query,(movie.name, movie.duration, movie.video_type, movie.link))
            movie_video_id = cur.fetchone()[0]

            cur.close()
            self.conn.commit()

            return movie_video_id

        return self.get_movie_video_id(movie)


    def movie_video_already_exists(self, movie):
        cur = self.conn.cursor()

        query = "SELECT * FROM videos WHERE movie_link=?"
        cur.execute(query,(movie.link,))

        response = cur.fetchall()

        if response:
            return True

        return False


    def movie_exists_by_movie_video_id(self, movie):
        cur = self.conn.cursor()

        query = "SELECT * FROM movies WHERE id=?"
        cur.execute(query,(movie.link,))

        response = cur.fetchall()

        if response:
            return True

        return False


    # Return movie video ID
    # Raise an Exception if no movie video is found

    def get_movie_video_id(self, movie):
        cur = self.conn.cursor()

        query = "SELECT id FROM videos WHERE movie_link=?"
        cur.execute(query,(movie.link,))

        video_id = cur.fetchall()[0][0]

        cur.close()

        if not video_id:
            raise Exception('No movie video ID found')

        return video_id
    

class MovieEntity:

    def __init__(self, conn):
        self.conn = conn
    

    # Insert a movie class into the DB
    # Return the ID

    def insert_movie(self, movie):
        if not self.movie_already_exists(self.conn, movie):
            cur = self.conn.cursor()

            query = "INSERT INTO movies (title, tmdb_id) VALUES (?,?) RETURNING id"
            cur.execute(query, (movie.name, movie.id))
            movie_id = cur.fetchone()[0]

            cur.close()
            self.conn.commit()

            return movie_id
        
        return self.get_movie_id(movie)


    def movie_already_exists(self, movie):
        cur = self.conn.cursor()

        query = "SELECT * FROM movies WHERE tmdb_id=?"
        cur.execute(query,(movie.id,))

        response = cur.fetchall()
        cur.close()

        if response:
            return True

        return False
    

    # Return the movie ID
    # Raise an Exception if no movie is found
    
    def get_movie_id(self, movie):
        cur = self.conn.cursor()

        query = "SELECT id FROM movies WHERE tmdb_id=?"
        cur.execute(query,(movie.id,))

        movie_id = cur.fetchone()[0]

        if movie_id:
            raise Exception('No movie found with the tmdb ID')
        
        return movie_id
        

class EpisodeFileEntity:

    def __init__(self, conn):
        self.conn = conn

    
    # Insert a movie file class into the DB

    def insert_episode_file(self, episode):
        if not self.episode_file_already_exist(episode) :
            cur = self.conn.cursor()

            query = "INSERT INTO files (file_name, hashcode, video_link) VALUES (?, ?, ?)"
            cur.execute(query,(episode.name, episode.hashcode, episode.link))

            cur.close()
            self.conn.commit()


    def episode_file_already_exist(self, episode):
        cur = self.conn.cursor()

        query = "SELECT * FROM files WHERE video_link=?"
        cur.execute(query,(episode.link,))

        response = cur.fetchall()

        if response:
            return True

        return False


class EpisodeVideoEntity:

    def __init__(self, conn):
        self.conn = conn

    # Insert an episode video class into the DB
    # Return the ID
    
    def insert_episode_video(self, episode):
        if not self.episode_video_already_exists(episode):
            cur = self.conn.cursor()

            query = "INSERT INTO videos (title, duration, video_type, episode_link) VALUES (?, ?, ?, ?) RETURNING id;"
            cur.execute(query,(episode.name, episode.duration, episode.video_type, episode.link))

            episode_id = cur.fetchone()[0]
            cur.close()

            return episode_id
        
        return self.get_episode_id(episode)


    def episode_video_already_exists(self, episode):
        cur = self.conn.cursor()

        query = "SELECT * FROM videos WHERE episode_link=?"
        cur.execute(query,(episode.link,))

        response = cur.fetchall()

        if response:
            return True

        return False


    # Return the episode video ID
    # Raise an Exception if no episode video is found

    def get_episode_video_id(self, episode):
        cur = self.conn.cursor()

        query = "SELECT id FROM videos WHERE episode_link=?"
        cur.execute(query,(episode.link,))

        video_id = cur.fetchall()[0][0]

        cur.close()

        if not video_id:
            raise Exception('No episode videi ID found.')
            
        return video_id
        

class EpisodeEntity:

    def __init__(self, conn):
        self.conn = conn
    
    
    # Insert an episode class into the DB
    # Return the ID
    
    def insert_episode(self, episode):
        if not self.episode_already_exists(episode):
            cur = self.conn.cursor()

            query = "INSERT INTO episodes (episode_number, title, season_link) VALUES (?,?,?) RETURNING id"
            cur.execute(query, (episode.episode_number, episode.name, episode.season_id))

            episode_id = cur.fetchone()[0]
            cur.close()

            return episode_id
        
        return self.get_episode_id(episode)


    def episode_already_exists(self, episode):
        cur = self.conn.cursor()

        query = "SELECT * FROM episodes WHERE episode_number=? AND season_link=?"
        cur.execute(query,(episode.episode_number,episode.season_id))

        response = cur.fetchall()
        cur.close()

        if response:
            return True

        return False
    
    
    # Return the episode ID
    # Raise an Exception if no episode is found

    def get_episode_id(self, episode):
        cur = self.conn.cursor()

        query = "SELECT id FROM episodes WHERE episode_number=? AND season_link=?"
        cur.execute(query,(episode.episode_number,episode.season_id))

        episode_id = cur.fetchone()[0]

        if not episode_id:
            raise Exception('No episode found')

        return episode_id
    

class SeasonEntity:

    def __init__(self, conn):
        self.conn = conn


    # Insert a season class into the DB
    # Return the ID
    
    def insert_season(self, season):
        if not self.season_already_exists(season):
            cur = self.conn.cursor()

            query = "INSERT INTO seasons (season_number, serie_link) VALUES (?,?) RETURNING id"
            cur.execute(query, (season.season_number, season.serie_id))

            season_id = cur.fetchone()[0]
            cur.close()

            return season_id
        
        return self.get_season_id(season)


    def season_already_exists(self, season):
        cur = self.conn.cursor()

        query = "SELECT * FROM seasons WHERE season_number=? AND serie_link=?"
        cur.execute(query,(season.season_number,season.serie_id))

        response = cur.fetchall()
        cur.close()

        if response:
            return True

        return False
    
    
    # Return the season ID
    # Raise an Exception if no season is found

    def get_season_id(self, season):
        cur = self.conn.cursor()

        query = "SELECT id FROM seasons WHERE season_number=? AND serie_link=?"
        cur.execute(query,(season.season_number,season.serie_id))

        season_id = cur.fetchone()[0]

        if not season_id:
            raise Exception('No season found')

        return season_id
    

class SerieEntity:

    def __init__(self, conn):
        self.conn = conn
   

    # Insert a serie class into the DB
    # Return the ID
    
    def insert_serie(self, serie):
        if not self.serie_already_exists(serie):
            cur = self.conn.cursor()

            query = "INSERT INTO series (title, season, episodes, tmdb_id) VALUES (?,?,?,?) RETURNING id"
            cur.execute(query, (serie.name, serie.number_of_seasons, serie.number_of_episodes, serie.id))

            serie_id = cur.fetchone()[0]
            cur.close()

            return serie_id
        
        return self.get_serie_id(serie)


    def serie_already_exists(self, serie):
        cur = self.conn.cursor()

        query = "SELECT * FROM series WHERE tmdb_id=?"
        cur.execute(query,(serie.id,))

        response = cur.fetchall()
        cur.close()

        if response:
            return True

        return False
    
    
    # Return the serie ID
    # Raise an Exception if no serie is found

    def get_serie_id(self, serie):
        cur = self.conn.cursor()

        query = "SELECT id FROM series WHERE tmdb_id=?"
        cur.execute(query,(serie.id,))

        serie_id = cur.fetchone()[0]

        if not serie_id:
            raise Exception('No serie found')

        return serie_id
