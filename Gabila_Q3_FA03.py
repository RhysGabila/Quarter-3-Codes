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

3.) Write a Short Explanation (3 - 4 sentences):

How did using an array help you analyze the data more easily?
-Using an array helped me analyze the data more easily and efficiently due to me being able to see all of the data being layed out.
I was able to easily see any mistakes in the code/dataset itself.
I was also able summarize the dataset easily by using an array.

Which part of summarizing the data was easy or difficult?
-Overall, summarizing the data was really easy and I did not have difficulty in trying to summarize it. 
There was no particularly difficult part to summarize either.
I was able to finish the code easily.
