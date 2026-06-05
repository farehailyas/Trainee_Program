num = list(map(int , input().split()))
# num = map(int , num)
print(num)
# convert each element in the list to int

# ifwe need one value at a time , loop give all at once.
num = map(int, input().split())  # lazy rahega
next(num)


# apply user defined function to each element in iterable
def double_elements(x):
    return 2*x
num
arr = list(map(double_elements , num))
print(arr)

# for more shorter and readable version of code use lambda function with map

arr =  list(map(lambda x: 3*x , num))
print(arr)

# when there are more than one iterable to pass in map
# to add corresponding elements in two list
a = [1 , 2 , 3]
b = [4 , 5 , 6]
arr = list(map(lambda x,y : x+y , a , b ))
print(arr)

# conert string to uppercase
st = ["apple" ,"mango" ,"banana"]
upper_case_str = list(map(str.upper , st))
print(upper_case_str)

# extract the first character from the string
first_char = list(map(lambda s: s[0] , st))
print(first_char)

# removing whitespace from the string
st = [" app " , " ki " , " kjh   "]
remove_spaces = list(map( str.strip , st))
print(remove_spaces)

