#imports the MovieVertex class from the movie_vertex file
from movie_vertex import MovieVertex

#Asks for the users input
movie1 = MovieVertex("The Movie", "Horror", 4.5, "A movie where things happend")
movie2 = MovieVertex("The Movie 2", "Action", 3.2, "A movie after the first one")
movie1.add_recommended_movies(movie2)

print(movie1.edges)