import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.random.randint(50 , 200 ,(4,8))
print(sales)

# axis = 1 for , axis = 0 for row.
total = sales.sum(axis = 1)
print("Sales per product")
print(total)

weekly_sales = sales.mean(axis = 0)
print("weekly sales record")
print(weekly_sales)

highest_sold_product = np.argmax(total)
print(f"Highest total index {highest_sold_product}")

df = pd.DataFrame(sales , columns=[ f"Week{i}" for i in range(1 , 9)],
                  index=['Product A', 'Product B', 'Product C', 'Product D'])

df["Total"] = total
print(df.head())

filtered_records = df[df['Total'] > 900]
print("filtered records")
print(filtered_records)

filtered_records.to_csv("sales_report.csv")

fig , ax = plt.subplots(1 , 2 , figsize = (12, 12))

weeks = np.arange(1, 9)
print(weeks)
products = ['Product A', 'Product B', 'Product C', 'Product D']

for i, product in enumerate(products):
    ax[0].plot(weeks, sales[i], marker='o', label=product)

ax[0].set_xlabel('Week')
ax[0].set_ylabel('Sales')
ax[0].set_title('Weekly Sales per Product')
ax[0].legend()
ax[0].grid()

ax[1].bar(products , total)
ax[1].set_xlabel('Product')
ax[1].set_ylabel('Total Sales')
ax[1].set_title('Total Sales per Product')
ax[1].legend(['Total Sales'])
ax[1].grid(axis='y')
plt.show()
