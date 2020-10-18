import random 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

random.seed(1)
values = []
sales = []
for item in range(1, 51):
    for store in range(1, 11):
        sales.append([item, store, random.randint(500, 1000)])  
        values.append([item, store, 1000])  

data = pd.DataFrame(np.array(values), columns=['item', 'store', 'inventory'])
data.to_csv("inventory.csv")

N = 5
inventory = [200, 350, 300, 350, 270]
sales = [250, 320, 340, 200, 250]

ind = np.arange(N) 
width = 0.35       
plt.bar(ind, sales, width, label='sales')
plt.bar(ind + width, inventory, width, label='inventory')

plt.ylabel('number of items')
plt.title('sales and inventory')

plt.xticks(ind + width / 2, ('item1', 'item2', 'item3', 'item4', 'item5'))
plt.legend(loc='best')
plt.show()

#====
plt.style.use('ggplot')

x = ['item1', 'item2', 'item3', 'item4', 'item5']
remaining_on_the_shelf = []
for i in range(0, 5): 
    remaining_on_the_shelf.append(inventory[i] - sales[i])
x_pos = [i for i, _ in enumerate(x)]


cc=['colors']*len(remaining_on_the_shelf)
for n,val in enumerate(remaining_on_the_shelf):
    print("val", val)
    if val<0:
        cc[n]='red'
    elif val>=0:
        cc[n]='blue'

plt.bar(x_pos, remaining_on_the_shelf, color=cc)
plt.xlabel("item")
plt.ylabel("number of items")
plt.legend(loc="upper right")

labels = ['lost demand', 'number of remaining items'] 
handles = [plt.Rectangle((0,0),1,1, color=cc[l]) for l in range(0, len(labels))]
plt.legend(handles, labels)



plt.xticks(x_pos, x)
plt.show()
