"""A program to create movies objects and display them on a website page"""

import media
import fresh_tomatoes

# create movie objects:
toy_story = media.Movie(
    "Toy Story",
     "A story of a boy and his toys that come to life",
    "https://pixar-planet.fr/wp-content/uploads/2010/04/affiche-toy-story-23.jpg",  # NOQA
    "https://www.youtube.com/watch?v=4KPTXpQehio")

incredibles = media.Movie(
    "The Incedibles",
     "A story of a family of superheros",
    "https://1.bp.blogspot.com/-Usr_CYMyk9c/T-mjyFKhrKI/AAAAAAAAHtw/8lvQ9TjaKAw/s1600/The+Incredibles+%282004%29+2.jpg",  # NOQA
    "https://www.youtube.com/watch?v=-UaGUdNJdRQ")

nemo = media.Movie(
    "Finding Nemo",
    "A story of a fish lost in ocean",
    "http://www.pixartalk.com/wp-content/uploads/2009/06/nemogerman.jpg",
    "https://www.youtube.com/watch?v=bMtzgW-FVLY")

ratatouille = media.Movie(
    "Ratatouille",
    "A story of a rat who likes cooking",
    "https://movieposters2.com/images/671363-b.jpg",
    "https://www.youtube.com/watch?v=NgsQ8mVkN8w")

transylvania = media.Movie(
    "Hotel Transylvania",
    "A story of a vampire who has a hotel for monsters",
    "https://m.media-amazon.com/images/M/MV5BMTM3NjQyODI3M15BMl5BanBnXkFtZTcwMDM4NjM0OA@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=FYgzizpCTKU")

lion_king = media.Movie(
    "The Lion King",
    "A story of a lion who lost his dad and ran away then return back " +
    "to get his right in thrown and be the king of animals",
    "https://vignette.wikia.nocookie.net/disney/images/c/cb/The_Lion_King_Textless_poster_1.jpg/revision/latest?cb=20140810104158",  # NOQA
    "https://www.youtube.com/watch?v=4sj1MT05lAA")

# create a list of movies:
movie_list = [toy_story, incredibles, nemo, ratatouille, transylvania,
              lion_king]

# use fresh_tomatoes file to display the list:
fresh_tomatoes.open_movies_page(movie_list)

# show valid ratings of movie class
print "movie valid rarings are : ", media.Movie.VALID_RATING

# show class documenation
print "class documentation : ", media.Movie.__doc__

# show class name
print "class name is ", media.Movie.__name__

# show file/module in which this class was defined
print "file name is ", media.Movie.__module__
