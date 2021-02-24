from python_modules.classes.season import Season
from python_modules.classes.episode import Episode

class Serie:
   
    def __init__(self, serie):
        self.id = serie[0]
        self.name = serie[1]
        self.genres = serie[2]
        self.number_of_episodes = serie[3]
        self.number_of_seasons = serie[4]
        self.overview = serie[5]
        self.season = []
    

    def addSeason(self, season):
        self.season.append(season)
    

    def __str__(self):
        id_string = "ID : " + str(self.ID) + "\n"
        name_string = "Name : " + str(self.name) + "\n"
        genres_string = "Genres : " + str(self.genres) + "\n"
        number_of_episodes_string = "Number Of Episodes : " + str(self.number_of_episodes) + "\n"
        number_of_seasons_string = "Number Of Seasons : " + str(self.number_of_seasons) + "\n"
        overview_string = "Overview : " + str(self.overview) + "\n"
        seasons_string = "Season : "
        for season in self.season:
            seasons_string += str(season) + "\n"

        return id_string + name_string + genres_string + number_of_episodes_string + number_of_seasons_string + overview_string + seasons_string