def foo1():
    b='hello'
    
    def bar():
        
        c=True
        print(a)
        print(b)
        print(c)

    bar()

def foo2():
    a=200
    print(a)#only work in this function


if __name__=='__main__':
    a=100#globale viable
    # print(b)  # NameError: name 'b' is not defined
    print("*****local/golable variable *****")
    print("*** foo demo ***")
    foo1()
    print('***** foo2 *****')
    foo2()
    print(a)#from global


