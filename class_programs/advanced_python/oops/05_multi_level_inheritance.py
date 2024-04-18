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


class SeniorDeveloper(Developer):
    def __init__(self, f_name, l_name, eid, pay, prog_lang1, prog_lang2):
        super().__init__(f_name, l_name, eid, pay, prog_lang1)
        self.prog_lang2 = prog_lang2

    def helping_team(self):
        print("Helping team members to solve the issues")
        print(Employee.raise_amount)


sdev1 = SeniorDeveloper('Sachin', 'Joshi', 589, 50000, 'Python', 'C#')
# sdev2 = SeniorDeveloper('Jospeh', 'Jain', 345, 60000, 'Java', 'Go')
print(sdev1.prog_lang2)
print(sdev1.prog_lang1)
print(sdev1.eid)
sdev1.helping_team()
sdev1.display()

# print(help(SeniorDeveloper))
