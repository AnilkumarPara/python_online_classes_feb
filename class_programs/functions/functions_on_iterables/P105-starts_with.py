file_names = ['movies.txt', 'Movies.txt', 'movie.txt', 'Movie.txt', 'flowers.txt', 'fruits.txt', 'flower.txt']
prefixes = ('movies', 'movie', 'Movies', 'Movie')
for file_name in file_names:
    if file_name.startswith(prefixes):
        print(file_name)
