class GrandParent:
    print("I am in the GrandParent class")
    a = 5  # Public class variable
    _b = 6  # Protected class variable
    __c = 7  # Private class variable

    def __display(self):
        print(self.__c)


class Parent(GrandParent):
    print("I am in the Parent class")

    def display(self):
        print(self.__c)


class Child(Parent):
    print("I am in the Child class")

    # def display(self):
    #     print(self._GrandParent__c)


p = Parent()
# print(p._b)
p.display()
# c = Child()
# print(c._b)
# c.display()
# g = GrandParent()
# g.display()
# print(Parent._GrandParent__c)
# print(help(Child))
