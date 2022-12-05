import webbrowser
class Movie():
    def __init__(self,movie_name,movie_storyline,movie_image,movie_trailer):
        self.title=movie_name
        self.storyline=movie_storyline
        self.image_url=movie_image
        self.movie_trailer_url=movie_trailer

    def show_trailer(self):
        webbrowser.open(self.movie_trailer_url)
