'''The factory pattern is a creational design pattern used in software development to encapsulate the processes involved in creation of objects '''
'''The factory pattern is used when:
- class does not know what kind of object it must create on a user's request
- you want to build an extensible association between this creater class and casses corresponding to objects that it is supposed to create'''

class ShapeInterface:
    def draw(self):
        pass

class Circle(ShapeInterface):
    def draw(self):
        print("Circle draw")


class Square(ShapeInterface):
    def draw(self):
        print('Square draw')



class ShapeFactory:
    @staticmethod
    def getShape(type):
        if type == 'circle':
            return Circle()
        if type == 'square':
            return Square()
        assert 0, "Could not find shape "+type

#Another example of Factory Pattern
class Person:
    '''Base class Person has methods for getting the name and the gender and has two sub-classes namely Male and Female that print the greeting message and a Factory class'''
    def __init__(self):
        self.name = None
        self.gender = None

    def get_name(self):
        return self.name

    def getGender(self):
        return self.gender

class Male(Person):
    def __init__(self,name):
        print("Hello Mr. "+ name)

class Female(Person):
    def __init__(self,name):
        print('Hello Miss. '+ name)

class Factory:
    '''Factory class has a method named get_person that takes two argments name and gender of a person'''
    def get_person(self,name, gender):
        if gender == "M":
            return Male(name)
        if gender == "F":
            return Female(name)

#Usecase
if __name__ == '__main__' :
    factory = Factory()
    person = factory.get_person('Aleksandra', 'F')



