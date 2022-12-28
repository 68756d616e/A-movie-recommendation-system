# A movie recommendation system

import random

print("Welcome to yout a movie recommendation system")

# Different type of genres

action = ['action 1', 'action 2']
horror = ['horror 1', 'horror 2']
comedy = ['comedy 1', 'comedy 2']
romantic = ['romantic 1', 'romantic 2']


while True:
    # The user will choose what genre of moveis they would like
    question = input("What type of movies do you like, action, horror, comedy or romantic? :")

    if question == 'action':
        print(random.choice(action))
    elif question == 'horror':
        print(random.choice(horror))
    elif question == 'comedy':
        print(random.choice(comedy))
    elif question == 'romantic':
        print(random.choice(romantic))
    else:
        print("Please choose action, horror, comedy or romantic")

