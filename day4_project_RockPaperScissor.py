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
game=[rock,paper,scissors]
choice=int(input("What do you choose ? 0-Rock 1-Paper 2-Scissors \n"))
print(game[choice])
comp_choice=random.randint(0,2)
print(game[comp_choice])
if choice==0:
  if comp_choice==1:
    print("Computer wins")
  elif comp_choice==2:
    print("You win")
  else:
    print("Match drawn")
elif choice==1:
  if comp_choice==0:
    print("You win")
  elif comp_choice==2:
    print("Computer wins")
  else:
    print("Match drawn")
elif choice==2:
  if comp_choice==0:
    print("Computer wins")
  elif comp_choice==1:
    print("You win")
  else:
    print("Match drawn")





