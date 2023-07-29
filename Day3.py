# Day 2
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
    print('Leap year.')
elif year % 100 == 0:
    print('Leap year.')
elif year % 400 == 0:
    print('Leap year.')
else:
    print('Not leap year')

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

    print(f"Your final bill is: ${bill}")


# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

couple = name1 + name2
lower_case_couple = couple.lower()
t = lower_case_couple.count("t")
r = lower_case_couple.count("r")
u = lower_case_couple.count("u")
e = lower_case_couple.count("e")
true = t+r+u+e
l = lower_case_couple.count("l")
o = lower_case_couple.count("o")
v = lower_case_couple.count("v")
e = lower_case_couple.count("e")
love = l+o+v+e
score = int(str(true) + str(love))
if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")

