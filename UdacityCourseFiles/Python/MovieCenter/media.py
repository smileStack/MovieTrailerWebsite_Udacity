import webbrowser
class Media():
    #constructor of the Media class
    def __init__(self, title, poster_image,trailer):
        self.title = title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer

    '''Uses the webbrowser module to open
    an instance of a trailer.
    '''
    def Show_trailer(self):
         webbrowser.open(self.trailer)
