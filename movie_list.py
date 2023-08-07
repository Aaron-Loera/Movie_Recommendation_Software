#imports the MovieVertex class from the movie_vertex file and MovieGraph from the movie_graph file
from movie_vertex import MovieVertex


#a list of all movie objects
movie_list = []


#Creating objects to represnt all the movies for the recommendation software, adding them to the list, and adding them to related films
iron_man = MovieVertex("Iron Man", "Superhero", 4.5, "The newly found hero Iron Man fights against his ex-mentor!")
movie_list.append(iron_man)

iron_man2 = MovieVertex("Iron Man 2", "Superhero", 4, "Iron Man returns as he has to face the consequences of his past.")
movie_list.append(iron_man2)
iron_man2.add_related_movies(iron_man)
iron_man.add_related_movies(iron_man2)

spider_man = MovieVertex("Spider-Man", "Superhero", 4.5, "A teenager gain incredible powers when he gets bit by a spider.")
movie_list.append(spider_man)

spider_man2 = MovieVertex("Spider-Man 2", "Superhero", 5, "Spider-Man fights his turned evil mentro Dock Ock!")
movie_list.append(spider_man2)
spider_man.add_related_movies(spider_man2)
spider_man2.add_related_movies(spider_man)

prisoners = MovieVertex("Prisoners", "Suspense", 5, "Two fathers desperatley search for their missing children.")
movie_list.append(prisoners)

arrival = MovieVertex("Arrival", "Suspense", 3.5, "A professor is needed for her translating skills when aliens arive to earth.")
movie_list.append(arrival)

nope = MovieVertex("NOPE", "Suspense", 5, "Two cowboy siblings attempt to unravel the mystery of an alien spaceship in their town.")
movie_list.append(nope)
nope.add_related_movies(arrival)
arrival.add_related_movies(nope)

baby_driver = MovieVertex("Baby Driver", "Action", 4.5, "A young merc is dragged into the world of bank robberies, car chases, and gun fights.")
movie_list.append(baby_driver)

john_wick = MovieVertex("John Wick", "Action", 4, "A retired hitman goes back into the world of violence to avenge his dog.")
movie_list.append(john_wick)

john_wick2 = MovieVertex("John Wick 2", "Action", 3, "John Wick returns when a previous contractor blackmails him into doing his bidding.")
movie_list.append(john_wick2)
john_wick2.add_related_movies(john_wick)
john_wick.add_related_movies(john_wick2)

john_wick3 = MovieVertex("John Wick 3", "Action", 5, "John Wick is injured, alone, and desperate as he fights of the high table.")
movie_list.append(john_wick3)
john_wick3.add_related_movies(john_wick2)
john_wick3.add_related_movies(john_wick)
john_wick2.add_related_movies(john_wick3)
john_wick.add_related_movies(john_wick3)

smile = MovieVertex("Smile", "Horror", 3, "A therpaist gets passed a cures that causes her to spiral into delusions and insanity.")
movie_list.append(smile)

the_conjuring = MovieVertex("The Conjuring", "Horror", 4, "Two paranormal hunters try to solve the mystery of a demons presence in a clients home.")
movie_list.append(the_conjuring)
smile.add_related_movies(the_conjuring)
the_conjuring.add_related_movies(smile)

jigsaw = MovieVertex("Jig-Saw", "Horror", 2.5, "A group of stangers try to escape a maze of horrible torture and suffering.")
movie_list.append(jigsaw)

the_hangover = MovieVertex("The Hangover", "Comedy", 4.5, "3 friends look for their missing 4th member after a late night party in Las Vegas.")
movie_list.append(the_hangover)

the_hitmans_bodyguard = MovieVertex("The Hitman's Bodyguard", "Comedy", 4, "An uptight bodyguard is forced to protect a unique natured hitman.")
movie_list.append(the_hitmans_bodyguard)

the_hitmans_bodyguard2 = MovieVertex("The Hitman's Bodyguard 2", "Comedy", 3, "Our favorite bodyguard returns to save our previous hitman's wife.")
movie_list.append(the_hitmans_bodyguard2)
the_hitmans_bodyguard2.add_related_movies(the_hitmans_bodyguard)
the_hitmans_bodyguard.add_related_movies(the_hitmans_bodyguard2)


#adds all the movies in movie_list to the graph
for movie in movie_list
