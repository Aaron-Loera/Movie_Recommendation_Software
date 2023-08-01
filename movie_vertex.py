#Creates a movie object that acts as a vertex
class MovieVertex():
    def __init__(self, name, genre, rating, description):
        self.name = name
        self.genre = genre
        self.rating = rating
        self.description = description
        self.edges = {}


movie1 = MovieVertex("The Movie", "Horror", 4.5, "A movie where things happend")
print(movie1.rating)