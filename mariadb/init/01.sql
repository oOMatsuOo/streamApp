CREATE OR REPLACE DATABASE video;

USE video;


CREATE TABLE IF NOT EXISTS series (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200),
    season INT,
    episodes INT,
    tmdb_id VARCHAR(50),
    CONSTRAINT unique_tmdb_id UNIQUE (tmdb_id)
);


CREATE TABLE IF NOT EXISTS film_series (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200)
);


CREATE TABLE IF NOT EXISTS movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200),
    tmdb_id VARCHAR(50),
    CONSTRAINT unique_tmdb_id UNIQUE (tmdb_id)
);


CREATE TABLE IF NOT EXISTS seasons (
    id INT AUTO_INCREMENT PRIMARY KEY,
    season_number INT,
    serie_link INT,
    FOREIGN KEY(serie_link) REFERENCES series (id) ON UPDATE CASCADE,
    CONSTRAINT unique_season_for_serie_number UNIQUE (season_number, serie_link)
);


CREATE TABLE IF NOT EXISTS episodes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    episode_number INT,
    title VARCHAR(200),
    season_link INT,
    FOREIGN KEY(season_link) REFERENCES seasons (id) ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS videos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200),
    duration TIME,
    video_type ENUM('movie','serie'),
    episode_link INT,
    FOREIGN KEY(episode_link) REFERENCES episodes (id) ON UPDATE CASCADE,
    movie_link INT,
    FOREIGN KEY(movie_link) REFERENCES movies (id) ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS files(
    id INT AUTO_INCREMENT PRIMARY KEY,
    file_name VARCHAR(200) NOT NULL,
    hashcode VARCHAR(200),
    video_link INT,
    FOREIGN KEY(video_link) REFERENCES videos (id) ON UPDATE CASCADE,
    serie_link INT,
    FOREIGN KEY(serie_link) REFERENCES series (id) ON UPDATE CASCADE,
    CONSTRAINT unique_file_name UNIQUE (file_name),
    CONSTRAINT unique_hashcode UNIQUE (hashcode)
);
