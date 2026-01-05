########
#import modules
#######

########
#define functions
#######
#-----------                                                                                                                           ~This game is about you trying to obtain chips. You can go to different locations and get different endings. Make sure you have enough money to buy the chips. You start off with 0 dollars(global variable). Have fun. :)~





def start():
    print("Welcome to Pepe Goes to Store! 🐸 ")
    Home()




def Home():
    print("You are at home eating chips of the bag, but suddenly you realize you ran out of chips..") 
    move = input("\nWhere would you like to go to obtain EL Chips? \n\t1.Stay home\n\t2.Somewhere random\n\t3.Space\n\t4.Store\n\t")
    if move.lower() == "stay home":
        stayhome()
    elif move.lower() == "somewhere random":
        Somewhererandom()
    elif move.lower() == "space":
        Space()
    elif move.lower() == "store":
        Store()
    else:
        print("\nYou realize that you have tried to go somewhere else, but started flying up into heaven with no potato chips. :( ")
        print("☆ .‧₊˚\n╭◜◝ ͡ ◜◝╮  ㅤ ╭◜◝ ͡ ◜◝╮.\n(      )     (      )☆\n╰◟◞ ͜ ◟◞╭◜◝ ͡ ◜◝╮ ͜  ◟◞╯\n.     ☆(      )☆\n       ╰◟◞ ͜ ◟◞╯ . ☆ ")
        print("\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")


def stayhome():
    print("\nYou decided to stay home, but you still have no chips.")
    move = input("Where would you like to go?\n\t1.room1\n\t2.room2\n")
    if move.lower() == "room1":
        room1()
    elif move.lower() == "room2":
        room2()
    else:
        print("Really?")
        print("\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")


def room1():
    print("\nYou find 10 cents, but you suddenly fall asleep.")
    print("+10 🪙")
    global money
    money = money + .10
    print("\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")
    
def room2():
    print("\nYou find 4 lucky dollars in Room2.")
    print("+4 💵")
    global money
    money = money + 4
    move = input("\nWhere would you like to go?\n\t1.room3\n\t2.Store\n\t3.Kitchen\n\t4.Bathroom\n\t")
    if move.lower() == "room3":
        room3()
    elif move.lower() == "store":
        Store()
    elif move.lower() == "kitchen":
        Kitchen()
    elif move.lower() == "bathroom":
        Bathroom()
    else:
        print("\nYou got too confused and lost the game" +  "\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")


def room3():
    print("You go through the entire room and found 100 dollars")
    print("+100 💵")
    print ("\nDo you want to go to the store? Yes or No? ")
    yes = input()
    if yes.lower() in ["yes", "yea", "yeah", "ok", "okay"]:
        global money 
        money = money + 100
        Store()
    else:
        print("You go back to the couch and pretend your eating chips" + "\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")
    
def Kitchen():
    print("\nYou sit down and contemplate about how long it took you to get here, while you eat ramen noodles.")
    print("-1 🍜")
    print("\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")

def Bathroom():
    print("\nYou take a nice bubbly bath ,but when you get out its 12 am and you still have no chips.")
    print("\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")
        




def Somewhererandom():
    print("You decided to go to park ")
    move = input("\nWhat would you like to do? \n\t1.Keep walking \n\t2.Relax\n\t3.Quit the game\n\t")
    if move.lower() == "keep walking":
        Keepwalking()
    elif move.lower() == "relax":
        relax()
    elif move.lower() == "quit the game":
        Quitthegame()
    else:
        print("You can do that?" + "\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")
        

def Keepwalking():
    move = input("\nWhat would you like to do? \n\t1.Relax \n\t2.Pet a Dog\n\t3.Go to the fountain \n\t")
    if move.lower() == "relax":
        relax()
    elif move.lower() == "pet a dog":
        Petadog()
    elif move.lower() == "go to the fountain":
        Fountain()
    
def Petadog():
    print("\nA dog chases you " + "\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")
    
def Fountain():
    print("\nYou go to the fountain and steal 600 coins")
    print("+600 🪙")
    global money
    money = money + .60
    print("\nDo you want to go to the store or bank?")
    LW = input()
    if LW.lower() == "store":
        Store()
    elif LW.lower() == "bank":
        bank()
    else:
        print("\nI said store or bank. Now restart and think about your decision making.")

