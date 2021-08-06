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

# Need to determine winner


# One idea is to sequentially check for the best type of hand all the way down to the worst
# Then we also have to settle ties
# 7 choose 5 is already 21 possibilities

# Given 7 cards, check if there exists a royal flush poker hand
def checkRoyalFlush(card_list):
	# First there has to be 5 cards of the same suit
	# Then, given that suit, all those cards must be exactly A, K, Q, J, 10
	suit_dict = {k:[] for k in suits}
	for c in card_list:
		suit_dict[c.suit].append(c)
	# Sort the dictionary of cards by most popular suit
	# Note that since there are 7 cards and 4 suits, you cannot have a tie for the most popular suit
	suit_dict = dict(sorted(suit_dict.items(), key=lambda x: len(x[1]), reverse=True))
	#print(suit_dict)
	# Get royal flush values
	rf_vals =  values[9:] + [values[0]]
	val_dict = {k:False for k in rf_vals}
	# Look at the most popular suit
	pop_suit = list(suit_dict.items())[0][1]
	# There must be more than 5 cards of the same suit to have a royal flush
	if not len(pop_suit) >= 5:
		return False
	# Mark the values we see among cards in the most popular suit
	for c in pop_suit:
		if c.val in val_dict.keys():
			val_dict[c.val] = True
	# Fail if not all royal flush values were seen
	for v in val_dict.keys():
		if not val_dict[v]:
			return False
	return True



print(checkRoyalFlush(table_cards + hand))
print(checkRoyalFlush(table_cards + bobHand))
print(checkRoyalFlush(table_cards + aliceHand))

def testRoyalFlush():
	rf = [Card(v, 'Hearts') for v in (values[9:] + [values[0]])] 
	rf.append(Card(7, 'Clubs'))
	rf.append(Card(8, 'Diamonds'))
	print(checkRoyalFlush(rf))
testRoyalFlush()


