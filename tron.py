# Calculate the probability that we land on tron by turn 3 or 4 with various mulligan strategies
# Assume we draw 7 cards and no mulligans
import random
import requests

def rng(min, max):
	source = "https://www.random.org/integers/?num=1&min=" + str(min) + "&max=" + str(max) + "&col=5&base=10&format=plain&rnd=new"
	number = requests.get(source)
	number = int(number.text)
	return number

class Card:
	name: str
	cost: str
	
	def __init__(self, _name, _cost):
		self.name = _name
		self.cost = _cost

	def print(self):
		print(self.name)

def printCards(card_list):
	for c in card_list:
		c.print()

# Insert num copies of card into deck
def insert_deck(deck, card, num):
	for i in range(num):
		deck.append(card)

# Create the deck
deck = []
insert_deck(deck, Card("sylvan scrying", 2), 4)
insert_deck(deck, Card("ancient stirrings", 1), 4)
insert_deck(deck, Card("blast zone", 0), 1)
insert_deck(deck, Card("boseiju, who endures", 0), 1)
insert_deck(deck, Card("forest", 0), 3)
insert_deck(deck, Card("sanctum of ugin", 0), 1)
insert_deck(deck, Card("Urza's Mine", 0), 4)
insert_deck(deck, Card("Urza's Power Plant", 0), 4)
insert_deck(deck, Card("Urza's Tower", 0), 4)
insert_deck(deck, Card("Emrakul, the promised end", 13), 1)
insert_deck(deck, Card("Kozilek, butcher of truth", 10), 1)
insert_deck(deck, Card("Ulamog, the ceaseless hunger", 10), 2)
insert_deck(deck, Card("Wurmcoil engine", 6), 2)
insert_deck(deck, Card("Warping Wail", 2), 2)
insert_deck(deck, Card("Chromatic Sphere", 1), 3)
insert_deck(deck, Card("Chromatic Star", 1), 4)
insert_deck(deck, Card("Expedition Map", 1), 4)
insert_deck(deck, Card("Karn Liberated", 7), 4)
insert_deck(deck, Card("Karn, The great creator", 4), 4)
insert_deck(deck, Card("Oblivion Stone", 3), 2)
insert_deck(deck, Card("Relic of Progenitus", 1), 2)
insert_deck(deck, Card("Ugin, the ineffable", 6), 1)
insert_deck(deck, Card("Ugin, the spirit dragon", 8), 2)

# Shuffle the deck
def shuffle(deck=deck):
	shuffled_deck = []
	length = len(deck)
	while len(shuffled_deck) < length:
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

# Returns the position of first card with matching name in hand, -1 if not found
def search_hand(hand, name):
	counter = 0
	for x in hand:
		if x.name == name:
			return counter
		counter += 1
	return -1

def check_tron(hand):
	if search_hand(hand, "Urza's Mine") > 0 and search_hand(hand, "Urza's Power Plant") > 0 and search_hand(hand, "Urza's Tower") > 0:
		return True
	else:
		return False

def check_two_lands(hand):
	unique_lands = 0
	if search_hand(hand, "Urza's Mine") > 0:
		unique_lands += 1
	if search_hand(hand, "Urza's Power Plant") > 0:
		unique_lands += 1
	if search_hand(hand, "Urza's Tower") > 0:
		unique_lands += 1
	if unique_lands == 2:
		return True
	else:
		return False

def check_one_land(hand):
	unique_lands = 0
	if search_hand(hand, "Urza's Mine") > 0:
		unique_lands += 1
	if search_hand(hand, "Urza's Power Plant") > 0:
		unique_lands += 1
	if search_hand(hand, "Urza's Tower") > 0:
		unique_lands += 1
	if unique_lands == 1:
		return True
	else:
		return False

def card_to_battlefield(hand, position, field):
	field.append(hand[position])
	del hand[position]

def simulate_hands(num=10000):
	tron_counter = 0
	two_lands = 0
	one_land = 0

	for x in range(10000):
		print('Your hand is :')
		print()
		hand = draw(7, deck)
		printCards(hand)
		print()

		if check_tron(hand):
			print('found tron')
			tron_counter += 1
		elif check_two_lands(hand):
			two_lands += 1
		elif check_one_land(hand):
			one_land += 1

		# Put back cards and shuffle deck
		deck = deck + hand
		deck = shuffle(deck)

	print("Over 10k hands, had " + str(tron_counter) + " hands with tron assembled (no mulligans)")
	print("Hands with 2 unique lands " + str(two_lands))
	print("Hands with 1 unique land " + str(one_land))


print('Your hand is :')
print()
hand = draw(7, deck)
printCards(hand)
print()

print('Remainder of deck: ')
print()
printCards(deck)
print()


field = []
tron_check = {0: ["tower", 0], 1: ["plant", 0], 2: ["mine", 0]} 	# Used to keep track of played tron lands. tron_check[1][1] = 1 means power plant played


# Algorithm to play Tron:
# 1. If not all of Urza's tower, Urza's mine, and Urza's power plant are on the field, play one of them if in the hand
# 2. If we can't progress towards tron, play a green land if we have one, otherwise any land is fine

# Nuances:
# Objectively, if we can complete tron, or know we can complete tron within 3 turns, we should do this
# If we cannot complete tron, we might consider playing a forest or green land instead of progressing towards tron to activate a green spell to find a missing land

# step 1
land_played = False

# Haven't played a land, and no tower on field, try playing tower
if not land_played and tron_check[0][1] == 0:
	pos = search_hand(hand, "Urza's Tower")
	if pos >= 0:
		card_to_battlefield(hand, pos, field)
		land_played = True

if not land_played and tron_check[1][1] == 0:
	pos = search_hand(hand, "Urza's Power Plant")
	if pos >= 0:
		card_to_battlefield(hand, pos, field)
		land_played = True

if not land_played and tron_check[2][1] == 0:
	pos = search_hand(hand, "Urza's Mine")
	if pos >= 0:
		card_to_battlefield(hand, pos, field)
		land_played = True

if not land_played:
	pos = search_hand(hand, "forest")
	if pos >= 0:
		card_to_battlefield(hand, pos, field)
		land_played = True

if not land_played:
	pos = search_hand(hand, "boseiju, who endures")
	if pos >= 0:
		card_to_battlefield(hand, pos, field)
		land_played = True

if not land_played:
	pos = search_hand(hand, "sanctum of ugin")
	if pos >= 0:
		card_to_battlefield(hand, pos, field)
		land_played = True

if not land_played:
	pos = search_hand(hand, "blast zone")
	if pos >= 0:
		card_to_battlefield(hand, pos, field)
		land_played = True

if not land_played:
	pos = search_hand(hand, "Urza's Tower")
	if pos >= 0:
		card_to_battlefield(hand, pos, field)
		land_played = True

if not land_played:
	pos = search_hand(hand, "Urza's Power PLant")
	if pos >= 0:
		card_to_battlefield(hand, pos, field)
		land_played = True

if not land_played:
	pos = search_hand(hand, "Urza's Mine")
	if pos >= 0:
		card_to_battlefield(hand, pos, field)
		land_played = True

print("Hand:")
printCards(hand)
print()

print("Field:")
printCards(field)
print()