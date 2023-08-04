#Creates a class that combines all movie vertices into a traversible graph
class MovieGraph():
    def __init__(self):
        self.graph = {}
    
    #adds a movie vertex to the corresponding genre in graph
    def add_movie(self, movie_vertex):
        if movie_vertex.genre in self.graph:
            self.graph[movie_vertex.genre].append(movie_vertex)
        else:
            self.graph[movie_vertex.genre] = [movie_vertex]

    #searches for the specified movie using depth-first search
    def find_movie(self, target):
        pass