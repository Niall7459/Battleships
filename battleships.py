import random
import time
import fixpath
import sys
from colorama import Fore, Back, Style
from subprocess import call
import colorama

colorama.init()

firstShip = []
secondShip = []
thirdShip = []
mycoordshit = []
myguesses = []
botguesses = []
botships = []

chatbox=[]
maxplace = 9
message="none"
submsg=""

def board():
    place = 1
    call(["cls"], shell=True)
    print(Style.BRIGHT + Fore.WHITE + "\n   Battleships")
    print("\n\n      | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  |      " + message)
    print("\n\n      |----|----|----|----|----|----|----|----|      ")
    for row in range(0,8):
        for i in range(0,8):
            if i == 0:
                sys.stdout.write("      |")
            if (place in firstShip) or (place in secondShip) or (place in thirdShip):  #One of my ships
                if place in mycoordshit: #My ships that have been hit
                    user = Style.BRIGHT + Fore.RED + "XX" + Fore.WHITE #HIT SHIP
                else:
                    user = Style.BRIGHT + Fore.GREEN + "XX" + Fore.WHITE #Not hit
            elif place in myguesses:
                if place in botships:
                    user = Style.BRIGHT + Fore.BLUE + "YH" + Fore.WHITE #I have hit here!
                else:
                    user = Style.BRIGHT + Fore.YELLOW + "G " + Fore.WHITE #I have guessed here
            else:
                if len(str(abs(place))) > 1:
                    user = Fore.WHITE + str(place)
                else:
                    user = Fore.WHITE + str(place) + " "
            if i <> 8:
                if place == 8:
                    sys.stdout.write(" " + user + " |      " + submsg)
                else:
                    sys.stdout.write(" " + user + " |")
            else:
                sys.stdout.write(user)
            place = place + 1
        if i != 3:
            sys.stdout.write("\n")
            print("      |----|----|----|----|----|----|----|----|")
    print("")

def drawchatbox():
    for i in chatbox:
        print("    " + i + Fore.WHITE)
    if len(chatbox) > 8:
        chatbox.pop(0)



def botShips():
    for i in range(0,6):
        coord = random.randint(1,36)
        botships.append(coord)
    chatbox.append(Fore.MAGENTA + "Bot: " + Fore.YELLOW + "Has chosen his ships!")
        

def myShips():
    #For loops for ever
    shipLoc11 = raw_input(Fore.MAGENTA + "Me: " + Fore.YELLOW + "Enter first coordinate for ship 1: ")
    shipLoc12 = raw_input(Fore.MAGENTA + "Me: " + Fore.YELLOW + "Enter second coordinate for ship 1: ")
    shipLoc21 = raw_input(Fore.MAGENTA + "Me: " + Fore.YELLOW + "Enter first coordinate for ship 2: ")
    shipLoc22 = raw_input(Fore.MAGENTA + "Me: " + Fore.YELLOW + "Enter second coordinate for ship 2: ")
    shipLoc31 = raw_input(Fore.MAGENTA + "Me: " + Fore.YELLOW + "Enter first coordinate for ship 3: ")
    shipLoc32 = raw_input(Fore.MAGENTA + "Me: " + Fore.YELLOW + "Enter second coordinate for ship 3: ")
    firstShip.append(int(shipLoc11))
    firstShip.append(int(shipLoc12))
    secondShip.append(int(shipLoc21))
    secondShip.append(int(shipLoc22))
    thirdShip.append(int(shipLoc31))
    thirdShip.append(int(shipLoc32))
    submsg = Fore.YELLOW + "Your ships have been deployed!" + Fore.WHITE
    board()

    
def AIchoose():
    validChoice = False
    while validChoice == False:
        placeChosen = random.randint(1,36)
        if placeChosen not in botguesses:
            validChoice = True
            botguesses.append(placeChosen)
            mycoordshit.append(placeChosen)
        
def choose():
    placeChosen = raw_input(Fore.MAGENTA + "    Me: " + Fore.YELLOW +  ": Enter place number to strike: " + Fore.WHITE)
    #if (int(placeChosen) in Xcoords) or (int(placeChosen) in Ocoords) :
    #    chatbox.append(Fore.RED + "This place is already taken on the game board")
    #else: #Untidy, especially with name colors but does its job at the moment
    #    if cuser==Fore.RED + "Crosses":
    #         Xcoords.append(int(placeChosen))
    #    else:
    #         Ocoords.append(int(placeChosen))
    myguesses.append(int(placeChosen))
    if int(placeChosen) in botships:
        chatbox.append(Fore.MAGENTA + "Me" + Fore.YELLOW + " You have hit Player 2's ship!")
    else:
        chatbox.append(Fore.MAGENTA + "Me" + Fore.YELLOW + " Has chosen coordinate: " + placeChosen)

def gameloop():
    board()
    drawchatbox()
    choose()
    AIchoose()
    time.sleep(0.1)

def resetGame():
    print "Resetting messages.."
    chatbox = []
    time.sleep(1)
    print "Configuring the game board."
    print "Resetting player scores..."
    time.sleep(0.5)
    print "Setting up the game board..."


print "Preparing the game..."
resetGame()
message = Fore.CYAN + "Welcome to Battleships!" + Fore.WHITE
submsg = Fore.YELLOW + "Please choose your ships!" + Fore.WHITE

time.sleep(0.1)

board()
botShips()
myShips()
board()

while True:
    scomb = []
    for ship in firstShip:
        scomb.append(ship)
    for ship in secondShip:
        scomb.append(ship)
    for ship in thirdShip:
        scomb.append(ship)

    i = 0
    for ship in scomb:
        if ship in botguesses:
            submsg = Fore.RED + "Your ship has been hit!" + Fore.WHITE
            i = i + 1
            if i == 6:
                submsg = Fore.RED + "All your ships have been sunk!" + Fore.WHITE
    if i != 6:
        gameloop()
    else:
        chatbox.append(Fore.RED + "All your ships are now sink!")
