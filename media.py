import webbrowser


class Movie():
    """ This is a class that contains information about Movie

    Attributes:
        title (str): Title of movie
        storyline (str): Storyline for movie
        poster_image_url (str): Poster image for movie
        trailer_youtube_url (int): URL for movie trailer
    """

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
