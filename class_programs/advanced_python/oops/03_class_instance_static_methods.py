class Employee:
    raise_amount = 1.04

    def __init__(self, f_name, l_name, eid, pay):
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

    @staticmethod
    def is_working_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee('Sachin', 'Joshi', 589, 50000)
emp2 = Employee('Jospeh', 'Jain', 345, 60000)

import datetime

d = datetime.date(2024, 4, 12)
print(Employee.is_working_day(d))
