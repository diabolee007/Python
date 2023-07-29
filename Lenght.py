print(len(input('What is your name?')))

print('Welcome to the Band Generator.')
street = input("What's the name of the city you grew up in?\n")
food = input("What's your favorite food?\n")
print("Your band name could be " + street + " "+ food)

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
weight_results = int(weight)
height_results = float(height)**2
print(int(weight_results/height_results))
               
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#calculates how long it will be before you turn 90
#Write your code below this line 👇
days = int(age) * 365
n1 = 90 * 365 
days1 = n1 - days
days_results =  str(days1)
weeks = int(age) * 52
n2 = 90 * 52
weeks2 = n2 - weeks
weeks_results = str(weeks2)
months = int(age) * 12
n3 = 90 * 12
months2 = n3 - months
months_results = str(months2)

print("you have " + days_results +" days, " + weeks_results +
      " weeks, and " + months_results + " months left.")
