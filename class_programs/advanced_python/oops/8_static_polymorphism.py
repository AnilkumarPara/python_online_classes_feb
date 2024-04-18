class add_class:
    a = 5
    a = 6
    a = 7

    def add(self, a, b):
        print(a+b)

    def add(self, a, b, c):
        print(a + b +c)

    def add(self, a, b, c, d):
        print(a + b +c + d)


    # def add(self, *args):
    #     addition = 0
    #     for n in args:
    #         addition += n
    #     print(addition)

# ac = add_class()
# ac.add(2, 3)
# ac.add(2, 3, 4)
print(help(add_class))
