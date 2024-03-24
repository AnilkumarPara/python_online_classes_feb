file_names = ['image1.png', 'image2.PNG', 'image3.jpg', 'Movie.txt', 'image4.jpeg', 'flower.gif', 'fruits.txt',
              'image5.svg']
suffixes = ('.png', '.jpeg', '.jpg')
for file_name in file_names:
    if file_name.endswith(suffixes):
        print(file_name)
