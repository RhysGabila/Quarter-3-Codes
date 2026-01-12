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

5.) Write a Reflection (3–5 sentences):

Why did you choose this dataset?
-I chose this dataset because I am already familiar with it due to examples shown in class before.
I was able to easily modify it because I was already familiar on how to layout the dataset.
I also found it the easiest to layout the data from this dataset.

How does a 2D array help organize and work with this kind of data?
-A 2D array or really a multidimensional array is a list of lists.
What this means is that we are able to sort and easily organize the data from our dataset into a list, except the data we will 
organize in the list, is also a list. A 2D array also makes it convenient to summarize, add or remove elements, and so much more to the list.
