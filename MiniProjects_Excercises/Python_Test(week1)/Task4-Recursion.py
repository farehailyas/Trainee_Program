"""Part A recursion """

def flatten(lis):
    result = []
    if not isinstance(lis, list):
        return [lis]
    for i in lis:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
            
    return result

lis = [1, [2, [3, 4]], 5]
result = flatten(lis)
print(result)

"""Generator """

def countdown(n):
    i = n
    while i>0 :
        yield i
        i-=1
    yield "Blast Off!"

for i in countdown(5):
    print(i)