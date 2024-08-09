# Write code below 💖

# beginning message
print('===================')
print('Rock Paper Scissors')
print('===================')
print('1) ✊')
print('2) ✋')
print('3) ✌️')
answer = int(input('Pick a number:  '))
print('   ')


# Say what the users answer is
if answer == 1:
  print('You chose Rock')
elif answer == 2:
  print('You chose Paper')
elif answer == 3:
  print('You chose Scissors')
else:
  print("Your answer wasn't an option..")


# telling the cpu what to pick AND how to say their answer
import random
random = random.randint(1, 3)

if random == 1:
  com_answer = 'Rock'
elif random == 2:
  com_answer = 'Paper'
elif random == 3:
  com_answer = 'Scissors'

if random == 1:
  print('CPU chose Rock')
elif random == 2:
  print('CPU chose Paper')
elif random == 3:
  print('CPU chose Scissors')
print('   ')

# did you win or lose?
if random == answer:
  print('Draw!')
elif random == 1 and answer == 2:
  print('You Win!')
elif random == 1 and answer == 3:
  print('You Lose...')
elif random == 2 and answer == 1:
  print('You Lose...')
elif random == 2 and answer == 3:
  print('You Win!')
elif random == 3 and answer == 2:
  print('You Lose...')
elif random == 3 and answer == 1:
  print('You Win!')
else:
  print("Can't play, try again")


