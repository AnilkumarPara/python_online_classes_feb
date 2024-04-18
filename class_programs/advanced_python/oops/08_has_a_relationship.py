# Define the Engine class
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return "Engine starting with horsepower of " + str(self.horsepower)

# Define the Car class that has an Engine
class Car:
    def __init__(self, model, engine_horsepower):
        self.model = model
        self.engine = Engine(engine_horsepower)  # Composition relationship

    def start(self):
        return f"{self.model} car's engine starts: {self.engine.start()}"

# Create an instance of Car with an Engine
my_car = Car("Toyota Camry", 268)
print(my_car.start())
