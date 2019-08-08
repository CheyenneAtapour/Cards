# ~ 13 games to advance in plat (4 winstreak) with a 70% winrate
# ~ 12 games to advance in plat with an 80% winrate

# ~ 16 games to advance in legend with 70% winrate
# about the same for 80%

# one more koaki, one more treacherous in bandit keith Leng LING

import random

count = 0
winstreak = 0
av = 0
adv = 0

for x in range(100):
	count = 0
	while True:
		count += 1
		y = random.randint(1,101)
		print(y)
		if y >= 20:
			winstreak += 1
		else:
			winstreak = 0
		if winstreak == 5:
			print("It took " + str(count) + " games to advance")
			adv += 1
			av += count
			break

av = av / adv 

print("on average, it took you " + str(av) + " games to advance over 100 trials")