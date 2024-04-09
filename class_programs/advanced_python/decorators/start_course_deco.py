print("start")


def courses(func):
    def wrapper_func(name, institute_name):
        print(f"Hi {name}")
        func()
        print("Interested people can contact us")
        print(f"\nRegards, \n{institute_name} Institute")
    return wrapper_func


@courses
def start_courses():
    print("We are starting with the following courses")
    print("Python, Java, Selenium, Testing")


start_courses('Sachin', 'Cranes')
print()


@courses
def start_course():
    print("We are going to start with the Python Course")


start_course("John", "Spider")

