oppMon = []
x = 0
a = False
prompt = ""
oppHP = 1000

def showField():
	print("HP = " + str(oppHP))
	if(oppHP <= 0):
		print("Opponent has lost the game. You win!")
		quit()
	if(oppMon == []):
		print("Opponent's battlefield contains no monsters.")
	for i in range(len(oppMon)):
		print(oppMon[i])
	return 0


for i in range(50):
	if(x <= 4):
		if(a == True):
			a = False
			x = x + 1
			oppMon = oppMon + [x*10]
		else:
			a = True
	elif(x > 4):
		if(a == True):
			a = False
			oppMon = oppMon + [50]
		elif(a == False):
			a = True
	showField()
	while(prompt != 0):
		prompt = input("1. Declare an attack, 2. Declare a board clear, 0. Pass the turn")
		if(prompt == 1):
			pos = input("Declare target ")
			dmg = input("Declare damage")
			if(pos == -1):
				oppHP -= dmg
			else:
				oppMon[pos] = oppMon[pos] - dmg
				if(oppMon[pos] <= 0):
					if(pos < len(oppMon) - 1 ):
						oppMon = oppMon[0:pos] + oppMon[pos+1:]
					elif(pos >= len(oppMon) - 1):
						oppMon = oppMon[0:-1]
			showField()
		elif(prompt == 2):
			dmg = input("Declare board clear damage amount")
			for i in range(len(oppMon)):
				oppMon[i] = oppMon[i] - dmg
			showField()
		else:
			print("Passing turn")
	prompt = ""
