import time
import sys
import winsound

ANIMBEGIN = (
	"""
						[0,0,0,0,0,0,0]
						[0,0,0,0,0,0,0]
						[0,0,0,0,0,0,0]
						[0,0,0,0,0,0,0]        16.6666666667%
						[0,0,0,0,0,0,0]
						[0,0,0,0,0,0,0]
	""",
	"""
						[0,0,0,0,0,0,0]
						[0,0,0,0,0,0,0]
						[0,0,0,0,0,0,0]
						[0,0,0,0,0,0,0]        33.3333333334%
						[0,0,0,0,0,0,0]
						[1,2,2,1,2,1,1]
	""",
	"""
						[0,0,0,0,0,0,0]
						[0,0,0,0,0,0,0]
						[0,0,0,0,0,0,0]
						[0,0,0,0,0,0,0]        50.0000000001%
						[1,1,2,2,1,1,1]
						[1,2,2,1,2,1,1]
	""",
	"""
						[0,0,0,0,0,0,0]
						[0,0,0,0,0,0,0]
						[0,0,0,0,0,0,0]	
						[1,2,1,1,2,1,2]        66.6666666668%
						[1,1,2,2,1,1,1]
						[1,2,2,1,2,1,1]	
	""",
	"""
						[0,0,0,0,0,0,0]
						[0,0,0,0,0,0,0]
						[2,1,2,1,1,1,2]	
						[1,2,1,1,2,1,2]        83.3333333335%
						[1,1,2,2,1,1,1]
						[1,2,2,1,2,1,1]	
	""",
	"""
						[0,0,0,0,0,0,0]
						[1,2,2,1,2,2,1]
						[2,1,2,1,1,1,2]	
						[1,2,1,1,2,1,2]        100%
						[1,1,2,2,1,1,1]
						[1,2,2,1,2,1,1]	
	""",
	"""
						[1,2,1,2,1,1,2]
						[1,2,2,1,2,2,1]
						[2,1,2,1,1,1,2]	
						[1,2,1,1,2,1,2]        COMPLETED LOADING PROCESS
						[1,1,2,2,1,1,1]
						[1,2,2,1,2,1,1]		
	""",
	"""
	"""
	)
def displayIntro():
	winsound.winsound('kahoot.wav',True)
RangeHM = len(ANIMBEGIN) - 1
tx = 0.5
print(ANIMBEGIN[0])
time.sleep(tx)
print(ANIMBEGIN[1])
time.sleep(tx)
print(ANIMBEGIN[2])
time.sleep(tx)
print(ANIMBEGIN[3])
time.sleep(tx)
print(ANIMBEGIN[4])
time.sleep(tx)
print(ANIMBEGIN[5])
time.sleep(tx)
print(ANIMBEGIN[6])
time.sleep(tx)
for x in range(0,17):
	print()
OPENINGGRAPHIC = (
	"""
					[0,0,0,X]
					[0,0,X,Y]          WELCOME TO
					[0,X,0,Y]   CONNECT 4 by Aiden Golub
					[X,0,0,Y]
					
________________________________________________________________________________________________________________________
	"""
	)
SPACER = (
	"""
VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
	"""
	)
numbers1=[" 1  2  3  4  5  6  7"]
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
spacer1= ["---------------------"]
spacer = (', '.join(spacer1))
numbers = (', '.join(numbers1))
grid6 = [0,0,0,0,0,0,0]
grid5 = [0,0,0,0,0,0,0]
grid4 = [0,0,0,0,0,0,0]
grid3 = [0,0,0,0,0,0,0]
grid2 = [0,0,0,0,0,0,0]
grid1 = [0,0,0,0,0,0,0]
numberclass = [1,2,3,4,5,6,7]
numCheck = ["1","2","3","4","5","6","7"]
Rounds = 16
grids = [grid1, grid2, grid3, grid4, grid5, grid6, numbers]
p1p="x"
p2p="o"
sp="-"
def grid_def():
    print ("",numbers,"\n",spacer,"\n",grid6,"\n",grid5,"\n",grid4,"\n",grid3,"\n",grid2,"\n",grid1)

