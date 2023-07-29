#coin flip
#import random
#random_flip = random.randint(0,1)
#if random_flip == 1:
    #print("Heads")
#else:
    #print("Tails")

#random name for meal
# Import the random module here
#import random
# Split string method
#names_string = input("Give me everybody's names, separated by a comma. ")
#names = names_string.split(", ")
#buyer = random.choice(names)
#print(buyer + " is going to buy the meal today")

#Rock, Paper, Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_images = [rock, paper, scissors]
user_results = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
import random
if user_results >= 3 or user_results < 0:
    print("invalid entry you lose")
else:    
    print(game_images[user_results])
computer_results = random.randint(0,2)
print("computer chose:")
print(game_images[computer_results])

print(f"computer_chose {computer_results}")

if user_results == 0 and computer_results == 2:
  print("You win, Rock smashes scissors!")
elif user_results == 1 and computer_results == 2:
  print("you lose, Scissors cut paper ")
elif user_results == 2 and computer_results == 2:
  print("draw pick again")
elif user_results == 0 and computer_results == 1:
  print("You lose, Paper covers rock")
elif user_results == 1 and computer_results == 0:
  print("You win, Paper covers rock")
elif user_results == 2 and computer_results == 1:
  print("You win, Scissors cut paper")
elif user_results == 1 and computer_results == 1:
  print("draw, pick again")
elif user_results == 0 and computer_results == 0:
  print("draw, pick again")
elif user_results == 2 and computer_results == 0:
  print("You lose, Rock smashes scissors")
else:
  print("invalid entry you lose")
