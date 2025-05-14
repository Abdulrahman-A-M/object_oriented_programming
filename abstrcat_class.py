from abc import ABC,abstractmethod

class Animal(ABC):
    def move(self):
        pass


class Human(Animal):
    def move(self):
        print('I can walk and run')

class Snake(Animal):
    def move(self):
        print('I can crawl')



class Dog(Animal):
    def move(self):
        print('I can bark')



class Lion(Animal):
    def move(self):
        print('I can roar')

S=Snake()
S.move()


D=Dog()
D.move()

L =Lion()
L.move()


#EXAMPLE 2
# no need to explicitly call abc
print('*'*50)
class parent:
    def geeks(self):
        pass

class child(parent):
    def geeks(self):
        print('child class')


R = child()
R.geeks()

print('*'*50)
# example 3
# use super() to call properties or function
class R(ABC):
    def rk(self):
        print('Abstract Base Class')

class K(R):
    def rk(self):
        super().rk()
        print('subclass')

r=K()
r.rk()

