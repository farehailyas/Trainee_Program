sets = {1.2, 2, 3, 4, 5}
print(type(sets))
print(sets)
sets.add(87)
sets.remove(5)
print(sets)

sets2 = {1, 2, 3, 4, 5}

union = sets.union(sets2)
print(union)
intersection = sets.intersection(sets2)
print(intersection)
sets2.clear()
print(sets2)