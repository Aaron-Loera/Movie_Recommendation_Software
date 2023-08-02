#Creates a movie object that acts as a vertex
class MovieVertex():
    def __init__(self, name, genre, rating, description):
        self.name = name
        self.genre = genre
        self.rating = rating
        self.description = description
        self.edges = {}
    
    #adds a new edge to the current vertex
    def add_recommended_movies(self, new_movie):
        self.edges[new_movie.name] = [new_movie.genre, new_movie.rating, new_movie.description]


movie1 = MovieVertex("The Movie", "Horror", 4.5, "A movie where things happend")
movie2 = MovieVertex("The Movie 2", "Action", 3.2, "A movie after the first one")
movie1.add_recommended_movies(movie2)

print(movie1.edges)