print(OPENINGGRAPHIC)
print("To start, label each player")
print("")
Player1 = input("Player 1: ")
Player2 = input("Player 2: ")
print("")
gamerule = input("How to play: Sure(y) or Nah I'm Good(n): ")
if gamerule == "y":
	print("                                                                                                         ")
	print(" vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
	print("|   1. "+Player1 +" and "+Player2+" will take turns entering numbers 1-7                                   ")
	print("|   2. Those numbers are which slot you put the gamepiece in from left to right                          ")
	print("|   3. When either "+Player1 +" or "+Player2+" has four gamepieces in a row, they win                      ")
	print("|   GOOD LUCK!                                                                                           ")
	print(" vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
	print("                                                                                                         ") 
print("")
tostart = input("Press (enter) to start the game")
print("")
time.sleep(.5)
print(SPACER)
print("")
grid6n = str(grid6)[1:-1]
grid6n = grid6n.replace(',',' ')
grid6n = grid6n.replace("'",'')
grid6n = grid6n.replace("0",sp)
grid5n = str(grid5)[1:-1]
grid5n = grid5n.replace(',',' ')
grid5n = grid5n.replace("'",'')
grid5n = grid5n.replace("0",sp)
grid4n = str(grid4)[1:-1]
grid4n = grid4n.replace(',',' ')
grid4n = grid4n.replace("'",'')
grid4n = grid4n.replace("0",sp)
grid3n = str(grid3)[1:-1]
grid3n = grid3n.replace(',',' ')
grid3n = grid3n.replace("'",'')
grid3n = grid3n.replace("0",sp)
grid2n = str(grid2)[1:-1]
grid2n = grid2n.replace(',',' ')
grid2n = grid2n.replace("'",'')
grid2n = grid2n.replace("0",sp)
grid1n = str(grid1)[1:-1]
grid1n = grid1n.replace(',',' ')
grid1n = grid1n.replace("'",'')
grid1n = grid1n.replace("0",sp)
print ("",numbers,"\n",spacer,"\n"," "+grid6n,"\n"," "+grid5n,"\n"," "+grid4n,"\n"," "+grid3n,"\n"," "+grid2n,"\n"," "+grid1n)
def conboard():
	grid6n = str(grid6)[1:-1]
	grid6n = grid6n.replace(',',' ')
	grid6n = grid6n.replace("'",'')
	grid6n = grid6n.replace("1",p1p)
	grid6n = grid6n.replace("2",p2p)
	grid6n = grid6n.replace("0",sp)
	grid5n = str(grid5)[1:-1]
	grid5n = grid5n.replace(',',' ')
	grid5n = grid5n.replace("'",'')
	grid5n = grid5n.replace("1",p1p)
	grid5n = grid5n.replace("2",p2p)
	grid5n = grid5n.replace("0",sp)
	grid4n = str(grid4)[1:-1]
	grid4n = grid4n.replace(',',' ')
	grid4n = grid4n.replace("'",'')
	grid4n = grid4n.replace("1",p1p)
	grid4n = grid4n.replace("2",p2p)
	grid4n = grid4n.replace("0",sp)
	grid3n = str(grid3)[1:-1]
	grid3n = grid3n.replace(',',' ')
	grid3n = grid3n.replace("'",'')
	grid3n = grid3n.replace("1",p1p)
	grid3n = grid3n.replace("2",p2p)
	grid3n = grid3n.replace("0",sp)
	grid2n = str(grid2)[1:-1]
	grid2n = grid2n.replace(',',' ')
	grid2n = grid2n.replace("'",'')
	grid2n = grid2n.replace("1",p1p)
	grid2n = grid2n.replace("2",p2p)
	grid2n = grid2n.replace("0",sp)
	grid1n = str(grid1)[1:-1]
	grid1n = grid1n.replace(',',' ')
	grid1n = grid1n.replace("'",'')
	grid1n = grid1n.replace("1",p1p)
	grid1n = grid1n.replace("2",p2p)
	grid1n = grid1n.replace("0",sp)
	print ("",numbers,"\n",spacer,"\n"," "+grid6n,"\n"," "+grid5n,"\n"," "+grid4n,"\n"," "+grid3n,"\n"," "+grid2n,"\n"," "+grid1n)
def CollumnCheck():
	print()
	print("Collumn filled up, please enter another number!")
	time.sleep(0.8)
	for x in range(0,24):
		print()
	conboard()
	print()
	print()
	ky == True
print("")
Rounds = 42
Playeruser1 = 1
x = True
while x is True:
	
	if Rounds != 42:
		print(Player2+" just played: "+ inputnumber)
	print("")
	ky = True
	while ky == True:
		inputnumber1 = input(Player1+", Enter a number (1 - 7): ")
		if inputnumber1 == "1":
			count1+=1
		elif inputnumber1 == "2":
			count2+=1
		elif inputnumber1 == "3":
			count3+=1
		elif inputnumber1 == "4":
			count4+=1
		elif inputnumber1 == "5":
			count5+=1
		elif inputnumber1 == "6":
			count6+=1
		elif inputnumber1 == "7":
			count7+=1
		if count1 >= 7 and inputnumber1 == "1":
			CollumnCheck()
		elif count2 >= 7 and inputnumber1 == "2":
			CollumnCheck()
		elif count3 >= 7 and inputnumber1 == "3":
			CollumnCheck()
		elif count4 >= 7 and inputnumber1 == "4":
			CollumnCheck()
		elif count5 >= 7 and inputnumber1 == "5":
			CollumCheck()
		elif count6 >= 7 and inputnumber1 == "6":
			CollumnCheck()
		elif count7 >= 7 and inputnumber1 == "7":
			CollumnCheck()
		elif inputnumber1 == "" or inputnumber1 not in numCheck:
			print()
			print("Please enter a correct number!")
			time.sleep(0.8)
			for x in range(0,24):
				print()
			conboard()
			print()
			print()
			ky = True
		else:
			ky = False
	if inputnumber1 == "1":
		if grid1[0] == 0:
			del grid1[0]
			grid1.insert(0, Playeruser1)
		elif int(grid2[0]) == 0 and int(grid3[0]) == 0:
			del grid2[0]
			grid2.insert(0, Playeruser1)
		elif int(grid3[0]) == 0 and int(grid4[0]) == 0:
			del grid3[0]
			grid3.insert(0, Playeruser1)
		elif int(grid4[0]) == 0 and int(grid5[0]) == 0:
			del grid4[0]
			grid4.insert(0, Playeruser1)
		elif int(grid5[0]) == 0 and int(grid6[0]) == 0:
			del grid5[0]
			grid5.insert(0, Playeruser1)
		elif int(grid6[0]) == 0:
			del grid6[0]
			grid6.insert(0, Playeruser1)
		
	
		
	if inputnumber1 == "2":
		if grid1[1] == 0:
			del grid1[1]
			grid1.insert(1, Playeruser1)
		elif int(grid2[1]) == 0 and int(grid3[1]) == 0:
			del grid2[1]
			grid2.insert(1, Playeruser1)
		elif int(grid3[1]) == 0 and int(grid4[1]) == 0:
			del grid3[1]
			grid3.insert(1, Playeruser1)
		elif int(grid4[1]) == 0 and int(grid5[1]) == 0:
			del grid4[1]
			grid4.insert(1, Playeruser1)
		elif int(grid5[1]) == 0 and int(grid6[1]) == 0:
			del grid5[1]
			grid5.insert(1, Playeruser1)
		elif int(grid6[1]) == 0:
			del grid6[1]
			grid6.insert(1, Playeruser1)
			
			
			
			
	if inputnumber1 == "3":
		if grid1[2] == 0:
			del grid1[2]
			grid1.insert(2, Playeruser1)
		elif int(grid2[2]) == 0 and int(grid3[2]) == 0:
			del grid2[2]
			grid2.insert(2, Playeruser1)
		elif int(grid3[2]) == 0 and int(grid4[2]) == 0:
			del grid3[2]
			grid3.insert(2, Playeruser1)
		elif int(grid4[2]) == 0 and int(grid5[2]) == 0:
			del grid4[2]
			grid4.insert(2, Playeruser1)
		elif int(grid5[2]) == 0 and int(grid6[2]) == 0:
			del grid5[2]
			grid5.insert(2, Playeruser1)
		elif int(grid6[2]) == 0:
			del grid6[2]
			grid6.insert(2, Playeruser1)
			
			
			
			
	if inputnumber1 == "4":
		if grid1[3] == 0:
			del grid1[3]
			grid1.insert(3, Playeruser1)
		elif int(grid2[3]) == 0 and int(grid3[3]) == 0:
			del grid2[3]
			grid2.insert(3, Playeruser1)
		elif int(grid3[3]) == 0 and int(grid4[3]) == 0:
			del grid3[3]
			grid3.insert(3, Playeruser1)
		elif int(grid4[3]) == 0 and int(grid5[3]) == 0:
			del grid4[3]
			grid4.insert(3, Playeruser1)
		elif int(grid5[3]) == 0 and int(grid6[3]) == 0:
			del grid5[3]
			grid5.insert(3, Playeruser1)
		elif int(grid6[3]) == 0:
			del grid6[3]
			grid6.insert(3, Playeruser1)
			
	
	if inputnumber1 == "5":
		if grid1[4] == 0:
			del grid1[4]
			grid1.insert(4, Playeruser1)
		elif int(grid2[4]) == 0 and int(grid3[4]) == 0:
			del grid2[4]
			grid2.insert(4, Playeruser1)
		elif int(grid3[4]) == 0 and int(grid4[4]) == 0:
			del grid3[4]
			grid3.insert(4, Playeruser1)
		elif int(grid4[4]) == 0 and int(grid5[4]) == 0:
			del grid4[4]
			grid4.insert(4, Playeruser1)
		elif int(grid5[4]) == 0 and int(grid6[4]) == 0:
			del grid5[4]
			grid5.insert(4, Playeruser1)
		elif int(grid6[4]) == 0:
			del grid6[4]
			grid6.insert(4, Playeruser1)
	
	
	if inputnumber1 == "6":
		if grid1[5] == 0:
			del grid1[5]
			grid1.insert(5, Playeruser1)
		elif int(grid2[5]) == 0 and int(grid3[5]) == 0:
			del grid2[5]
			grid2.insert(5, Playeruser1)
		elif int(grid3[5]) == 0 and int(grid4[5]) == 0:
			del grid3[5]
			grid3.insert(5, Playeruser1)
		elif int(grid4[5]) == 0 and int(grid5[5]) == 0:
			del grid4[5]
			grid4.insert(5, Playeruser1)
		elif int(grid5[5]) == 0 and int(grid6[5]) == 0:
			del grid5[5]
			grid5.insert(5, Playeruser1)
		elif int(grid6[5]) == 0:
			del grid6[5]
			grid6.insert(5, Playeruser1)
			
			
	if inputnumber1 == "7":
		if grid1[6] == 0:
			del grid1[6]
			grid1.insert(6, Playeruser1)
		elif int(grid2[6]) == 0 and int(grid3[6]) == 0:
			del grid2[6]
			grid2.insert(6, Playeruser1)
		elif int(grid3[6]) == 0 and int(grid4[6]) == 0:
			del grid3[6]
			grid3.insert(6, Playeruser1)
		elif int(grid4[6]) == 0 and int(grid5[6]) == 0:
			del grid4[6]
			grid4.insert(6, Playeruser1)
		elif int(grid5[6]) == 0 and int(grid6[6]) == 0:
			del grid5[6]
			grid5.insert(6, Playeruser1)
		elif int(grid6[6]) == 0:
			del grid6[6]
			grid6.insert(6, Playeruser1)
			
			
	Rounds -= 1
	time.sleep(.6)
	print("")
	print(SPACER)
	print("")
	for x in range(0,24):
		print()
	conboard()
	print("")
	if Rounds == 0:
		x = False
	
	Playeruser2 = 2
	print("")
	print(Player1+" just played: "+inputnumber1)
	print("")
	tx = True
	while tx == True:
		inputnumber = input(Player2+", Enter a number (1 - 7): ")
		if inputnumber == "1":
			count1+=1
		elif inputnumber == "2":
			count2+=1
		elif inputnumber == "3":
			count3+=1
		elif inputnumber == "4":
			count4+=1
		elif inputnumber == "5":
			count5+=1
		elif inputnumber == "6":
			count6+=1
		elif inputnumber == "7":
			count7+=1
		if count1 >= 7 and inputnumber == "1":
			CollumnCheck()
		elif count2 >= 7 and inputnumber == "2":
			CollumnCheck()
		elif count3 >= 7 and inputnumber == "3":
			CollumnCheck()
		elif count4 >= 7 and inputnumber == "4":
			CollumnCheck()
		elif count5 >= 7 and inputnumber == "5":
			CollumCheck()
		elif count6 >= 7 and inputnumber == "6":
			CollumnCheck()
		elif count7 >= 7 and inputnumber == "7":
			CollumnCheck()
		elif inputnumber == "" or inputnumber not in numCheck:
			print()
			print("Please enter a correct number!")
			time.sleep(0.8)
			for x in range(0,24):
				print()
			conboard()
			print()
			print()
			tx = True
		else:
			tx = False
	if inputnumber == "1":
		if grid1[0] == 0:
			del grid1[0]
			grid1.insert(0, Playeruser2)
		elif int(grid2[0]) == 0 and int(grid3[0]) == 0:
			del grid2[0]
			grid2.insert(0, Playeruser2)
		elif int(grid3[0]) == 0 and int(grid4[0]) == 0:
			del grid3[0]
			grid3.insert(0, Playeruser2)
		elif int(grid4[0]) == 0 and int(grid5[0]) == 0:
			del grid4[0]
			grid4.insert(0, Playeruser2)
		elif int(grid5[0]) == 0 and int(grid6[0]) == 0:
			del grid5[0]
			grid5.insert(0, Playeruser2)
		elif int(grid6[0]) == 0:
			del grid6[0]
			grid6.insert(0, Playeruser2)
	
		
	if inputnumber == "2":
		if grid1[1] == 0:
			del grid1[1]
			grid1.insert(1, Playeruser2)
		elif int(grid2[1]) == 0 and int(grid3[1]) == 0:
			del grid2[1]
			grid2.insert(1, Playeruser2)
		elif int(grid3[1]) == 0 and int(grid4[1]) == 0:
			del grid3[1]
			grid3.insert(1, Playeruser2)
		elif int(grid4[1]) == 0 and int(grid5[1]) == 0:
			del grid4[1]
			grid4.insert(1, Playeruser2)
		elif int(grid5[1]) == 0 and int(grid6[1]) == 0:
			del grid5[1]
			grid5.insert(1, Playeruser2)
		elif int(grid6[1]) == 0:
			del grid6[1]
			grid6.insert(1, Playeruser2)
			
			
			
			
	if inputnumber == "3":
		if grid1[2] == 0:
			del grid1[2]
			grid1.insert(2, Playeruser2)
		elif int(grid2[2]) == 0 and int(grid3[2]) == 0:
			del grid2[2]
			grid2.insert(2, Playeruser2)
		elif int(grid3[2]) == 0 and int(grid4[2]) == 0:
			del grid3[2]
			grid3.insert(2, Playeruser2)
		elif int(grid4[2]) == 0 and int(grid5[2]) == 0:
			del grid4[2]
			grid4.insert(2, Playeruser2)
		elif int(grid5[2]) == 0 and int(grid6[2]) == 0:
			del grid5[2]
			grid5.insert(2, Playeruser2)
		elif int(grid6[2]) == 0:
			del grid6[2]
			grid6.insert(2, Playeruser2)
			
			
			
			
	if inputnumber == "4":
		if grid1[3] == 0:
			del grid1[3]
			grid1.insert(3, Playeruser2)
		elif int(grid2[3]) == 0 and int(grid3[3]) == 0:
			del grid2[3]
			grid2.insert(3, Playeruser2)
		elif int(grid3[3]) == 0 and int(grid4[3]) == 0:
			del grid3[3]
			grid3.insert(3, Playeruser2)
		elif int(grid4[3]) == 0 and int(grid5[3]) == 0:
			del grid4[3]
			grid4.insert(3, Playeruser2)
		elif int(grid5[3]) == 0 and int(grid6[3]) == 0:
			del grid5[3]
			grid5.insert(3, Playeruser2)
		elif int(grid6[3]) == 0:
			del grid6[3]
			grid6.insert(3, Playeruser2)
			
	if inputnumber == "5":
		if grid1[4] == 0:
			del grid1[4]
			grid1.insert(4, Playeruser2)
		elif int(grid2[4]) == 0 and int(grid3[4]) == 0:
			del grid2[4]
			grid2.insert(4, Playeruser2)
		elif int(grid3[4]) == 0 and int(grid4[4]) == 0:
			del grid3[4]
			grid3.insert(4, Playeruser2)
		elif int(grid4[4]) == 0 and int(grid5[4]) == 0:
			del grid4[4]
			grid4.insert(4, Playeruser2)
		elif int(grid5[4]) == 0 and int(grid6[4]) == 0:
			del grid5[4]
			grid5.insert(4, Playeruser2)
		elif int(grid6[4]) == 0:
			del grid6[4]
			grid6.insert(4, Playeruser2)
			

	if inputnumber == "6":
		if grid1[5] == 0:
			del grid1[5]
			grid1.insert(5, Playeruser2)
		elif int(grid2[5]) == 0 and int(grid3[5]) == 0:
			del grid2[5]
			grid2.insert(5, Playeruser2)
		elif int(grid3[5]) == 0 and int(grid4[5]) == 0:
			del grid3[5]
			grid3.insert(5, Playeruser2)
		elif int(grid4[5]) == 0 and int(grid5[5]) == 0:
			del grid4[5]
			grid4.insert(5, Playeruser2)
		elif int(grid5[5]) == 0 and int(grid6[5]) == 0:
			del grid5[5]
			grid5.insert(5, Playeruser2)
		elif int(grid6[5]) == 0:
			del grid6[5]
			grid6.insert(5, Playeruser2)
			

	if inputnumber == "7":
		if grid1[6] == 0:
			del grid1[6]
			grid1.insert(6, Playeruser2)
		elif int(grid2[6]) == 0 and int(grid3[6]) == 0:
			del grid2[6]
			grid2.insert(6, Playeruser2)
		elif int(grid3[6]) == 0 and int(grid4[6]) == 0:
			del grid3[6]
			grid3.insert(6, Playeruser2)
		elif int(grid4[6]) == 0 and int(grid5[6]) == 0:
			del grid4[6]
			grid4.insert(6, Playeruser2)
		elif int(grid5[6]) == 0 and int(grid6[6]) == 0:
			del grid5[6]
			grid5.insert(6, Playeruser2)
		elif int(grid6[6]) == 0:
			del grid6[6]
			grid6.insert(6, Playeruser2)
	
	Rounds -= 1
	time.sleep(.6)
	print("")
	print(SPACER)
	print("")
	for x in range(0,24):
		print()
	conboard()
	print("")
	x = True
	if Rounds == 0:
		x = False
		
