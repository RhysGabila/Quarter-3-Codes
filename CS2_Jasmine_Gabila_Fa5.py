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

print("\n")
print("Average Steps Per Person: \n")
  
for i in range(len(names)):
    average = arr[i].mean()
    print(names[i], "Average:", int(average))
  

print("\n Highest Amount of Steps Per Person: \n")    
for i in range(len(names)):
    maximum = arr[i].max()
    print(names[i], "Highest:", int(maximum))
    
print("\n Lowest Amount of Steps Per Person: \n")    
for i in range(len(names)):
    min = arr[i].min()
    print(names[i], "Lowest:", int(min))
    
highest = arr.max()
lowest = arr.min()
difference = highest - lowest
print("\nThe Difference Between The Highest and Lowest Amount of Steps is:", difference)

print("\nSteps per Day: \n")
for j in range(len(days)):
    steps = arr[:, j]
    print(days[j], "Steps:", steps)

print("\nAverage per Day: \n")
for j in range(len(days)):
    avr = arr[:, j].mean()
    print(days[j], "Average:", avr)
    
print("\nTotal steps per day: \n")
dailys = []

for day in range(len(days)):
    total = 0
    for row in range(len(names)):
        total += arr[row][day]
    dailys.append(total)

for i in range(len(days)):
    print(days[i], "total steps:", dailys[i])

most_active = max(dailys)
best_day = days[dailys.index(most_active)]

print("\nThe Most Active Day is:", best_day)
