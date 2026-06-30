from functools import reduce
from operator import add
from itertools import accumulate

# calculate final price after applying discount on each product

disc = [0.4 , 0.5 , 0.8]
price = 100 

accumulated_discount = reduce(lambda x, y : x*y , disc)

total = accumulated_discount * price
print(total)

lis = [1 , 2 , 3 ,4 , 5 , 6]
# find the larget number in a list using reduce
large = reduce(lambda x,y : max(x,y) ,lis )
print(large)

# accumulate return intermediate results as well
ans = accumulate(lis, add)
print(list(ans))

