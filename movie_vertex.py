#Creates a movie object that acts as a vertex
class MovieVertex():
    def __init__(self, name, genre, rating, description):
        self.name = name
        self.genre = genre
        self.rating = rating
        self.description = description
        self.edges = {}

    #retuns all the following information of the current movie object
    def get_movie_information(self):
        return self.genre, self.rating, self.description

    #adds a new edge to the current vertex
    def add_recommended_movies(self, new_movie):
        self.edges[new_movie.name] = list(new_movie.get_movie_information())


# movie1 = MovieVertex('Movie 1', 'Action', 4, 'This is movie one')
# movie2 = MovieVertex('Movie 2', 'Action', 3, 'The second movie')

# movie1.add_recommended_movies(movie2)

# print(movie1.edges)