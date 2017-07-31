"""This module provide the movie class."""

import webbrowser


class Movie(object):
    """This class provide a way to store movie related information"""
    VALID_RATING = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, movie_title, movie_storyline, movie_poster, movie_trailer):
        """This is the constructor for Movie class"""

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    def show_title(self):
        """This method print the title of the movie"""
        print self.title

    def show_trailer(self):
        """This method opens the trailer of this movie in the web browser"""
        webbrowser.open(self.trailer_youtube_url)
