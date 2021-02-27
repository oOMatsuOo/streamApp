class Video:
    
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
    
    def __str__(self):
        name_string = "Name : " + str(self.name) + "\n"
        duration_string = "Duration : " + str(self.duration) + "\n"

        return name_string + duration_string
