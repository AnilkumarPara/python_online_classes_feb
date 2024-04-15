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

    def __init__(self, f_name, l_name, eid, pay, prog_lang):
        print("This is a Developer init")
        super().__init__(f_name, l_name, eid, pay)
        # Employee.__init__(self, f_name, l_name, eid, pay)
        self.prog_lang = prog_lang


dev1 = Developer('Sachin', 'Joshi', 589, 50000, 'Python')
dev2 = Developer('Jospeh', 'Jain', 345, 60000, 'Java')
print(dev1.prog_lang)
print(dev1.f_name)
# print(help(Developer)