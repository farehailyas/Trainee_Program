def assign_Grades(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "F"
    
n = int(input("Enter the number of subjects "))

marks = []
total_marks = n * 100
average = 0
obtained_marks = 0
percentage = 0

for i in range(n):
    mark = int(input(f"Enter marks for subject {i+1} "))
    marks.append(mark)
    obtained_marks += mark

average = (obtained_marks/n) 
percentage = (obtained_marks/total_marks) * 100

# output
print()
print("__Report Card__")
for i in range (n):
    grade = assign_Grades(marks[i])
    print ()
    print(f"Subject 1 : {marks[i]} {grade}")

print(f"Total : {obtained_marks} / {total_marks}")
print()
print(f"Average : {average}")
print()
print(f"Percentage {percentage}%")