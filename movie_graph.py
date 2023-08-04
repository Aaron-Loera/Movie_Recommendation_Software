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

    #searches for the specified movie using breadth-first search
    def find_movie(self, starting_genre, target_movie):
        visited = set()
        queue = [self.graph[starting_genre]]

        while queue:
            current_vertex = queue.pop()
            if current_vertex not in visited:
                visited.add(current_vertex)
                if current_vertex == target_movie:
                    print("Found your movie!")
                    return visited
                else:
                    for neighbor in self.graph[current_vertex]:
                        if neighbor not in visited:
                            queue.insert(0, neighbor.name)
        return False


