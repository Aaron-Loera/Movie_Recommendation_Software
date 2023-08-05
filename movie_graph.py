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

    #searches for the specified movie in the specified genre
    def find_movie(self, starting_genre, target_movie):
        for movie in self.graph[starting_genre]:
            if movie.name == target_movie:
                return movie.get_movie_information()
        return False


