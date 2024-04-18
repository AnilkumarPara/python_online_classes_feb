class Employee:
    def __init__(self, f_name, l_name, eid):
        self.f_name = f_name
        self.l_name = l_name
        self.eid = eid

    def display(self):
        print(self.f_name)
        print(self.l_name)
        print(self.eid)


emp1 = Employee('Sachin', 'Joshi', 589)
emp2 = Employee('Jospeh', 'Jain', 345)
emp2.display()