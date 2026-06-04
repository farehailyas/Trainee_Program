from collections import deque
d = deque(["abc" ,"def" ,"ghi"])
# add elements to the right
d.append("fareha")
# add elements to the left
d.appendleft("nowehere")

#add multiple elements to the right
d.extend(["now" , "and" , "then"])
# add multiple elements to the left
d.extendleft(["before" ,"and" ,"after"])

# remove first occurence of specified element
d.remove("and")

# remove element from right end
d.pop()

# remove element from left
d.popleft()
d.reverse()
print(d)