def bank():
    print("\nYou realized that you were beng carefully watched by the cops and get arrested before depositng money."+ "\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")



def relax():
    print("\nYou sit down on the peaceful grass and find 10 bugs")
    print("+10 🐛")
    print("\nA minute passes by and you teleport to school")
    move = input("What would you like to do? \n\t1.Go home \n\t2.Go to the vending Machine\n\t3.Go to a class\n\t")
    if move.lower() == "go home":
        Gohome()
    elif move.lower() == "go to the vending machine":
        Vendingmachine()
    elif move.lower() == "go to a class":
        Gotoclass()
    else:
        print("\nSuspended" + "\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")


def Gohome():
    print("\nYou walk back to your house and wonder why your house is gone." + "\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")

def Vendingmachine():
    print("\nSomeone comes up to you and ask you to pick a number 1-10")
    num = input("Pick a number from 1-10 ")
    if num == "7":
        print("\nThe guy gives you $3.00")
        global money
        money = money + 3
        if money >= 2.50:
            print("\nYou bought a bag of chips and before you get home you ate all of them. :(" + "\nSmall bag ending"+ "\n👝")
    else:
        print("\nYou didn't bring enough money and now you are sad and go home."+ "\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")
        
def Gotoclass():
    print("\nYou tried sneaking into a random class and got caught. " + "\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")

def Quitthegame():
    print("Goodbye" + "\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")





def Space():
    print("\nWelcome to Pepe goes to space.")
    move = input("\nWhere would you like to go to ? \n\t1.Mercury\n\t2.Venus\n\t3.Earth\n\t4.Mars\n\t5.Jupiter\n\t6.Saturn\n\t7.Uranus\n\t8.Neptune\n\t9.Sun\n\t10.Black hole\n\t11.moon\n")
    if move.lower() == "mercury":
        Mercury()
    elif move.lower() == "venus":
        Venus()
    elif move.lower() == "earth":
        Earth()
    elif move.lower() == "mars":
        Mars()
    elif move.lower() == "jupiter":
        Jupiter()
    elif move.lower() == "saturn":
        Saturn()
    elif move.lower() == "uranus":
        Uranus()
    elif move.lower() == "neptune":
        Neptune()
    elif move.lower() == "sun":
        Sun()
    elif move.lower() == "black hole":
        Blackhole()
    elif move.lower() == "moon":
        Moon()
    else:
        print("\nYou decide to go somewhere else and find alien chips." + "\n*Alien chip ending*" + "\n🦪")


def Sun():
    print("\nYou fly straight into the sun"+ " 🌞 👁👄👁")
    print("\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")

def Earth():
    print("\nYou can't seem to figure out that you live on earth and your brain explodes")
    print("\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")

def Blackhole():
    while 1 == 1:
        print("infinite time loop")
        Blackhole()

def Moon():
    print("\nYou are the first person to go to the moon." + "\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")

def Mercury():
    print("\nYou realize you are geting older." + "\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")

def Venus():
    print("\nYou start to burn." + "\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")

def Mars():
    print("\nYou enter mars")
    move = input("\nWhere would you like to go? \n\t1.Phobos\n\t2.Deimos\n")
    if move.lower() == "phobos":
        Phobos()
    elif move.lower() == "deimos":
        deimos()
    else:
        print("\nrocks hit your ship and it explodes" + "\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")


def Phobos():
        print("\nYou feel the moon going faster and it crashes into mars before you can get el chips" + "\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")
    
def deimos():
        print("You start to slip off the moon and go into space because it has no grooves and ridges." + "\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")


def Jupiter():
    print("\nYou try to visit all of Jupiter's 80 moons, but you missed one and the moon goes flying towards you and flattens you." +"\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")

def Saturn():
    print("\nYou see 12 mythical creatures with go carts and weird objects. A blue shell comes and knocks you into space." + "\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")
    
def Uranus():
    print("\nAliens kidnapped you and do tests on you.")
    move = input("\nWhat do you do? \n\t1.Fight back\n\t2.Escape\n\t3.Stay\n\t4.Leave the game\n")
    if move.lower() == "fight back":
        print("\nYou try to fight, but more aliens come out with lazer guns."+ "\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")
    elif move.lower() == "escape":
        print("\nThey bring out the alien Doge and catch you." + "\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")
    
    elif move.lower() == "stay":
        print("\nThey never stop testing on you " + "\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")

    elif move.lower() == "leave the game":
        print("\nYou bring out the dual lightsaber and kill all the aliens and their base." + "\n|anakin skywalker ending|")

    else:
        print("You become one 🛸")
    
