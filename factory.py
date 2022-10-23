from abc import ABCMeta, abstractclassmethod
from re import T
from secrets import choice

class IPerson(metaclass=ABCMeta):

    @abstractclassmethod
    def person_method():
        """ Interface Method """

class Student(IPerson):
    
    def __init__(self) -> None:
        self.name = "Basic student name"

    def person_method(self):
        print('I am a student')

class Teacher(IPerson):

    def __init__(self) -> None:
        self.name = "Basic teacher name"

    def person_method(self):
        print("I am a teacher")

class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        elif person_type == "Teacher":
            return Teacher()
        else:
            print("Invalid Type")
            return -1

if __name__ == "__main__":
    choice = input("What type of person do you want to create?\n ('Student' or 'Teacher')\n")
    person = PersonFactory.build_person(choice)
    person.person_method()