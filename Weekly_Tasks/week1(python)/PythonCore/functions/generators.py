def fun():
    yield 1
    yield 2
    yield 3

for i in fun():
    print(i)

# generator expression method
generator =  (x*x for x in range(1, 6))
for i in generator:
    print(i)