class Employee:
    raise_amount = 1.04

    def __init__(self, f_name, l_name, eid, pay):
        print("This is a Employee init")
        self.f_name = f_name
        self.l_name = l_name
        self.eid = eid
        self.pay = pay

    def display(self):
        print(self.f_name)
        print(self.l_name)
        print(self.eid)
        print(self.pay)

    def increase_salary(self):
        print(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount


class Developer(Employee):
    raise_amount = 1.1

    def __init__(self, f_name, l_name, eid, pay, prog_lang1):
        print("This is a Developer init")
        super().__init__(f_name, l_name, eid, pay)
        self.prog_lang1 = prog_lang1


class Manager(Employee):
    def __init__(self, f_name, l_name, eid, pay, employees=None):
        super().__init__(f_name, l_name, eid, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)


dev1 = Developer('Anil', 'Para', 389, 50000, 'Python')
dev2 = Developer('Joshi', 'Sachin', 388, 52000, 'Java')
dev3 = Developer('Dravid', 'Rahul', 390, 53000, 'C#')
mgr1 = Manager('Sunil', 'EK', 489, 7000, [dev1, dev2])
print(len(mgr1.employees))
mgr1.remove_employee(dev2)
print(len(mgr1.employees))
mgr1.add_employee(dev3)
print(len(mgr1.employees))
