fp = None
try:
    fp = open('bad_file.txt', 'r')
    if fp.name == 'bad_file.txt':
        raise Exception


except FileNotFoundError:
    print("Please give the correct file name")
except:
    print("Please give good file")
else:
    print(fp.read())

finally:
    if fp is not None:
        fp.close()
        print(fp.closed)
    print("End of the Program")


