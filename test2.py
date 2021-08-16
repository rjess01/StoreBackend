from types import AsyncGeneratorType


class Student:
    
    def __init__(self, name, age):
        """
        Class constructor on Python
        """
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hi there!. My name is: " + self.name)


print("********* Test 2 *********")

student1 = Student("Jesse Ramos", 23)
student1.say_hello()

student2 = Student("Jesse Ramos", 23)
student2.say_hello()

print(student1.name)
student1.name = "Name Changed"
print(student1.name)

me = {
    "name" : "Jesse",
    "age" : 23
}

print(type(student1))
print(type(me))