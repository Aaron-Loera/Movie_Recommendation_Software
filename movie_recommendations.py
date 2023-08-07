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

# print(movie_graph.graph)


#The software recommendation system
def software_recommendation(graph_name):

    #asks for the users input
    user_choice = input("Welcome to Aaron's Movie Recommendations! We're glad to see you here and hope to provide you with the best movies for your taste! Let us know if you're looking for a specific movie or if you would like to see out recommendations. Please type (r) if you would like to see our recommendations or (s) if you want to see if we have a particular movie: ")

    #checks if the input is a valid option
    while (user_choice != 'r') and (user_choice != 's'):
        user_choice = input("\nSorry that was an invalid option. Please type (r) if you would like to see our recommendations or (s) if you want to see if we have a particular movie: ")

    #calls the movie_recommendations function
    if user_choice == 'r':

        #calls the movie_recommendation function
        movie_chosen = movie_recommendations(graph_name)
        
        #asks the user if they want to continue their search
        users_input = continue_search()
        
        #find_other_movies is called and executes appropiate response for users_input
        find_other_movies(graph_name, users_input, movie_chosen)
    
    elif user_choice == 's':

        #calls the movie_search function
        movie_chosen = movie_search(graph_name)

        #asks the user if they want to continue their search
        users_input = continue_search()
            
        #if the user types yes the find_similar_movies method is called until they're happy with their results
        find_other_movies(graph_name, users_input, movie_chosen)
   

#Function that recommends various movies based on the chosen genre
def movie_recommendations(graph_name):

    #makes a list of all the genres in the movie graph and ask for the user to pick on
    genres_list = [genre for genre in graph_name.graph]
    print(f"\nHere are our genres we have available: {genres_list}")
    user_genre_choice = input("\nWhich genre would you like to to explore: ")

    #checks if the users choice is a valid genre
    while user_genre_choice not in genres_list:
        user_genre_choice = input("\nSorry that isn't a valid genre. Which genre would you like to explore: ")

    #shows all films under the chosen genre and asks the user to choose one
    chosen_genre = graph_name.graph[user_genre_choice]
    print(f"\nGreat choice! Here are the top films we recommend for this genre: {chosen_genre}")
    user_movie_choice = input("\nWhich film would you like to check out: ")

    #varifies if the users input is a valid movie choice
    movie_list = [movie.name for movie in chosen_genre]
    while user_movie_choice not in movie_list:
        user_movie_choice = input("\nSorry that isn't one of our listed films. Please pick which film you would like to check out: ")
    
    #identifies which movie the user has chosen and prints the movies information
    for movie in chosen_genre:
            if user_movie_choice == movie.name:
                print(f"\nAwesome pick! Here are all the details for {movie.name}: {movie.get_movie_information()}")
                return movie


#Function that searches for the given movie in the provided genre
def movie_search(graph_name):

    #makes a list of all the genres in the movie graph and ask for the user to pick on
    genre_list = [genre for genre in graph_name.graph]

    #askes the user for a specified movie name and movie genre
    user_movie_choice = input("\nWe hope we have the movie you're looking for. Please type in the movie name you are searching for: ")
    user_genre_choice = input(f"\nAwesome, and what genre does it fall under from the following {genre_list}: ")

    #checks if the users specified genre is in the provided genres
    while user_genre_choice not in genre_list:
        user_genre_choice = input("\nSorry that's not a valid genre. What genre does your movie fall in: ")
    
    #prints the appropiate message on whether the movie is found or not
    print("Alright let's check if we have your movie...")
    movie_search_result = movie_graph.find_movie(user_genre_choice, user_movie_choice)
    if movie_search_result == False:
        print("\nSorry it seems we don't have that movie in our inventory!\n")
        return None
    else:
        movie, movie_information = movie_search_result
        print(f"\nWe found your movie! Here are the following details for {user_movie_choice}: {movie_information}\n")
        return movie


#If applicable the software recommends similar movies to the user
def find_other_movies(graph_name, users_input, movie_chosen):
    #base case
    if users_input == 'n':
        print("\nThank you for using Aaron's Movie Recommendations.")

    #reursive step for searching for a movie
    elif users_input == 's':
        second_movie_chosen = movie_search(graph_name)

        #asks the user if they want to continue their search
        users_input = continue_search()
            
        #if the user types yes the find_similar_movies method is called until they're happy with their results
        find_other_movies(graph_name, users_input, second_movie_chosen)
    
    #recursive step for finding related movies
    elif users_input == 'r':

        #if movie_chosen is None then the user can either exit the program or go back to look at the genres
        if movie_chosen == None or movie_chosen.edges == {}:
            users_input2 = input("\nIt seems your chosen film doesn't have any related movies. Would you like to go back to see our genres? Please type (y)es to look out our genres or (n)o to exit our program: ")

            while (users_input2 != "y" and users_input2 != "n"):
                users_input2 = input(f"\nSorry that's not a valid option. Would you like to go back to see our genres? Please type (y)es to look out our genres or (n)o to exit our program: ")

            if users_input2 == "n":
                find_other_movies(graph_name, users_input2, movie_chosen)
            
            else:
                second_movie_chosen = movie_recommendations(graph_name)
                
                #asks the user if they want to continue their search
                users_input = continue_search()
            
                #if the user types yes the find_similar_movies method is called until they're happy with their results
                find_other_movies(graph_name, users_input, second_movie_chosen)

        #shows all the related films from the movie the user picked
        else:
            #all related films to the users current movie in string format
            related_films = [movie.name for movie in movie_chosen.edges.keys()]
            
            #asks which recommended movie the user would like to visit from the orignal users_movie
            second_movie_chosen = input(f"\nHere are all the following recommended movies for {movie_chosen}: {related_films}. Which movie would you like to know more about: ")

            #ensures that the users input is a valid movie
            while second_movie_chosen not in related_films:
                second_movie_chosen = input("\nSorry that's not a valid movie; which movie would you like know more about: ")
            
            #returns the information associated with the chosen movie
            for movie in movie_chosen.edges.keys():
                if second_movie_chosen == movie.name:
                    print(f"\nNice pick! Heres the following details for {movie}: {movie_chosen.edges[movie]}")
                    second_movie_chosen = movie
            
            #asks the user if they want to continue their search
            users_input = continue_search()
            
            #calls find_similar_movies recursively
            find_other_movies(graph_name, users_input, second_movie_chosen)


#Continues the users search based on the input the user provides
def continue_search():
    #asks the user if they want to see other recommended movies
    users_other_recommendations_choice = input("\nWould you like to see other related movies or search for one? Please type (s) if you would like to search for another movie, (r) if you would like to see related movies, or (n) if you would like end your search: ")
            
    #ensures the users input is valid
    while (users_other_recommendations_choice != "s" and users_other_recommendations_choice != "r" and users_other_recommendations_choice != "n"):
        users_other_recommendations_choice = input("Sorry I didn't get that. Please type (s) if you would like to search for another movie, (r) if you would like to see realated movies, (n) if you would like end your search: ")
    
    return users_other_recommendations_choice

software_recommendation(movie_graph)