"""
11 = jack
12 = queen
13 = king
14 = ace
c = clubs
d = diamonds
h = hearts
s = spades
"""
import random
deck = []
suits = ["clubs","diamonds","hearts","spades"]

#generate deck
for x in range(2, 15):
    for y in suits:
        deck.append(str(x)+y)
print (deck)

#clear card memory and shuffle
def shuffle():
    Nused = []
    Eused = []
    Sused = []
    Wused = []
    random.shuffle(deck)
    print (deck)
shuffle()
