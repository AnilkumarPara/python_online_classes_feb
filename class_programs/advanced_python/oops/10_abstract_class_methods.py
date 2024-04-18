from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    def leave_calendar(self):
        print("15 casual and 7 sick leaves per year")
        print("12 company holiday per year")

    @abstractmethod
    def salary_scale(self):
        pass

    @abstractmethod
    def performance_management(self):
        pass


class TestEngineer(Employee):
    print("I am in the TestEngineer class")

    # def salary_scale(self):
    #     print("Test engineer will have the salary scale of 3 to 8 lacs")

    def performance_management(self):
        print("Test Engineers Performance management will be done by the test lead")

    @abstractmethod
    def use_case_writing(self):
        pass

class JuniorTestEngineer(TestEngineer):
    print("I am in the JuniorTestEngineer class")

    def salary_scale(self):
        print("Test engineer will have the salary scale of 3 to 6 lacs")

    def use_case_writing(self):
        print("Write 5 uses cases per day")


class SeniorTestEngineer(TestEngineer):
    print("I am in the SeniorTestEngineer class")

    def salary_scale(self):
        print("Test engineer will have the salary scale of 6 to 8 lacs")

    def use_case_writing(self):
        print("Write 8 uses cases per day")

jte = JuniorTestEngineer('Anil')
jte.performance_management()
jte.leave_calendar()
jte.salary_scale()
jte.use_case_writing()


print()

ste = SeniorTestEngineer('Anil')
ste.performance_management()
ste.leave_calendar()
ste.salary_scale()
ste.use_case_writing()
# te.leave_calendar()
# te.salary_scale()
# te.performance_management()

class TestLead(Employee):
    print("I am in the TestLead class")

    def salary_scale(self):
        print("Test Lead will have the salary scale of 9 to 20 lacs")


