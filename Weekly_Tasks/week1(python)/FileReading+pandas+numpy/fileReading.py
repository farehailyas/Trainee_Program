# using with statement (reads file as whole , and closes automatically)

# with open("sample.txt" , "r") as textFile:
#     data = textFile.read()
# print(data)


# # handling exception
# try:
#     with open("file.txt" , "r") as fil:
#         data = fil.read()
#     print(data)
# except FileNotFoundError as e:
#     print("File not found")

# reading line by line
# textFile = open("sample.txt" , "r")
# for line in textFile:
#     print(line.strip())
# textFile.close()   

# # 
# textFile = open("sample.txt" , "r")
# data = textFile.readline()
# while data:
#     print(data)
#     data = textFile.readline()
# textFile.close()

# # writing to a file
# with open("sample.txt" , "a") as file:
#     file.write("New Data")

# newFile = open("sample.txt")
# data = newFile.readline()
# while data:
#     print(data)
#     data = newFile.readline()    

#     # reading a csv file

# import csv
# with open("customers-100.csv", "r") as file:
#     data = csv.reader(file)
#     for row in data:
#         print(row[9])

# with open("customers-100.csv", "r") as file:
#     data = csv.DictReader(file)
#     for row in data :
#         print(row["First Name"])

# import json
# # json file
# with open("sample1.json", "r") as file:
#     data = json.load(file)
#     print(data)


# copy a file into another file 
open("copiedFile.txt" , "w").write(open("sample.txt" ,"r").read())
with open("copiedFile.txt" , "r") as file:
    result = file.read()
    print(result)

# using shutil
import shutil
shutil.copy("sample.txt" , "dest.txt")