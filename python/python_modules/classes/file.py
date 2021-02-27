class File:

    def __init__(self, file):
        self.name = file[0]
        self.hashcode = file[1]
        self.link = file[2]
    

    def __str__(self):
        name_string = "Name : " + str(self.name) + "\n"
        hashcode_string = "Hash Code : " + str(self.hashcode) + "\n"
        link_string = "Link : " + str(self.link) + "\n"

        return name_string + hashcode_string + link_string