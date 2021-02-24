class Movie:

    def __init__(self, movie):
        self.id = movie[0]
        self.genres = movie[1]
        self.name = movie[2]
        self.overview = movie[3]
    

    def __str__(self):
        id_string = "ID : " + str(self.id) + "\n"
        genres_string = "Genres : " + str(self.genres) + "\n"
        name_string = "Name : " + str(self.name) + "\n"
        overview_string = "Overview : " + str(self.overview) + "\n"

        return id_string + genres_string + name_string + overview_string
