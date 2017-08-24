import re

class Movie:
    """
    This class will create a movie website. You could execute command to generate website which includes useful
    movie information you initialized for previewing.
    """

    # Constructor for initialize fields for movie object
    def __init__(self, movie_title, movie_storyline, trailer_youtube, poster_image):
        self.title = movie_title
        self.storyline = movie_storyline
        self.trailer_youtube_url = trailer_youtube
        self.poster_image_url = poster_image

    @classmethod
    def checkUrl(self, movies):
        results = []
        for movie in movies:
            pattern = re.compile(r'http(s)?:\/\//i')
            if pattern.match('hello world!'):
                print("great")
        return results