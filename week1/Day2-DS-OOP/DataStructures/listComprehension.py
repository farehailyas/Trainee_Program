# normally adding elements in list
 # 1. looks up 'append' on list object
                # 2. calls function
                # 3. checks capacity
                # 4. change to int 
                # 5. stores value
import time
start = time.time()
list1 = []
# n = int(input())
n = 10000000
# elements = input().split()
for i in range(n):
    list1.append(i)
end = time.time()
print(end - start)
# print(list1)

# using list comprehension
# CPython uses LIST_APPEND bytecode internally
# direct C-level operation — no Python function call
start = time.time()
list2 = [i for i in range(n) ]
end = time.time()
print(end - start)
# print (list2)