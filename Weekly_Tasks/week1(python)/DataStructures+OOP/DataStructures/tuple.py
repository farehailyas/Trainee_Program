import sys
data = (1 ,2 ,3 ,4 ,5,6)
print(sys.getsizeof(data))
# adding elements (tuples are immutable, so we cannot add elements directly)
# we can create a new tuple by concatenating the existing tuple with a new tuple
data = data + (6,)     
print(data)
sliced_data = data[1:4:2]
print(sliced_data)

# unpack with sterick
first, *middle, secondLast ,last = data
print(first)
print(middle)
print(secondLast)
print(last)