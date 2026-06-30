import sys
data = [1 , 2, 3, 4, 5]
print(sys.getsizeof(data))
# adding elements
data.append(6)
print(data)
# removing elements
data.remove(3)
print(data)
# accessing elements
print(data[0])  # first element
print(data[-1])  # last element
data.pop(4)  # removes the element at index 4
print(data)
# slicing
print(data[1:4])
print(data[:3])
print(data[2:5])
# length of the list
print(len(data))
data2 = tuple(data)  # converting list to tuple
print(data2)
data2[0] = 11
# print(data2)  # this will raise an error because tuples are immutable