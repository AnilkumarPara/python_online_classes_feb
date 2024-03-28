"""
WAP to find a movie names starts with ‘G’ in the given list of movies
using  list comprehension
"""
movies = ("Star wars", "Gundamma katha", "Gadar", "Gadzilla", "Robo")
print([movie for movie in movies if movie.startswith('G')])
