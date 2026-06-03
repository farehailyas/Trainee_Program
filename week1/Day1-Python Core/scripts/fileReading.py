# using with statement (reads file as whole , and closes automatically)

with open("sample.txt" , "r") as textFile:
    data = textFile.read()
    print(data)

reading line by line
textFile = open("sample.txt" , "r")
for line in textFile:
    print(line.strip())
textFile.close()   

# 
textFile = open("sample.txt" , "r")
data = textFile.readline()
while data:
    print(data)
    data = textFile.readline()
textFile.close()