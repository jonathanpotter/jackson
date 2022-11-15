import random


number_value = [ 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King' ]

suits = [ 'Diamonds', 'Hearts', 'Spades', 'Clubs' ]

print("We picked the " + random.choice(number_value) + " of " + random.choice(suits) + ".")
