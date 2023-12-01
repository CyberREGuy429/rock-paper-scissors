import random
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
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, type 1 for Paper, type 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
  print("Invalid number, you lose!")
else:
  print(game_images[user_choice])
  
  computer_choice = random.randint(0, 2)
  print("The computer chooses")
  print(game_images[computer_choice])
  
  # if user_choice == 0:
  #   print(rock)
  # elif user_choice == 1:
  #   print(paper)
  # elif user_choice == 2:
  #   print(scissors)
  
  # if computer_choice == 0:
  #   print(rock)
  # elif computer_choice == 1:
  #   print(paper)
  # elif computer_choice == 2:
  #   print(scissors)
    
  if user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice > user_choice:
    print("You lose!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
  elif user_choice > computer_choice:
    print("You win!")
  else:
    print("Draw!")
  exit()