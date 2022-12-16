
fd = open("input.txt", "r")
list_calories = fd.read().splitlines()

list_maximum_calories = []
list_top_3 = []
maximumCalories = 0
sumCalories = 0

for calory in list_calories:
    if calory != '': 
        sumCalories=+ sumCalories + int(calory)
        
    else:
        list_maximum_calories.append(sumCalories)
 
        if maximumCalories < sumCalories:
            maximumCalories = sumCalories
        sumCalories = 0


print(f"The elf tha eat the maximum number of calories is {maximumCalories}")

list_maximum_calories.sort(reverse=True)

for i in range(3):
    list_top_3.append(list_maximum_calories[i])



print(f"The top maximum calories is: {sum(list_top_3)}")
