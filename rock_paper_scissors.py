# rock paper scissors.. SHOOT!
# I wanted to use words instead of numbers 💕

import random

word_to_int = {"rock": 1, "paper": 2, "scissors": 3}

answers = ['rock', 'paper', 'scissors']
# converts cpu choice into integer
chosen_str_answer =  random.choice(answers)
chosen_answer = word_to_int[chosen_str_answer]

print('===================')
print('      ✊ ✋ ✌      ')
print('===================')


my_choice = input('Rock, Paper, Scissors?: ' )

print('you chose: ' + my_choice)
# chosen_str_answer displays words
print('computer chose: '  + chosen_str_answer)

# converts my choice to an integer ,,, "lower" is added for case sensitivity
my_choice = word_to_int[my_choice.lower()]

# the verdict
if chosen_answer == my_choice:
  print('tie')
elif (chosen_answer == 1 and my_choice == 2) or (chosen_answer == 2 and my_choice == 3) or (chosen_answer == 3 and my_choice == 1):
  print('you win!')
elif (chosen_answer == 1 and my_choice == 3) or (chosen_answer == 2 and my_choice == 1) or (chosen_answer == 2 and my_choice == 2):
  print('you lose...')
else:
  print('error')
