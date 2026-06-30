import numpy as np
# 1d
arr = np.array([1,2,3,4,5,6])

# 2d 

arr1 = np.array([[1,2,3,4,4] , [6,7,8,9 ,10] , [11,12,13,14 , 15]])
print(arr)
print(arr1)

# indexing
a1=  arr1[1,2]
print(f"element in 2 d array {a1}")

# slicing
sliced = arr1[ 0:2 , 2:4 ]
print(f"sliced array {sliced}")

a0 = np.zeros((2,3))
print(a0)

ar  = np.arange(0, 10, 2)
print(ar)
# advance indexing
# indexing based on some condition or collective one
index = [1,2,6]
arr = np.array([0,1,2,3,4,5,6,7,7,8])
print(arr[index])

# condition based
con = arr > 6
print(arr[con])

# arithmetic operations
x = np.array([2,3,4,5,6])
y = np.array([3,4,5,6,7])
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(f"data type {x.dtype}")
# np.absolute(x)
# np.add()
# np.pi
# np.exp()
# np.sqrt()

dtype = [('name', 'S10'), ('year', int), ('cgpa', float)]
vals  = [('Hrithik', 2009, 8.5),
         ('Ajay',    2008, 8.7),
         ('Pankaj',  2008, 7.9),
         ('Aakash',  2009, 9.0)]

data = np.array(vals , dtype = dtype)
print(np.sort(data , order = "name"))
print(np.sort(data , order = ["year" ,"cgpa"]))