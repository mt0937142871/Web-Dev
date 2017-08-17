"""This module setup the website for movie trailers"""

import movie
import fresh_tomatoes


''' Instance of Toy Story, including tytle, description,
    poster, and trailer url '''
TOY_STORY = movie.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

''' Instance of AVATAR, including tytle, description,
    poster, and trailer url '''
AVATAR = movie.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=d1_JBMrrYw8")

''' Instance of Lion King, including tytle, description,
    poster, and trailer url '''
LION_KING = movie.Movie(
    "Lion King",
    "A story of lions fight for the thrones",
    "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=4sj1MT05lAA")

''' Instance of Begin Again, including tytle, description,
    poster, and trailer url '''
BEGIN_AGAIN = movie.Movie(
    "Begin Again",
    "A man and woman fail on their careers, and start again",
    "https://upload.wikimedia.org/wikipedia/en/b/bd/Begin_Again_film_poster_2014.jpg",  # noqa
    "https://www.youtube.com/watch?v=uTRCxOE7Xzc")

''' Instance of Beauty and the Beast, including tytle, description,
    poster, and trailer url '''
BEAUTY_AND_THE_BEAST = movie.Movie(
    "Beauty and the Beast",
    "A love story between a pretty and a beast",
    "https://upload.wikimedia.org/wikipedia/en/d/d6/Beauty_and_the_Beast_2017_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=e3Nl_TCQXuw&t=1s")

''' Instance of Rise of the Planet of the Apes, including tytle, description,
    poster, and trailer url '''
RISE_OF_THE_PLANET_OF_THE_APES = movie.Movie(
    "Rise of the Planet of the Apes",
    "A story of apes being smart and think and claim their world",
    "https://upload.wikimedia.org/wikipedia/en/8/81/Rise_of_the_Planet_of_the_Apes_Poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=28Z_D9Grh18")

''' Instance of Love Rosie, including tytle, description,
    poster, and trailer url '''
LOVE_ROSIE = movie.Movie(
    "Love, Rosie",
    "A love story between two people",
    "https://upload.wikimedia.org/wikipedia/en/e/eb/Love%2C_Rosie_%28film%29_UK_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=5zL3YJKygd4")

''' A list consists of all the movie instances '''
MOVIES = [TOY_STORY, AVATAR, LION_KING, BEGIN_AGAIN,
          BEAUTY_AND_THE_BEAST, RISE_OF_THE_PLANET_OF_THE_APES,
          LOVE_ROSIE]


''' Calling open_movies_page with MOVIES to create the trailer website '''
fresh_tomatoes.open_movies_page(MOVIES)
