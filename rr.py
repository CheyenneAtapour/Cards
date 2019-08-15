# this is a round-robin simulator

import random

def key(element): # key for sorting
	return element[1]

players = input("How many players? ") # even number of players
players = int(players, 10)
rounds = input("How many rounds? ") # rounds < players
rounds = int(rounds, 10)

# make list of lists, representing each player 
# [ [#wins, #losses], [#wins, #losses] ]
scores = []
for x in range( players ):
	temp = [ 0, 0 ]
	scores.append( temp )

x = 1
while x <= rounds:
	
	# initialize array of unmatched players
	start = [] 
	for a in range(players):
		start.append(a)

	while not len(start) == 0:
		# scores[y] plays scores[y+x mod len(scores)]
		first = start.pop(0)
		second = (y + x) % len(scores)

		result = random.randint(0,100)
		if result < 50: # first player wins
			scores[first][0] += 1
			scores[second][1] += 1
		else: # second player wins
			scores[first][1] += 1
			scores[second][0] += 1
	x += 1

scores.sort(key=key)
print(scores)


'''
# for each round, we want to pair random players that have
# not yet played each other, until they have all played each
# other and we then reset

dic = {}

x = 0
y = 0

# generate all possible pairs and initialize
while x < players:
	y = x + 1
	while y < players:
		dic[(x, y)] = 0 # boolean for "paired"
		y += 1
	x += 1

# randomly pair off players
# fix one player to pair
# randomly choose another player to pair with

for b in range(rounds):
	# create array to keep track of remaining players to be paired
	start = []
	for a in range(players):
		start.append(a)

	while not len(start) == 0: # if players was odd, we would need to implement byes
		first = start.pop()
		second = start.pop(random.randint(0, len(start)-1)) # both args inclusive
		if first > second: # flip order of pair if needed
			temp = second
			second = first
			first = temp
		while(dic[first, second] == 1):
			start.append(second)
			second = start.pop(random.randint(0, len(start)-1))
			if first > second: # flip order of pair if needed
				temp = second
				second = first
				first = temp
		dic[(first, second)] = 1 # players paired
		result = random.randint(0,100)
		if result < 50: # first player wins
			scores[first][0] += 1
			scores[second][1] += 1
		else: # second player wins
			scores[first][1] += 1
			scores[second][0] += 1

scores.sort(key=key)
print(scores)
'''





# a bit naive way to proceed: 
# same player cannot be paired
# pair needs to be new

#while( (not first == second) and (not dic[(first,second)] == 1) ):
#	first = random.randint(0, players-1)
#	second = random.randint(0, players-1)
#	start.pop(first)
#	start.pop(second)
#	dic[(first, second)] = 1 # players paired
#	result = random.randint(0,101)
#	if result < 50: # first player wins
#		scores[first][0] += 1
#		scores[second][1] += 1
#	else: # second player wins
#		scores[first][1] += 1
#		scores[second][0] += 1