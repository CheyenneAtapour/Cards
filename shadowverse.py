# Calculates the average number of games to reach grandmaster in Shadowverse

import random

WINRATE = 70
STARTRANK = 27256

def monteCarlo():
	avg = 0
	for x in range(1000):
		num = 0
		streak = 0
		rank = STARTRANK
		while True:
			game = random.randint(1, 101)
			num += 1

			# Won a game
			if game <= WINRATE:
				streak += 1
				rank += 100

			# Lost a game
			else:
				streak = 0
				rank -= 100

			# Apply winstreak points
			if streak >= 2 and rank < 50000:
				rank += 30

			# Check ending condition
			if rank >= 60000:
				print("Took " + str(num) + " games to reach grandmaster\n")
				avg += num
				break
	print("Over 1000 runs, took " + str(avg / 1000) + " games to reach grandmaster\n")
	return

monteCarlo()