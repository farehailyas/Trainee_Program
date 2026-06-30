from collections import deque
import heapq

"""part a"""
lis = deque(["task1" , "task2" , "task3"])
lis.append("task4")

for i in range(5):
    print(lis[0])
    lis.popleft()
    lis.append(f"task{8}")

from collections import Counter

lang = ["Python","Java","Python","C++","Python","Java","Go"]
count = Counter(lang)
print(count.most_common(2))

lis = [45, 92, 67, 88, 55, 76, 91, 33]
heapq.heapify(lis)
print(lis)
print(heapq.nlargest(3 , lis))