#Creates a class that combines all movie vertices into a traversible graph
class MovieGraph():
    def __init__(self):
        self.graph = {}
    
    #adds a movie vertex to a graph
    def add_movie(self, movie_vertex):
        self.graph[movie_vertex.name] = movie_vertex.edges