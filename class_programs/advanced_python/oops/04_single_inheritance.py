class Employee:
    raise_amount = 1.04  # 4% raise

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        print("Employee created: ", self.first_name, self.last_name)

    def display(self):
        print("Employee display")
        print(f"Name: {self.first_name} {self.last_name}, Salary: {self.salary}")

    def increase_salary(self):
        self.salary *= self.raise_amount
        print(f"New salary after raise: {self.salary}")


class Developer(Employee):
    raise_amount = 1.10  # 10% raise for developers

    def __init__(self, first_name, last_name, salary, prog_lang):
        super().__init__(first_name, last_name, salary)

        self.prog_lang = prog_lang
        print("Developer specialty: ", self.prog_lang)

    def display(self):
        print("Developer display")
        print(f"Name: {self.first_name} {self.last_name}, Salary: {self.salary}")
        print("Programming Language 1: ", self.prog_lang)


# Test the classes with an example

dev1 = Employee('Sachin', 'Joshi', 50000,)
# dev2 = Developer('Jospeh', 'Jain', 345, 60000, 'Java')
dev1.display()
# print(help(Developer))

