import matplotlib.pyplot as plt

x = [1 ,2 ,3 ,4 ,5 ,6,7]
y = [2,4,6,8,10,12 , 12]

# line chart 
# plt.plot(x,y)
# plt.show()

# subplots get axes only in subplots
# fig , ax = plt.subplots()
# ax.plot(x , y , marker = 'o' , label = "Data Points")
# ax.set_title("Visualizing data")
# ax.set_xlabel("x")
# ax.set_ylabel("y")
# plt.show()

# x = ["mon" , "tues" , "wed"]
y = [1 , 2 , 3]
# plt.bar(x,y)
# plt.title("days")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()


# histogram
x = [7, 8, 9, 10, 10, 12, 12, 12, 13, 14, 14, 15, 16, 16, 17, 18, 18, 19, 20, 20,
     21, 22]
y = [7, 8, 9, 10, 10, 12, 12, 12, 13, 14, 14, 15, 16, 16, 17, 18, 18, 19, 20, 20,
     21, 22]
# plt.hist(x)
# plt.show()

# # scatter plot
# plt.scatter(x , y)
# plt.show()

# pie chart
plt.pie(x , labels = y)
plt.show()

plt.boxplot(x)
plt.show()