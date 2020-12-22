# Calculates generic winrate, stores in file
# Instructions:
# my_script.py -f "C:\path\to\my\file to read﻿"

def updateFile(myFile, wins, losses):
	# Write winrate data to file
	f = open(myFile, 'w')
	f.write(str(wins) + "\n")
	f.write(str(losses))
	f.close()

from argparse import ArgumentParser

# Set up command line file parser
parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="myFile", help="Open specified file")
args = parser.parse_args()
myFile = args.myFile

# Get winrate data from file
f = open(myFile)
lines = f.readlines()
wins = int(lines[0])
losses = int(lines[1])
f.close()

while True:
	totalGames = wins + losses
	if totalGames == 0:
		print("Play some games and winrate will show here!")
	else:
		print("Wins: " + str(wins))
		print("Losses: " + str(losses))
		print("Current winrate: " + str(wins / totalGames))
	val = input("Game result: ")
	if (val == 'l' or val == 'L'):
		losses += 1
	elif (val == 'w' or val == 'W'):
		wins += 1
	else:
		print("Invalid selection")
	updateFile(myFile, wins, losses)