# The Cat class

# self is the first param
# It is equal to 'this' in other languages
# instance = created

class Cat:
    name = ''
    age = 0
    color = ''
    
    # __ 代表是python的内置函数 baked in 
    # self is the first parameter, it is a reference to the current object
    def __init__(self, name, age=0, color='white'):
        self.name = name
        self.age = age
        self.color = color
        print(f'Constructor for {self.name}')

    def meow(self):
        print(f'{self.name} meow')
    
    def sleep(self):
        print(f'{self.name} zzz')
    
    def hungry(self):
        for _ in range(5):
            self.meow()
    
    def eat(self):
        print(f'{self.name} nom nom nom')
    
    def description(self):
        print(f'{self.name} ia a {self.color} cat, who is {self.age} years old.')