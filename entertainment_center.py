import media
import fresh_tomatoes

# Create first movie with desired parameters
good_will_hunting = media.Movie("Good Will Hunting",
                                "An adult who meets a therapist and "
                                "changes his life",
                                "https://upload.wikimedia.org/wikipedia"
                                "/en/b/b8/Good_Will_Hunting_theatrical"
                                "_poster.jpg",
                                "https://www.youtube.com/watch?v=QSMvyuEeIyw")

# Create second movie with desired parameters
indiana_jones_temple_of_doom = media.Movie("Indiana Jones and the "
                                           "Temple of Doom",
                                           "After arriving in India, Indiana "
                                           "Jones is asked by a desperate "
                                           "village to find a mystical stone.",
                                           "https://upload.wikimedia.org/wikipedia/en/1/10/Indiana_Jones_and_the_Temple_of_Doom_PosterB.jpg",  # NOQA
                                           "https://www.youtube.com/watch?v=Kp4fGyLnNTw")  # NOQA

# Create third movie with desired parameters
independence_day = media.Movie("Independence Day",
                               "Aliens attack the world on 7-4",
                               "https://upload.wikimedia.org/wikipedia/en/b/bb/Independence_day_movieposter.jpg",  # NOQA
                               "https://www.youtube.com/watch?v=kA2WzBi2grE")

# Place 3 movies in a list
movies = [good_will_hunting, indiana_jones_temple_of_doom, independence_day]

# Pass in list of movies to open_movies_page()
fresh_tomatoes.open_movies_page(movies)
