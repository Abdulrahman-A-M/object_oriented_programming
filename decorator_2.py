def escape_unicode(f):
    def wrap(*args,**kwargs):
        x=f(*args,**kwargs)
        return ascii(x)
    
    return wrap

@escape_unicode
def remove_spcial_char():
    return 'blomkÒ'

s=remove_spcial_char()
print(s)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# exmaple 2
class CallCount:
    def __init__(self,f):
        self.f=f
        self.count=0
    
    def __call__(self, *args, **kwds):
         self.count +=1
         
         return self.f(*args, **kwds)
@CallCount
def hello(name):
    print('Hello, {}'.format(name))


hello('Ann')
hello('Luke')
print(hello.count)


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#example 3 multi decorators

class Trace:
    def __init__(self):
        self.enabled=True
    
    def __call__(self,f):
        def wrap(*args,**kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args,**kwargs)
        return wrap
    
def escape_unicode(f):
    def wrap(*args,**kwargs):
        x =f(*args,**kwargs)
        return ascii(x)
    return wrap

tracer=Trace()
s=remove_spcial_char()
print(s)
tracer.enabled = False
ss=remove_spcial_char()
print(ss)


