# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#average of numbers
#Write your code below this row 👇
total_height = 0
for height in student_heights:
    total_height += height
#print(total_height)

number_students = 0
for student in student_heights:
    number_students += 1
#print(number_students)

answer = round(total_height / number_students)
print(answer)

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆
# max number using for loop instead of max
#Write your code below this row 👇
largest_score = 0
for score in student_scores:
    if score > largest_score:
        largest_score = score
print(f"The highest score in the class is {largest_score}")

# to add envelopes
total = 0
for number in range(1, 25):
  total += number
print(total)

#FizzBuzz game
total = range(1, 101)

for number in total:
    if number % 3 == 0 and number % 5 == 0:
        print ("Fizz Buzz")
    elif number % 5 == 0:
        print ("Buzz")
    elif number % 3 == 0:
        print ("Fizz")
    else:
        print(number)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letters = random.sample(letters,nr_letters)
numbers = random.sample(numbers,nr_numbers)
symbols = random.sample(symbols, nr_symbols)
letters.extend(numbers)
symbols.extend(symbols)
random.shuffle(letters)
password = ''.join([str(elem) for elem in letters])
print(password)
        
