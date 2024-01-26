#pylint:disable=W0612
import random, time
from termcolor import colored
game = 0
player = 2
difficulty = 0
color1 = 'green'
color2 = 'red'
colorN = 'yellow'
fields = ["#","#","#","#","#","#","#","#","#"]
patterns = ["012","345","678","036","147","258","048","246"]
patts = [152,578,376,310,801,627]
colors = ['yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow','yellow']



def blank(x):
	x = int(x)
	for i in range (0,x):
		print("")
def result():
	print(colored(fields[0],colors[0]),colored(fields[1],colors[1]),colored(fields[2],colors[2]))
	print(colored(fields[3],colors[3]),colored(fields[4],colors[4]),colored(fields[5],colors[5]))
	print(colored(fields[6],colors[6]),colored(fields[7],colors[7]),colored(fields[8],colors[8]))
	
def draw():
	for x in fields:
		if x == "#":
			return 0
	return 1


	
def end():
	global game
	for x in patterns:
		pattern = int(x)
		digit1 = pattern//100
		digit2 = ((pattern%100)//10)
		digit3 = pattern%10
		if fields[digit1] != "#" and fields[digit1] == fields[digit2] and fields[digit1] == fields[digit3]:
			game = 0
			return 1
		if draw() == 1:
			game = 0
			return 2
			

		
def getnum(player):
	blank(1)
	try:
		print(player,",input the number of the field you want to put your mark on (1-9)")
		print("To see the layout again enter L")
		inpt = input()
		if inpt == "L" or inpt == "l":
			blank(1)
			print(colored('1 2 3',colorN))
			print(colored('4 5 6',colorN))
			print(colored('7 8 9',colorN))
			return getnum(player)
		tmp = int(inpt)-1
	except:
		blank(1)
		print("An exception occured")
		blank(1)
		return getnum(player)
	
	if tmp > 8:
		tmp = 8
	if tmp < 0:
		tmp = 0
	wert = int(tmp)
	if fields[wert] == "#":
		return wert
	else:
		print("This field is already occupied, try again ",player)
		result()
		return getnum(player)
		
		
def p1():
	global player
	player = 1
	field1 = getnum(p1name)
	fields[field1] = "X"
	colors[field1] = color1
	result()
	blank(1)
	if end() == 1:
		print(p1name," won the game")
		result()
		blank(2)
		return
	if end() == 2:
		print(p1name, " and ",p2name," tied the game! GG!" )
		blank(1)
		result()
		blank(2)
		return
		
def p2():
	global player
	player = 2
	field2 = getnum(p2name)
	fields[field2] = "O"
	colors[field2] = color2
	result()
	blank(1)
	if end() == 1:
		print(p2name," won the game")
		blank(1)
		result()
		blank(2)
		return
	if end() == 2:
		print(p1name, "and",p2name,"tied the game! GG!" )
		blank(1)
		result()
		blank(2)
		return
		
def bot():
	global difficulty
	if difficulty == 0:
		boteasy()
	if difficulty == 1:
		bothard()

def boteasy():
	global player
	global p1name
	player = 2
	p1name = "easyBOT"
	if fields[4] == "#":
		fieldBOT = 4
	else:
		while True:
			tmp = int(random.randint(0,8))
			if fields[tmp] == "#":
				fieldBOT = tmp
				break
	time.sleep(0.5)			
	fields[fieldBOT] = "O"
	colors[fieldBOT] = color2
	print(p2name," chose field ",fieldBOT+1)
	result()
	if end() == 1:
		print(p2name," won the game")
		blank(1)
		result()
		blank(2)
		return
	if end() == 2:
		print(p1name, " and ",p2name," tied the game! GG!" )
		blank(1)
		result()
		blank(2)
		return
		
def bothard():
	global player
	global p2name
	player = 2
	p2name = "hardBOT"
	problem = 100
	count = int(0)
	for x in patterns:
			pattern = int(x)
			digit1 = pattern//100
			digit2 = ((pattern%100)//10)
			digit3 = pattern%10
			if fields[digit1] == "#" and fields[digit2] == "O" and fields[digit3] == "O":
				problem = digit1
				fieldBOT = digit1
			if fields[digit1] == "O" and fields[digit2] == "#" and fields[digit3] == "O":
				problem = digit2
				fieldBOT = digit2
			if fields[digit1] == "O" and fields[digit2] == "O" and fields[digit3] == "#":
				problem = digit3
				fieldBOT = digit3
	if problem == 100:
		for x in patterns:
			pattern = int(x)
			digit1 = pattern//100
			digit2 = ((pattern%100)//10)
			digit3 = pattern%10
			if fields[digit1] == "#" and fields[digit2] == "X" and fields[digit3] == "X":
				problem = digit1
				fieldBOT = digit1
			if fields[digit1] == "X" and fields[digit2] == "#" and fields[digit3] == "X":
				problem = digit2
				fieldBOT = digit2
			if fields[digit1] == "X" and fields[digit2] == "X" and fields[digit3] == "#":
				problem = digit3
				fieldBOT = digit3
	if fields[4] == "#" and problem == 100:
		fieldBOT = 4
		problem = 4
		
	elif problem == 100:
		for y in patts:
			patt = int(y)
			dig1 = patt // 100
			dig2 = (patt%100)//10
			dig3 = patt %10
			
			if fields[dig1] == fields[dig2] == "X" and fields[dig3] == "#":
				fieldBOT = dig3
				problem = 69
	
	if problem == 100:
		if fields[4] == "X":
			if fields[0] == fields[1] == fields[2] == fields[3] == fields[5] == fields[6] == fields[7] == fields[8] == "#":
				fieldBOT = 2
				problem = 99
				
	elif problem == 100:
		for x in patterns:
			pattern = int(x)
			digit1 = pattern//100
			digit3 = pattern%10
			if fields[digit1] != "#" or fields[digit3] != "#":
				count += 1
		if count == 0:
			problem = 69
			fld = int(random.randint(0,3))
			if fld == 0 or fld == 2:
				fieldBOT = fld
			if fld == 1 or fld == 3:
				fieldBOT = fld+5
	if problem == 100:
		while True:
			tmp = int(random.randint(0,8))
			if fields[tmp] == "#":
				fieldBOT = tmp
				break			
	time.sleep(0.5)			
	fields[fieldBOT] = "O"
	colors[fieldBOT] = color2
	print(p2name," chose field ",fieldBOT+1)
	result()
	if end() == 1:
		print(p2name," won the game")
		blank(1)
		result()
		blank(2)
	if end() == 2:
		print(p1name, " and ",p2name," tied the game! GG!" )
		blank(1)
		result()
		blank(2)
		return
	
def mainmenu():
	global fields
	global player
	global colors
	tmp = input("Do you want to play a game of tic tac toe? (y/n):    ")
	if tmp == "y":
		player = 2
		fields = ["#","#","#","#","#","#","#","#","#"]
		colors = [colorN,colorN,colorN,colorN,colorN,colorN,colorN,colorN,colorN]
		try:
			players = int(input("Input the number of players (1-2):     "))
		except:
				blank(1)
				print("An exception occured")
				blank(1)
				return
				
		if players > 2:
			players = 2
		if players < 1:
			players = 1
		if players == 1:
			singleplayer()
		if players == 2:
			twoplayers()
	else:
		blank(1)
		return
		
def singleplayer():
	global p1name
	global p2name
	global game
	global player
	global difficulty
	game = 1
	p2name = "BOT"
	p1name = input("Input the name of player1:     ")
	try:
		tmp = int(input("Input the difficulty of the bot (0-1):     "))
	except:
		blank(1)
		print("An exception occured")
		blank(1)
		return
	if tmp > 1:
		tmp = 1
	if tmp < 0:
		tmp = 0
	difficulty = tmp
	blank(1)
	result()
	blank(1)
	while True:
		if player == 2:
			if game == 0:
				return
			else:
				p1()
		else:
			if game == 0:
				return
			else:
				bot()
	
def twoplayers():
	global p1name
	global p2name
	global game
	global player
	game = 1
	p1name = input("Input the name of player1:     ")
	p2name = input("Input the name of player2:     ")
	blank(1)
	result()
	blank(1)
	while True:
		if player == 2:
			if game == 0:
				return
			else:
				p1()
		else:
			if game == 0:
				return
			else:
				p2()
	
print("In this game of tic tac toe, you will need to enter the number") 
print("of the field you want to put your mark on. ")
print("The Layout is as following:")
blank(1)
print(colored('1 2 3',colorN))
print(colored('4 5 6',colorN))
print(colored('7 8 9',colorN))
blank(1)
while True:
	mainmenu()
	time.sleep(0.5)
