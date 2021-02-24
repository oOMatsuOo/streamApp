class Video:

    def __init__(self, video):
        self.name = video[0]
        self.video_type = video[1]
        self.link = video[2]
        self.duration = video[3]
    
    def __str__(self):
        name_string = "Name : " + str(self.name) + "\n"
        video_type_string = "Video Type : " + str(self.video_type) + "\n"
        link_string = "Link to : " + str(self.link) + "\n"
        duration_string = "Duration : " + str(self.duration) + "\n"

        return name_string + video_type_string + link_string + duration_string