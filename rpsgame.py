import random

try:
    input = raw_input
except NameError:
    pass

comp = random.choice(['rock','paper','scissors'])
user = input('rock, paper or scissors? Enter lowercase: ')

trumped_by = {
    'rock': ['paper'],
    'paper': ['scissors'],
    'scissors': ['rock']
  }

if comp == user:
  print('Tie')
else:
  if user in trumped_by[comp]:
    print('You win!')
  else:
    print('I win!')