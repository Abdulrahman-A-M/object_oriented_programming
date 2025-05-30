#Decorator 1

class ErrorCheck:
    def __init__(self,function):
        self.function=function

    def __call__(self, *params):
        if any([isinstance(i,str) for i in params]):
            raise TypeError('input has string value')
        else:
            return self.function(*params)


@ErrorCheck
def add_nums(*nums):
    return sum(nums)


# this is like normal decorator 
#exmaple
""" 

add=ErrorCheck(add_nums)


print(add(1,2,3,4))

print(add(1,2,'a',4))

"""



print(add_nums(1,2,3,4))

print(add_nums(1,2,'a',4))

