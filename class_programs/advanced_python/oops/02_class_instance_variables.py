# class data [properties/ attributes] and behavior [Methods]

class Employee:
    raise_amount = 1.04
    no_of_employees = 0

    def __init__(self, f_name, l_name, eid, pay):
        self.f_name = f_name
        self.l_name = l_name
        self.eid = eid
        self.pay = pay
        Employee.no_of_employees += 1

    def display(self):
        print(self.f_name)
        print(self.l_name)
        print(self.eid)
        print(self.pay)

    def increase_salary(self):
        print(self.pay * self.raise_amount)


print(Employee.no_of_employees)
emp1 = Employee('Sachin', 'Joshi', 589, 50000)
emp2 = Employee('Jospeh', 'Jain', 345, 60000)
print(Employee.no_of_employees)
print(emp1.no_of_employees)
print(emp2.no_of_employees)
# emp1.increase_salary()
#
# emp2.increase_salary()

# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)
# print(Employee.__dict__)
# print(emp1.__dict__)
# print(emp2.__dict__)
#
# print("-- Increased the percentage of hike through the class --")
# Employee.raise_amount = 1.06
# print(Employee.raise_amount)  # 1.06
# print(emp1.raise_amount)  # 1.06
# print(emp2.raise_amount)  # 1.06
#
# print("-- Increased the percentage of hike through the emp1 --")
# emp1.raise_amount = 1.1
# print(Employee.raise_amount)  # 1.06
# print(emp1.raise_amount)  # 1.1
# print(emp2.raise_amount)  # 1.06
#
# print("-- Increased the percentage of hike through the class again --")
# Employee.raise_amount = 1.08
#
# print(Employee.raise_amount)  # 1.08
# print(emp1.raise_amount)  # 1.1
# print(emp2.raise_amount)  # 1.08
#
#
# print("-- Increased the percentage of hike through the emp2  --")
# emp2.raise_amount = 1.5
#
# print(Employee.raise_amount)  # 1.08
# print(emp1.raise_amount)  # 1.1
# print(emp2.raise_amount)  # 1.5
#
# print(Employee.__dict__)
# print(emp1.__dict__)
# print(emp2.__dict__)
