from python_modules.classes.episode import Episode

class Season:
    
    def __init__(self, season):
        self.name = season[0]
        self.overview = season[1]
        self.season_number = season[2]
        self.number_of_episodes = season[3]
        self.episode = []
        self.serie_id


    def set_serie_id(self, serie_id):
        self.serie_id = serie_id


    def addEpisode(self, episode):
        self.episode.append(episode)

    
    def __str__(self):
        name_string = "Name : " + str(self.name) + "\n"
        overview_string = "Overview : " + str(self.overview) + "\n"
        season_number_string = "Season Number : " + str(self.season_number) + "\n"
        number_of_episodes_string = "Number Of Episodes : " + str(self.number_of_episodes) + "\n"
        episode_string = "Episodes : "
        for episode in self.episode:
            episode_string += str(episode) + "\n"

        return name_string + season_number_string + number_of_episodes_string + overview_string + episode_string
