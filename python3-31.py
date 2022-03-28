# Class inheritance

# ★★★ 
# 实例化子类的时候，如果子类有自己的构造函数，那么子类的构造函数会被调用而不会调用父类的构造函数，例如，Tiger类中的init,所以，除非没有办法，尽量不要override父类的构造函数
# ★★★ 

# Feline class
class Feline:
    def __init__(self, name) :
        self.name = name
        print('Creating a feline')
    
    def meow(self):
        print(f'{self.name}: meow')
    
    def setName(self, name):
        print(f'{self} setting name: {name}')
        self.name = name

# Lion class
class Lion(Feline):
    def roar(self):
        print(f'{self.name} roar')

# Tiger class
class Tiger(Feline):
    # Override the constructor is a BAD idea
    def __init__(self):
        # Super alows is to access the parent
        # if we forget this we will have a bad time later
        super().__init__('Non Name')
        print('Creating a tiger')
    
    def stalk(self):
        # have to make sure name is set in the parent
        # this is considered -LBYL (look before you leap)
        # here we are dynamically adding the attribute

        # if we did not init the supper we will have to be careful
        # if not hasatter(self, 'name'): super().setName('No Name')
        print(f'{self.name}: stalking')
    
    def rename(self, name):
        super().setName(name)
        

c = Feline('kitty')
print(c)
c.meow()

l = Lion('Leo')
print(l)
l.meow()
l.roar()

t = Tiger() # is a Feline, but with a different constructor
print(t)
t.stalk()
t.rename('Tony')
t.meow()
t.stalk()