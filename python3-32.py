# Multiple Inheritance

# Inherit from multiple classes at the same time

# ★★★ 
# 1. Python 允许继承多个类，继承顺序matters。当这些父类（Vehical类和Freezer类）拥有相同的方法（display()），Python 默认调用第一个继承的类中的该方法（见位置【1】），否则需要分别调用（见位置【4】）。

# 2. 子类中如果也有相同名字的方法，那么父类中的该方法会被子类override，优先调用子类中的该方法（见位置【3】）
# ★★★ 

# Vehical class
class Vehical:
    speed = 0
    def drive(self, speed):
        self.speed = speed
        print('Driving')
    
    def stop(self):
        self.speed = 0
        print('Stopped')
    
    def display(self):
        print(f'Deriving at {self.speed} speed')

# Freezer class
class Freezer:
    temp = 0
    def freeze(self, temp):
        self.temp = temp
        print('Freezing')
    
    def display(self):
        print(f'Freezing at {self.temp} temp')

# FreezerTruck class
class FreezerTruck(Vehical, Freezer): # 【2】 Here we define the Method Resolution Order(MRO)
    def display(self): # 【3】
        print(f'It is a freezer: {issubclass(FreezerTruck, Freezer)}')
        print(f'It is a vehical: {issubclass(FreezerTruck, Vehical)}')

        # super(Freezer,self).display() # Works because of MRO
        # super(Vehical,self).display() # Fails because of MRO
        # 【4】
        Freezer.display(self)
        Vehical.display(self)

t = FreezerTruck()
t.freeze(-30)
print('-'*20)
# 【1】这里调用的是Vehical类的display方法，因为继承顺序为Vehical、Freezer（见位置【2】）
t.display()