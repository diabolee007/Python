#tip calculator
print('Welcome to the tip calculator.')
bill = float(input("What was the total bill? $"))
tip = int(input('what percentage tip would you like to give? 10, 12, or 15?\n'))
people = int(input('How many people to split the bill?\n'))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person) # for 2 decimal places
print(f"Each person should pay: ${final_amount}" )


#BMI calculator
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
BMI = round(weight / height ** 2)
if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI > 30:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")

