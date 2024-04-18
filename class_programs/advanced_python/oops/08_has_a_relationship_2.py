class Anil:
    bike = 1

    def riding_a_bike(self):
        print(f"Riding {self.bike} Bike")


class Sunil:
    car = 1
    a = Anil()

    def riding_a_car(self):
        print(f"Riding {self.car} Car")


s = Sunil()
s.a.riding_a_bike()

