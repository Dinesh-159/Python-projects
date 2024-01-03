import random

comp_choice = random.choice(['rock' , 'paper','scissors'])

user_choice = str(input('Enter ur move: '))

print(comp_choice)

if (comp_choice == user_choice):
    print("TIE")

elif (user_choice == 'rock' and comp_choice == 'scissors'):
    print('You win')

elif(user_choice == 'paper' and comp_choice == 'rock'):
    print('You win')

elif(user_choice == 'scissors' and comp_choice == 'paper'):
    print('You win')

else:
    print("Better luck next time :)")