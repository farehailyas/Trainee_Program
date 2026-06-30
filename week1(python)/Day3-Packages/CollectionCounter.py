from collections import Counter
lis = ["abc" , 1 , 36 , "def" ,  1 ,"abc"]
count_lis = Counter(lis)
print(count_lis)

dic = {
    "abc": 1,
    "def" : 2,
    "ghi" :3
}
count_dic = Counter(dic)
print(count_dic)

tup = (1 ,2 ,3 ,4 ,5,6)
count_tuple = Counter(tup)
print(count_tuple[1])

# update counter value
count_tuple.update([2 , 3])
print(count_tuple)

# can perform arithmetic operations on count
from collections import Counter
ctr1 = Counter(["abc", "def", "def", "ghi"])
ctr2 = Counter(["def", "ghi", "ghi"])

print(ctr1 + ctr2)   # Addition
print(ctr1 - ctr2)   # Subtraction 
print(ctr1 & ctr2)   # Intersection
print(ctr1 | ctr2)   # Union