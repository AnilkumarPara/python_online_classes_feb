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


class TeamLead(Employee):
    raise_amount = 1.3

    def leading_team(self):
        print("lead the team")


class DevLead(TeamLead, Developer):
    def leading_team(self):
        print("lead the development team")

class Manager:
    pass

dlead1 = DevLead('Anil', 'Para', 389, 50000, 'Python')

# print(dlead1.raise_amount)
print(dlead1.__dict__)

print(isinstance(dlead1, Manager))
print(issubclass(TeamLead, Developer))
