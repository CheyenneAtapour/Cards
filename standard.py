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

def printCards(card_list):
	for c in card_list:
		c.print()

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
	for x in range(0, num):
		del deck[0]
	return hand

# Draw 2 cards
print('Your hand is :')
print()
hand = draw(2)
printCards(hand)

print()
print('Bob\'s hand is :')
print()
bobHand = draw(2)
printCards(bobHand)

print()
print('Alice\'s hand is :')
print()
aliceHand = draw(2)
printCards(aliceHand)

print()
input('Continue to flop')

print()
print('Flop is :')
print()
flop = draw(3)
printCards(flop)

print()
input('Continue to turn')

print()
print('Turn is :')
print()
turn = draw(1)
printCards(turn)

print()
input('Continue to river')

print()
print('River is :')
print()
river = draw(1)
printCards(river)

print()
table_cards = flop + turn + river

printCards(table_cards)








