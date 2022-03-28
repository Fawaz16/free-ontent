import random
# Rock
rps = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]
comp_wins =0
player_wins=0

def choose_option():
  user_choice = input('choose rock, paper or scissors')
  if user_choice in ['Rock', 'rock', 'r', 'R']:
    user_choice ='r'
  elif user_choice in ['Paper', 'paper', 'p', 'P']:
    user_choice ='p'
  elif user_choice in ['Scissors', 'scissors', 's', 'S']:
    user_choice ='r'
  else :
    print('i dont understand .')
    choose_option()


   def  computer_option():
      comp_choice = random.randint(rps)
  if comp_choice == '1'
  comp_choice== 'r'
  elif comp_choice == '2'
  comp_choice== 'p'

  else comp_choice == '3'
  comp_choice== 's'