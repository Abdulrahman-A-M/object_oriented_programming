import random
import numpy as np

def numberpower_generator():
    x = random.randint(0,10)
    yield x**2
    yield x**3
    yield 'Good after nighn'

x=numberpower_generator()
for i in x:
    print(i)

'''
Definition and Usage
The yield keyword is used to return a list of values from a function.

Unlike the return keyword which stops further execution of the function, the yield keyword continues to the end of the function.

When you call a function with yield keyword(s), the return value will be a list of values, one for each yield.'''
def numberpower_generator():
    x = random.randint(0,10)
    yield x**2
    yield x**3
    yield 'Good after nighn'
# only give first one
print(next(numberpower_generator()))

print('-'*22)
# infinit generator

def numberpower_generator():
    while True:
        x = random.randint(0,10)
        yield x**2
n=0
for i in numberpower_generator():
    print(i)
    n+=1
    if n ==10:
        break

print('-'*100)
print('-'*100)




"""
    yield pair of (X,Y) from data_x and data_y by generator
    """

def list_data_generator(batch_size,data_x,data_y,shuffle=True):
    data_lng=len(data_x)
    index_list=[*range(data_lng)]
    if shuffle:
        random.shuffle(index_list)
    
    index = 0
    while True: # infinit generator
        X = [0] * batch_size
        Y = [0] * batch_size
        print('do generator again')
        for i in range (batch_size):
            if index >= data_lng:
                index = 0
                if shuffle:
                        random.shuffle(index_list)
            X[i] = data_x[index_list[index]]
            Y[i] = data_y[index_list[index]]
            index +=1
            
            yield ((X,Y))
   

batch_size =10
data_x =[*range(5)]
data_y = [i *2 for i in data_x]

generator = list_data_generator(batch_size, data_x, data_y, shuffle=True)
#next(generator)
next(generator)
n=0
for i in generator:
    print(i)
    n+=1
    if n==10:
        break

