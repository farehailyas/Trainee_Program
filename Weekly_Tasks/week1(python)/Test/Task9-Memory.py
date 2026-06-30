"""Part B """
# STACK (immutable)
x = 5
print(f"x = 5, id: {id(x)}")
x = 5  # Same value, same object same address in memory
print(f"x = 5 again, id: {id(x)}")
x = 6  # New value, NEW object , instead of modifying its address value in stack it will 
# create a new reference object in stack
print(f"x = 6, id: {id(x)}\n")

# HEAP (Mutable)
lst = [1, 2, 3]
print(f"lst = [1,2,3], id: {id(lst)}")
lst.append(4)  # Same object, just modified so address remain same in stack , but values added in heap(mutable)
print(f"lst after append, id: {id(lst)}\n")
