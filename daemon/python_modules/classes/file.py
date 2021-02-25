class File:
    def __init__(self, name, hashcode, link):
        self.name = name
        self.hashcode = hashcode
        self.link = link
    
    def __init__(self, name, hashcode):
        self.name = name
        self.hashcode = hashcode
        self.link = 'null'
    
    def set_link(self, link):
        self.link = link

    def __str__(self):
        name_string = "Name : " + str(self.name) + "\n"
        hashcode_string = "Hash Code : " + str(self.hashcode) + "\n"
        link_string = "Link : " + str(self.link) + "\n"
 
        return name_string + hashcode_string + link_string
