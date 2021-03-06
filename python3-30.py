# Introduction to classes

# OOP - Object Oriented Programming
# Blue prints for creating objects
# Classes are a big topic
# We will cover this over multiple videos 

# Create the class

# Import the class 
import cat
from cat import Cat

# Use the class
# here's no self in the brackets, cuz this is not in a Class and does not have a current object.
def test():
    b = Cat('Kitkat', 1, 'tabby')
    c = Cat('Othello', 6, 'black')
    print(b)
    print(c)

    b.description()
    c.description()

    c.meow()
    b.sleep()
    c.hungry()
    b.eat()

if __name__ == '__main__':
    x = Cat('test')
    print(x)
    test()
    
