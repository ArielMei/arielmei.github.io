# Purpose:
# 1. Learn how to create 2 random teams from a list of players.
# 2. Learn lists and loading list data from a file

# What commands you will learn?
# 1. List: Which should be in square brackes[] with a comma between each item in the list.
# "choice(ListBame)", "ListName.append(ListItem)","ListName.remove(ListItem)", "len(ListName)"
# "file = open('filename','r')", "ListName = file.read().splitlines()"
# 2."while" loop
# 3."break" to break the loop

##----------------- Start ----------------------
#from random import choice # Get a random item from list
#
#players = ['Harry','Hermione','Neville','Ginny']
#print(players)
#
## Get an item in the list by adding its position in square brackets after the variable name.
## The first tem in the list is at position 0.
#print(players[0])
#print(players[1])
#
#print(choice(players))
#
## Create teamA and teamB
## ---------------- Step 1 -------------
#teamA = [] # create an empty list
#playerA = choice(players)
#teamA.append(playerA)     # append means add to the end
#players.remove(playerA)   # remove item from list
#print('Player left:', players)
#
#teamB = []
#playerB = choice(players)
#teamB.append(playerB)
#players.remove(playerB)
#print('Player left:', players)
##------------------------------------------

## --------------- Step 2 ------------------
## Add a while loop to keep choosing players until the length of players list is 0
#
#teamA = []
#teamB = []
#
#while len(players)>0:
#    playerA = choice(players)
#    teamA.append(playerA)     # append means add to the end
#    players.remove(playerA)   # remove item from list
#    print('Player left:', players)
#
#    playerB = choice(players)
#    teamB.append(playerB)
#    players.remove(playerB)
#    print('Player left:', players)
#
#print('TeamA:', teamA)
#print('TeamB:', teamB)
##------------------------------------------

##------------------ Step3 ---------------
# open players.txt, 'r' means read-only

#from random import choice
#
#players = []
#file = open('players.txt','r')
#players = file.read().splitlines() # "splitlines" means that every line in the file is a new item in the players list.
#print(players)
#
#teamA = []
#teamB = []
#
## If the number of items in file is odd, you will get error. Let's fix it.
#
#while len(players)>0:
#    playerA = choice(players)
#    teamA.append(playerA)
#    players.remove(playerA)
#
#    if players == []:
#        break
#
#    playerB = choice(players)
#    teamB.append(playerB)
#    players.remove(playerB)
#
#print('TeamA members are: ',teamA)
#print('TeamB members are: ',teamB)
