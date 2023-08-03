#imports the MovieVertex class from the movie_vertex file and MovieGraph from the movie_graph file
from movie_vertex import MovieVertex
from movie_graph import MovieGraph

#Creating objects to represnt all the movies for the recommendation software
iron_man = MovieVertex("Iron Man", "Superhero", 4.5, "The newly found hero Iron Man fights against his ex-mentor!")
iron_man2 = MovieVertex("Iron Man 2", "Superhero", 4, "Iron Man returns as he has to face the consequences of his past.")
spider_man = MovieVertex("Spider-Man", "Superhero", 4.5, "A teenager gain incredible powers when he gets bit by a spider.")
prisoners = MovieVertex("Prisoners", "Suspense", 5, "Two fathers desperatley search for their missing children.")
arrival = MovieVertex("Arrival", "Suspense", 3.5, "A professor is needed for her translating skills when aliens arive to earth.")
nope = MovieVertex("NOPE", "Suspense", 5, "Two cowboy siblings attempt to unravel the mystery of an alien spaceship in their town.")
baby_driver = MovieVertex("Baby Driver", "Action", 4.5, "A young merc is dragged into the world of bank robberies, car chases, and gun fights.")
john_wick = MovieVertex("John Wick", "Action", 4, "A retired hitman goes back into the world of violence to avenge his dog.")
john_wick2 = MovieVertex("John Wick 2", "Action", 3, "John Wick returns when a previous contractor blackmails him into doing his bidding.")
john_wick3 = MovieVertex("John Wick 3", "Action", 5, "John Wick is injured, alone, and desperate as he fights of the high table.")
smile = MovieVertex("Smile", "Horror", 3, "A therpaist gets passed a cures that causes her to spiral into delusions and insanity.")
the_conjuring = MovieVertex("The Conjuring", "Horror", 4, "Two paranormal hunters try to solve the mystery of a demons presence in a clients home.")
jigsaw = MovieVertex("Jig-Saw", "Horror", 2.5, "A group of stangers try to escape a maze of horrible torture and suffering.")
the_hangover = MovieVertex("The Hangover", "Comedy", 4.5, "3 friends look for their missing 4th member after a late night party in Las Vegas.")
the_hitmans_bodyguard = MovieVertex("The Hitman's Bodyguard", "Comedy", 4, "An uptight bodyguard is forced to protect a unique natured hitman.")
the_hitmans_bodyguard2 = MovieVertex("The Hitman's Bodyguard 2", "Comedy", 3, "Our favorite bodyguard returns to save our previous hitman's wife.")


#workspace
iron_man.add_recommended_movies(iron_man2)
iron_man2.add_recommended_movies(iron_man)

movie_graph = MovieGraph()

movie_graph.add_movie(iron_man)
movie_graph.add_movie(iron_man2)
movie_graph.add_movie(jigsaw)
movie_graph.add_movie(arrival)


#beginning of software recommendation system
def software_recommendation(graph_name):
    #asks for the users input
    user_choice = input("Welcome to Aaron's Movie Recommendations! We're glad to see you here and hope to provide you with the best movies for your taste! Let us know if you're looking for a specific movie or if you would like to see out recommendations. Please type (r) if you would like to see our recommendations or (s) if you want to see if we have a particular movie: ")

    #checks if the input is a valid option
    while (user_choice != 'r') and (user_choice != 's'):
        user_choice = input("Sorry that was an invalid option. Please type (r) if you would like to see our recommendations or (s) if you want to see if we have a particular movie: ")

    #lets the user choose which genre they would like to explore
    if user_choice == 'r':
        genres = [genre for genre in graph_name.graph]
        print(f"Here are our genres we have available: {genres}")
        user_choice = input("Which genre would you like to explore: ")
    
    #returns if the movie provided by the user exists within the graph
    else:
        print("Great, we hope we have the movie you're looking for...")
        user_choice = input("Please type in the movie name you are searching for: ")
        
software_recommendation(movie_graph)


