"""This code is used as a class to create movies"""

import webbrowser


class Movie():
    VALID_RATING = ["R", "PG", "G", "PG-13"]

    def __init__(self, movie_title, movie_story_line,
                 poster_image, youtube_trailer):
        """ class constructor """
        self.title = movie_title
        self.story_line = movie_story_line
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer
