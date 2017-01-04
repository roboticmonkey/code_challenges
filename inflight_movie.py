def inflight_movies(movie_lengths, flight_length):

    # longer_movies = []
    # shorter_movies = []

    # for movie in movie_lengths:
    #     if movie < (flight_length/2):
    #         shorter_movies.append(movie)
    #     else:
    #         longer_movies.append(movie)

    # for movie in shorter_movies:

    #     for show in longer_movies:
    #         if movie + show <= flight_length:
    #             return True


    # # return a boolean T/F if there are 2 movies whose sum = flight_length
    # return False

    movie_seen = set()

    for movie in movie_lengths:
        
        second_movie = flight_length - movie
        if second_movie in movie_seen:
            return True

        movie_seen.add(movie)
    return False

movies = [60, 70, 80, 92, 120, 65]
flight = 200
# movies = [60, 70, 80, 92, 120, 65]
# flight = 120

print inflight_movies(movies, flight)