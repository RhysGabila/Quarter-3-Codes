import numpy as np
names = ["My    ", "Reyven", "Frio  "]
days = ["Monday   ", "Tuesday  ", "Wednesday", "Thursday ", "Friday   "]
arr = np.array([
    [9800, 6700, 8900, 7400, 9600], #My steps
    [5100, 8200, 6900, 5800, 9100], #Reyven's steps
    [7600, 8400, 6000, 5300, 7200]  #Frio's steps
])
print("The Daily Step Counts from Monday to Friday: \n")

for i in range(len(names)):
    print(names[i], ":", arr[i])

print("\nTotal Steps per Day: \n")
for j in range(len(days)):
    total = arr[:, j].sum()
    print(days[j], "total:", total)

print("\n")
print("Average Steps Per Person: \n")
  
for i in range(len(names)):
    average = arr[i].mean()
    print(names[i], "Average:", int(average))
  

print("\n Highest Amount of Steps Per Person: \n")    
for i in range(len(names)):
    max = arr[i].max()
    print(names[i], "Highest:", int(max))
    
print("\n Lowest Amount of Steps Per Person: \n")    
for i in range(len(names)):
    min = arr[i].min()
    print(names[i], "Lowest:", int(min))

total_per_person = np.sum(arr, axis=1)
print("\n Total Amount of Steps Per Person: \n")
for i in range(len(names)):
    tot = arr[i].sum()
    print(names[i], "Total:", int(tot))

How did using an array help you analyze the data more easily?
-Using an array helped me analyze the data more easily and efficiently by it being sorted already. The array provides an organized and more compact way of storing the data. It is also easily accessible and easy to add, subtract, or duplicate it.

  Which part of summarizing the data was easy or difficult?
-No part of summarizing the data was particularly easy nor difficult. Everything provided me a challenge but was still pretty easy nontheless. I was able to accomplish everything properly.