def Neptune():
    print("You try to ice skate, but you have no chips. :C" + "\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")


        


def Store():
    print("\nYou arrive at the store")
    move = input("\nWhat aisle would you like to go? \n\t1.Aisle 1\n\t2.Aisle 2\n\t3.Aisle 3\n\t4.Aisle 4\n\t5.Check out ")
    if move.lower() == "aisle 1":
        Aisle1()
    elif move.lower() == "aisle 2":
        Aisle2()
    elif move.lower() == "aisle 3":
        Aisle3()
    elif move.lower() == "aisle 4":
        Aisle4()
    elif move.lower() == "check out":
        Checkout()
    else:
        print("\nThat is not in the store" + " \n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")


def Aisle1():
    print("You go into aisle 1. You find a coupon that has 20% off on all of the food in aisle 1.")
    move = input("\nWhat would you like to add into your cart?\n\t1.Can of beans($2.00)\n\t2.Chicken Soup($2.00)\n\t3.Canned Water($10.00)\n\t4.Go back\n\t ")
    if move.lower() == "can of beans":
        Canofbeans()
    elif move.lower() == "chicken soup":
        Chickensoup()
    elif move.lower() == "canned water":
        Cannedwater()
    elif move.lower() == "go back":
        Goback()
    else:
        a = input("that isn't in this aisle, would you like to go back? Yes or no? ")
        if a == "Yes":
            Goback()
        elif a == "yes":
            Goback()
        elif a == "no":
            Aisle1()
        elif a == "No":
            Aisle1()
        else:
            print("\n>:(" + "\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")


def Canofbeans():
    global money
    money -= 1.60
    print('With the coupon its only cost $1.60. ')
    print("You put can of bean in your cart." + "\n+ 🫘")
    storem = input("\nDo you want to go back or go to the check out? ")

    
    if storem == "check out":
        Checkout()
            
    elif storem == "back":
        Goback()

    elif storem == "Back":
        Goback()

    elif storem == "Go back":
        Goback()
    
    elif storem == "go back":
        Goback()
    else:
        print("You went back anyways")
        Goback()
    
def Chickensoup():
    global money
    money -= 1.60
    print('With the coupon its only cost $1.60. ')
    print("You put can of soup in your cart." + "\n+ 🥫")
    storem = input("\nDo you want to go back or go to the check out? ")
    
    
    if storem == "check out":
        Checkout()
            
    elif storem == "back":
        Goback()
    
    elif storem == "Back":
        Goback()

    elif storem == "Go back":
        Goback()
    
    elif storem == "go back":
        Goback()
    else:
        print("You went back anyways")
        Goback()
    
def Cannedwater():
    global money
    money -= 8
    print('With the coupon its only cost $8. ')
    print("You put can of water in your cart." + "\n+ 🌫")
    storem = input("\nDo you want to go back or go to the self check out? ")
    

    if storem == "checkout":
        Checkout()
            
    elif storem == "back":
        Goback()

    elif storem == "Back":
        Goback()

    elif storem == "Go back":
        Goback()
    
    elif storem == "go back":
        Goback()
    else:
        print("You went back anyways")
        Goback()
    




def Aisle2():
    print("\nYou go into aisle 2 and see a cat stealing money.")
    move = input("\nWhat would you like to add into your cart?\n\t1.Pasta($1.00)\n\t2.Taco shells($3.00)\n\t3.Rice($2.00)\n\t4.Go back\n\t ")
    if move.lower() == "pasta":
        Pasta()
    elif move.lower() == "taco shells":
        Tacoshells()
    elif move.lower() == "rice":
        Rice()
    elif move.lower() == "go back":
        Goback()
    else:
        a = input("that isn't in this aisle, would you like to go back? Yes or no? ")
        if a == "Yes":
            Goback()
        elif a == "yes":
            Goback()
        elif a == "no":
            Aisle2()
        elif a == "No":
            Aisle2()
        else:
            print("\n>:(" + "\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")


