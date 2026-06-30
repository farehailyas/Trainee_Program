
"""Part B"""

# writing in a file
records = [ ("fareha" , 89) , ("Ali" , 67) , ("Ahmad" , 73) , ("Hamza" , 54) , ("Sara" ,62)]

with open ("students.txt" , "w") as file:
    for name , score in records: 
        file.write(f"{name} {score}")
        file.write('\n')

print("Record inserted")


# appending
try:
    with open ("students.txt", "a") as file:
        file.write("Hassan 34\n")
except FileNotFoundError:
    print("Cannot find the file.")

# reading in a file
try:
    with open ("students.txt", "r") as file:
        for i in file:
            print(i , end = "")
except FileNotFoundError:
    print("Cannot find the file.")


