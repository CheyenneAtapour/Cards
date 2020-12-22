# Monte Carlo Simulator for Hearthstone Ranks

# Winning a game gives you a star
# if you win 3 games in a row, you start win-streaking and get an extra star per win
# win streaks stop when you hit diamond 5
# we will be ignoring star bonuses 
# losing a game loses you a star
# when you first enter a new rank, you start with 1 star in that rank ? 
# you cannot fall below rank 10 of a new medal rank, and you cannot fall below 5 of a medal rank either

# ranks are bronze, silver, gold, platinum, diamond, then legend, all with positions 10-1
# each rank has 3 stars to earn

# you get 3 stars in your rank, then your next win will get you the next rank with 1 star
# when you lose with 0 stars in your rank, your next rank will be the previous rank with 2 stars

import random

WINRATE = 67

STARTING_RANK = 4
STARTING_POSITION = 2
STARTING_STARS = 1
STARTING_WINSTREAK = 0
#STAR_BONUS = 0

ranks = {0:'bronze', 1:'silver', 2:'gold', 3:'platinum', 4:'diamond', 5:'legend'}
ranksNum = {v: k for k, v in ranks.items()} # {'bronze':0, 'silver':1, ...}


class Rank:
	def __init__(self):
		self.rank = ranks[STARTING_RANK]
		self.pos = STARTING_POSITION
		self.stars = STARTING_STARS
		self.winstreak = STARTING_WINSTREAK
		#self.starbonus = STAR_BONUS

	def getRank(self):
		return self.rank

	def getStars(self):
		return self.stars

	def getRankAndStars(self):
		return (self.rank, self.stars)

	def advanceRank(self):
		self.rank = ranks[ranksNum[self.rank]+1]
		pass

	def advancePos(self, newStars):
		# if it's over 10, need to advance rank
		if self.pos == 1:
			self.advanceRank()
			self.pos = 10
			self.stars = newStars
		else:
			self.pos -= 1
			self.stars = newStars
		pass

	def reducePos(self):
		self.pos += 1
		self.stars = 2
		pass

	def loseGame(self):
		self.winstreak = 0
		# if 0 stars, and not a rank floor, need to decrement position
		if self.stars == 0 and not self.pos % 5 == 0:
			self.reducePos()
		elif self.stars == 0 and self.pos % 5 == 0:
			pass
		else:
			self.stars -= 1
		pass	

	def winGame(self):
		addStars = 1
		# if we have won 2 previous games, and we are not diamond 5 we are winstreaking
		if self.winstreak >= 2 and (ranksNum[self.rank] < 4 or (ranksNum[self.rank] == 4 and self.pos > 5)):
			addStars += 1
		self.stars += addStars
		# if more than 3 stars, advance rank
		if self.stars > 3:
			self.advancePos(self.stars - 3)
		self.winstreak += 1
		pass

	def print(self):
		print("Rank: " + self.rank + " Position: " + str(self.pos) + " Stars: " + str(self.stars))
		pass
	
	def starsLeft(self):
		save = (self.rank, self.pos, self.stars, self.winstreak)
		x = 0
		self.winstreak = 0
		while not self.rank == 'legend':
			self.winGame()
			self.winstreak = 0
			x += 1
		self.rank = save[0]
		self.pos = save[1]
		self.stars = save[2]
		self.winstreak = save[3]
		return x

def rankRun():
	rank = Rank()
	print("Starting rank at: ")
	rank.print()
	x = 0
	while True:
		y = random.randint(1,101)
		x += 1
		if y <= WINRATE:
			rank.winGame()
			print("won game")
		else:
			rank.loseGame()
			print("lost game")
		rank.print()
		if rank.rank == 'legend':
			print("Took " + str(x) + " games to reach legend.")
			return x

def monteCarlo():
	avg = 0
	for x in range(1000):
		avg += rankRun()
	print("Over 1000 runs, " + str(avg / 1000) + " games on average to reach legend with winrate " + str(WINRATE) + "%")

def findStarsLeft():
	rank = Rank()
	print(rank.starsLeft())

monteCarlo()
#findStarsLeft()