def Pasta():
    global money
    print("\nOh no, looks like the cat stole half of your money.")
    money -= money/2
    print("You put pasta in your cart." + "\n+ 🍝")
    storem = input("\nDo you want to go back or go to the check out? ")
    
    

    if storem == "check out":
        Checkout()
            
    elif storem == "back":
        Goback()

    elif storem == "Back":
        Goback()

    elif storem == "Go back":
        Goback()
    
    elif storem == "go back":
        Goback()
    else:
        print("You went back anyways")
        Goback()

def Tacoshells():
    global money
    print("\nOh no, looks like the cat stole half of your money.")
    money = money/2
    print("You put tacoshells in your cart." + "\n+ 🌮")
    storem = input("\nDo you want to go back or go to the check out? ")
    
    

    if storem == "check out":
            Checkout()
            
    elif storem == "back":
        Goback()
    
    elif storem == "Back":
        Goback()

    elif storem == "Go back":
        Goback()
    
    elif storem == "go back":
        Goback()
    else:
        print("You went back anyways")
        Goback()
    
def Rice():
    global money
    print("\nOh no, looks like the cat stole half of your money.")
    money = money/2
    print("You put rice in your cart." + "\n+ 🍚")
    storem = input("\nDo you want to go back or go to the check out? ")
    
    
    
    if storem == "check out":
        Checkout()
            
    elif storem == "back":
        Goback()

    elif storem == "Back":
        Goback()

    elif storem == "Go back":
        Goback()
    
    elif storem == "go back":
        Goback()
    else:
        print("You went back anyways")
        Goback()
    




def Aisle3():
    print("\nYou go into aisle 3. ")
    move = input("\nWhat would you like to add into your cart?\n\t1.Lays chips($4.00)\n\t2.Doritos($5.00)\n\t3.Cheetos($3.00)\n\t4.Go back\n\t ")
    if move.lower() == "lays chips":
        Layschips()
    elif move.lower() == "doritos":
        Doritos()
    elif move.lower() == "cheetos":
        Cheetos()
    elif move.lower() == "go back":
        Goback()
    else:
        a = input("that isn't in this aisle, would you like to go back? Yes or no? ")
        if a == "Yes":
            Goback()
        elif a == "yes":
            Goback()
        elif a == "no":
            Aisle3()
        elif a == "No":
            Aisle3()
        else:
            print("\n>:(" + "\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")


def Layschips():
    global money
    print("\nOh no, looks like the cat stole half of your money.")
    money = money/2
    global l
    l = input("\nDo you want to put these in your bag? Yes or No? ")
    if l == "Yes":
        print("You put Lay's chips in your cart." + "\n+ 🫓")
        if money >= 4:
            print("\nYou go to check out and buy the chips."  + "\nYou walk back home, take a shower, put on your pjs, turn on a movie, open up the baggy of the chips and eat them.")
            print("🏆" + "\n Lays ending"+ "\n🫓")
    elif l == "yes":
        print("You put Lay's chips in your cart." + "\n+ 🫓")
        if money >= 4:
            print("\nYou go to check out and buy the chips."  + "\nYou walk back home, take a shower, put on your pjs, turn on a movie, open up the baggy of the chips and eat them.")
            print("🏆" + "Lay's ending" + "\n🫓")

        else:
            print("\nYou go to check out and and realize you didn't bring enough money." + "\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")
    
def Doritos():
    global money
    print("\nOh no, looks like the cat stole half of your money.")
    money = money/2
    global d
    d = input("\nDo you want to put these in your bag? Yes or No? ")
    if d == "Yes":
        print("You put Doritos in your cart." + "\n+ 🔻")
        if money >= 5:
            print("\nYou go to checkout and buy the doritos." + "\nYou walk back home, take a shower, put on your pjs, turn on a movie, open up the baggy of the chips and eat them.")
            print("🏆" + "\nDorito ending" + "\n🔻")
    elif d == "yes":
        print("You put Doritos in your cart." + "\n + 🔻")
        if money >= 5:
            print("\nYou go to checkout and buy the doritos." + "\nYou walk back home, take a shower, put on your pjs, turn on a movie, open up the baggy of the chips and eat them.")
            print("🏆" + "\nDorito ending" + "\n🔻")
        else:
            print("\nYou go to check out and and realize you didn't bring enough money." + "\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")
   
