import string


class Person:
    def __init__(self, name: str,age: int,gender: str) -> None:
        self.__name: str = name
        self.__age: int = age
        self.__gender: str = gender

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        self.__name = value

    @staticmethod
    def myMethod():
        print('Person')

p1 = Person("Mike", 20, 'm')
print(p1.Name)
p1.Name = "JHONSON"
print(p1.Name)
Person.myMethod()