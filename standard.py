import random

class Card:
	suit: str
	val: str
	
	def __init__(self, _val, _suit):
		self.suit = _suit
		self.val = _val
	
	def name(self):
		return self.val + ' of ' + self.suit

	def print(self):
		print(self.name())

values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

# Generate a standard 52 card deck
deck = []
for s in suits:
	for v in values:
		deck.append(Card(v, s))

# Shuffle the deck
def shuffle(deck=deck):
	shuffled_deck = []
	while len(shuffled_deck) < 52:
		index = random.randint(0, len(deck) - 1)
		shuffled_deck.append(deck[index])
		del deck[index]
	return shuffled_deck

deck = shuffle(deck)

# Returns a hand of the drawn cards
def draw(num=1, deck=deck):
	hand = deck[0:num]
	for x in range(num):
		del deck[x]
	return hand

# Draw 2 cards
hand = draw(2)
for h in hand:
	h.print()