def Cheetos():
    global money
    print("\nOh no, looks like the cat stole half of your money.")
    money = money/2
    global c
    c = input("\nDo you want to put these in your bag? Yes or No? ")
    if c == "Yes":
        print("You put Cheetos in your cart." + "\n+ 🥕")
        if money >= 3:
            print("\nYou go to the check out and buy the cheetos" + "\nYou walk back home, take a shower, put on your pjs, turn on a movie, open up the baggy of the chips and eat them.")
            print("🏆" + "\nCheeto ending" + "\n🥕")
    elif c == "yes":
        print("You put Cheetos in your cart." + "\n+ 🥕")
        if money >= 3:
            print("\nYou go to the check out and buy the cheetos" + "\nYou walk back home, take a shower, put on your pjs, turn on a movie, open up the baggy of the chips and eat them.")
            print("🏆" + "\nCheeto ending"+ "\n🥕")
    

        else:
            print("\nYou go to check out and and realize you didn't bring enough money." + "\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")
    else:
        Goback()

            
    

    
def Aisle4():
    print("\nYou go into aisle 4. ")
    move = input("\nWhat would you like to add into your cart?\n\t1.Milk($5.00)\n\t2.Cheese($8.00)\n\t3.Ice cream($6.00)\n\t4.Go back\n\t ")
    if move.lower() == "milk":
        Milk()
    elif move.lower() == "cheese":
        Cheese()
    elif move.lower() == "ice cream":
        Icecream()
    elif move.lower() == "go back":
        Goback()
    else:
        a = input("that isn't in this aisle, would you like to go back? Yes or no? ")
        if a == "Yes":
            Goback()
        elif a == "yes":
            Goback()
        elif a == "no":
            Aisle4()
        elif a == "No":
            Aisle4()
        else:
            print("\n>:(" + "\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")
    

def Milk():
    global money
    money = money/2
    print("You put milk in your cart." + "\n+ 🥛")
    storem = input("\nDo you want to go back or go to the check out? ")
    
    
    if storem == "check out":
            Checkout()
            
    elif storem == "back":
        Goback()
    
    elif storem == "Back":
        Goback()

    elif storem == "Go back":
        Goback()
    
    elif storem == "go back":
        Goback()
    else:
        print("You went back anyways")
        Goback()

def Cheese():
    global money
    money = money/2
    print("You put cheese in your cart." + "\n+ 🧀")
    storem = input("\nDo you want to go back or go to the check out? ")
    
    
    if storem == "check out":
            Checkout()
            
    elif storem == "back":
        Goback()

    elif storem == "Back":
        Goback()

    elif storem == "Go back":
        Goback()
    
    elif storem == "go back":
        Goback()
    else:
        print("You went back anyways")
        Goback()

def Icecream():
    global money
    money = money/2
    print("You put ice cream in your cart." + "\n+ 🍦")
    storem = input("\nDo you want to go back or go to the check out? ")
    

    if storem == "check out":
        Checkout()
            
    elif storem == "back":
        Goback()
   
    elif storem == "Back":
        Goback()

    elif storem == "Go back":
        Goback()
    
    elif storem == "go back":
        Goback()
    else:
        print("You went back anyways")
        Goback()





def Goback():
     move = input("\nWhat aisle would you like to go? \n\t1.Aisle 1\n\t2.Aisle 2\n\t3.Aisle 3\n\t4.Aisle 4\n\t5.Check out\n")
     if move.lower() == "aisle 1":
        Aisle1()
     elif move.lower() == "aisle 2":
        Aisle2()
     elif move.lower() == "aisle 3":
        Aisle3()
     elif move.lower() == "aisle 4":
        Aisle4()
     elif move.lower() == "check out":
        Checkout()

     else:
        print("That is not in the store" + " \n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")




def Checkout():
     print("\nYou go to checkout.")
     if money >= 1.60:
        print("\nYou realize that you arrived home with no chips..." +"\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")
        

     else:
        print("\nYou didn't bring enough money from home." +  "\n\n█▀▀\n█▄█\n\n▄▀█\n█▀█\n\n█▀▄▀█\n█░▀░█\n\n█▀▀\n██▄\n\n\n█▀█\n█▄█\n\n█░█\n▀▄▀\n\n█▀▀\n██▄\n\n█▀█\n█▀▄")




########
#main
#######

money = 0
start()