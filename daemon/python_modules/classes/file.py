class File:
    
    def __init__(self, name, hashcode, quality):
        self.name = name
        self.hashcode = hashcode
        self.quality = quality
        self.link = 'null'
        self.second_link = 'null'
    
    def set_link(self, link):
        self.link = link
    
    def set_second_link(self, link):
        self.second_link = link

    def __str__(self):
        name_string = "Name : " + str(self.name) + "\n"
        hashcode_string = "Hash Code : " + str(self.hashcode) + "\n"
        quality_string = "Quality : " + str(self.quality) + "\n"
        link_string = "Link : " + str(self.link) + "\n"
 
        return name_string + hashcode_string + quality_string + link_string
