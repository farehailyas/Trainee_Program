"""Task A List """ 
def top_three(scores):
    # make unique
    s = set(scores)
    sort = sorted(s , reverse = True)
    return sort[:3]

scores = [12 , 13 , 14 , 15 , 16 , 17, 12 , 12 , 12]
print(top_three(scores))

"""Task B Tuple """
from collections import namedtuple

Student = namedtuple('Student', 'name age grades')
s1 = Student("fareha" , 23 , "A")
s2 = Student("Ali" , 23 , "B")
# s1.name = "abc" #will give error
print(s1)
print(s2)

"""Task C """

lis1 = ["abc" , "def" , "hello" , "lmn"]
lis2 = ["abc" , "567" , "8910" , "163"]

s1 = set(lis1)
s2 = set(lis2)

# words in both
print(s1.intersection(s2))

# words only in first
print(s1-s2)
# all unique words combined

print(s1.union(s2))

"""Task D """
from collections import Counter
def word_frequency(text):
    count = Counter(text)
    print(count)
word_frequency(["lis" ,"jbh" , "jbh" , "jbh" ,"fr" , "fr" ])

"""Task E """
# using loop
# result = []
# for i in range(1,21):
#     for j in range (i, 21):
#         for k in range (j , 21):
#             if (i*i) + (j*j) == (k*k):
#                 result.append( (i , j , k) )
#             elif (i*i) + (k*k) == (j*j):
#                 result.append( (i , j , k) )
#             elif (k*k) + (j*j) == (i*i):
#                 result.append( (i , j , k) )

""" using list comprehension """
# expression loops condition
result = [ (i , j , k) for i in range(1,21) for j in range(i , 21 )  for k in range (j , 21) if (i*i) + (j*j) == (k*k) ]
for i in result:
    print(f"valid points {i}")


"""Task F """
import array as arr
a = arr.array( 'i',[2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
for i in range(len(a)):
    a[i] *= 2
print(a)