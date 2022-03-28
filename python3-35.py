# Decorators

# Decorator explanation from StackOverflow
# https://stackoverflow.com/questions/739654/how-to-make-function-decorators-and-chain-them-together/1594484#1594484

# Everything in python is an object
# That means functions can be used as objects
# So we can do some really cool things
# A decorator takes in a function, adds some functionality and returns it.

# Basic decorator
# In this example we will change the execution order
# from os import device_encoding

from os import name


def test_decorator(func):
    print('before')
    func()
    print('after')

@test_decorator
def do_stuff():
    print('Doing stuff')

# Real decorator
# In this example we will change the functionality
# @makeBold is equal to 
# f = makeBold(printName)
# and then call this function f()
def makeBold(func):
    def inner():
        print('<b>')
        func()
        print('</b>')
    return inner # Return the inner function

@makeBold
def printName():
    print('Bryan Cairns')

printName()

# Decorator with params
# Notice this has a defined number of params
def numcheck(func):
    def checkInt(o):
        if isinstance(o, int):
            if o == 0:
                print('Can not divide by zero')
                return False
            return True
        print(f'{o} is not a number')
        return False

    def inner(x,y):
        if not checkInt(x) or not checkInt(y):
            return 
        return func(x,y)
    return inner

@numcheck
def divide(a,b):
    print(a/b)

divide(100,3)
divide(100,0)
divide(100,'cat')

# Decorator with unkonwn number of params
# We want a decorator that can pass params and handle anything
# We also want to chain them together
# *args, **kwargs to the rescue

def outline(func):
    def inner(*args, **kwargs):
        print('-'*20)
        func(*args, **kwargs)
        print('-'*20)
    return inner

def list_items(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        print(f'args = {args}')
        print(f'kwargs = {kwargs}')
        for x in args:
            print(f'arg = {x}')
        for k,v in kwargs.items():
            print(f'key = {k}, value = {v}')
    return inner

# The order you set the decorators MATTERS
@outline
@list_items
def display(msg):
    print(msg)

# ★★★
# 注意这里加上关键字和不加关键字的区别

# 【1】加上关键字
# output：
# --------------------
# hello world
# args = ()
# kwargs = {'msg': 'hello world'}
# key = msg, value = hello world
# --------------------
display(msg = 'hello world')

# 【2】不加关键字
# output：
# --------------------
# hello world
# args = ('hello world',)
# kwargs = {}
# arg = hello world
# --------------------
display('hello world')

@outline
@list_items
def birthday(name = '', age = 0):
    print(f'Happy birthday {name} you are {age} years old')

# 效果同【1】【2】
birthday(name = 'Bryan', age = 46)
birthday('Bryan', 46)