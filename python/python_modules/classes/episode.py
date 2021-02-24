class Episode:

    def __init__(self, episode):
        self.name = episode[0]
        self.episode_number = episode[1]
        self.overview = episode[2]
        self.serie_id
        self.season_id

    
    def set_season_id(self, season_id):
        self.season_id = season_id


    def set_serie_id(self, serie_id):
        self.serie_id = serie_id


    def __str__(self):
        name_string = "Name : " + str(self.name) + "\n"
        overview_string = "Overview : " + str(self.overview) + "\n"
        episode_number_string = "Episode Number : " + str(self.episode_number) + "\n"

        return name_string + episode_number_string + overview_string