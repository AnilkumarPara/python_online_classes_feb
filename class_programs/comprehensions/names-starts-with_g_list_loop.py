"""
WAP to find a movie names starts with 'G' in the given list of movies
using for loop
"""
movies = ("Star wars", "Gundamma katha", "Gadar", "Gadzilla", "Robo")
g_movies = []
for movie in movies:
    if movie.startswith('G'):
        g_movies.append(movie)

print(g_movies)
