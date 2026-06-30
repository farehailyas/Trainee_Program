def starts_a(st):
    return st[0] == 'a'

lis = ["abc" , "ayu" ,"tyu"]

result = list(filter(starts_a , lis))
print(result)

li = [1 , 2 , 3 , 4]
# check even numbers using filter
res = list(filter(lambda x : x%2 == 0 , li))
print(res)