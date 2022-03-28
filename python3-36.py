# Iterators
# Making counting easy

# Iter Basics
# Lists, tuples, dictionaries, and sets are all iterable objects.
# They are iterable containers which you can get an iterator from.
people = ['Bryan', 'Tammy', 'Rango']
i = iter(people)
print(i)
print(next(i))
print(next(i))
print(next(i))
# print(next(i)) # StopIteration

# Iterable class
import random
class Lotto:
    def __init__(self) -> None:
        self._max = 5
    
    def __iter__(self):
        # The yield statement suspends function's execution 
        # and sends a value back to the caller, but retains enough
        # state to enable function to resume where it is left off
        for _ in range(self._max):
            yield random.randrange(0,100)
        
        # ★★★ 
        # The link below shows 'waht does the 'yield' keyword do'
        # https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do/231855#231855
    
    def setMax(self, value):
        self._max = value
    
print('-'*20)
lotto = Lotto()
lotto.setMax(10)
for x in lotto:
    print(x)
print('-'*20)