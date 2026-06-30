name = input("Enter your name : ")
age = int(input("Enter your Age : "))
height = float(input("Enter your height (in cm) : "))

height_in_meters = age / 100

print(f"Hello {name}. You are {age} years old and {height_in_meters:.2f}m long")

# printing data types
print(f"Type of name : {type(name)}")
print(f"Type of age : {type(age)}")
print(f"Type of height : {type(height_in_meters)}")
