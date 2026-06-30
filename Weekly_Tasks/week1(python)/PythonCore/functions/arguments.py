def func(*args):
    for arg in args:
        print(arg)
    
func("abc" , "def" ,"ghi" , "jkl")

def addition(*args):
    ans =sum(args)
    print(ans)

addition(3,4,5,6,6)

def mapValues(**kwargs):
    for k , val in kwargs.items():
        print(k , val)

mapValues( a = 2 ,b = 3 )