
import media #import Parent class

class Media():
    #constructor of the Media class
    def __init__(self, title, poster_image,trailer):
        self.title = title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer

class TV_Show(Media):
    #calls the parent constructor and then creates attrinbutes unique to Child class
    def __init__(self, title, poster_image, trailer, episodes):
        Media.__init__(self, title, poster_image, trailer)
        self.episodes_list = episodes
