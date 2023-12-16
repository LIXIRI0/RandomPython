print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("WELCOME TO YEARLY TREASURE HUNT YOU NEED TO FIND TREASURE IN ORDER TO WIN ")
choice1=input("you have come across 2 roads which road do you want to choose left or right\n LEFT-RIGHT\n").lower()
if choice1 == "right":
    print("You are walking in jungle and suddenly a lion started chasing you and ate you alive (YOU LOSE-REOPEN GAME TO PLAY AGAIN)")
elif choice1 == "left":
    choice2 = input("You walk so much and see a lake would you like to swim or wait\n WAIT-SWIM\n").lower()
    if choice2 == "swim":
        print("you tried to swim but the lake is full of poisonus jellyfishes one of them poisoned you and you drowned and poisoned (YOU LOSE-REOPEN GAME TO PLAY AGAIN)")
    elif choice2 == "wait":
        choice3 = input("You wait about 1 hour and you see a boat comes you get in the boat and get to the other side of the lake now you see 3 doors red-yellow-blue which one do you want to choose\n RED-YELLOW-BLUE\n").lower()
        if choice3 =="red":
            print("THERE IS A BIG FIRE INSIDE WHEN YOU OPEN THE DOOR IT SPREAD TO THE WHOLE FOREST AND YOU CANNOT SURVIVE FROM GASSES (YOU LOSE-REOPEN GAME TO PLAY AGAIN)")
        elif choice3 == "blue":
            print("THERE IS A BUNCH OF COBRA SNAKES WAITING YOU IN THE BLUE DOOR YOU OPENED AND ALL OF THE SNAKES BIT YOU (YOU LOSE-REOPEN GAME TO PLAY AGAIN)")
        elif choice3 == "yellow":
            print("THERE IS A SERIAL KILLER WAITING TO HUNT ANYONE WHEN YOU OPENED IT IT STABED YOU IN HEARTH AND YOU ARE DEAD")
        elif choice3 == "avoid":
            choice4 = input("You walk into the forest and see a cave in front of you there is a some noises inside do you go in or avoid and walk\n AVOID - GO IN\n")
            if choice4 == "go in":
                print("there is a bear inside waiting you he is very hungry and eats you raw (YOU LOSE-REOPEN GAME TO PLAY AGAIN) ")
            elif choice4 == "avoid":
                print("you walk a little bit and see a treasure chest between the trees you go in and you se ITS FULL OF GOLD WORTH OF $100.000.000 CONGRATS YOU WIN CONTAACT ME ON DISCORD FOR GETTING THE PRIZE")
elif choice1 == "straight":
    print("you just find an easter egg here is a coin for you")
    print('''             _.oood"""""""booo._
         _.o""   |`.  |    |   ""o._
       oP"  |`.  |  `.|    |    |  "Yo
     o8 `.  |  `.|    |.   |    |    `8o
    d'    `.|    |.   | `. |    |      `b
   d"-------*====+====+====+====+-------"b
  8'  `.    INNNNINNNNINNNNINNNNI        `8
 8      `.  INNNNINNNNINNNNINNNNI          8
,8----------+====*====+====+====+----------8.
8'  `.     `|    |`.  |gnnnnnnnn|.         `8
8     `.    |`.  |  `.|8   |.   | `.        8
8-----------+----+----*8---+----+-----------8
8        `. |   `|    |8,gnnnn:.|    `.     8
8.         `|    |`.  |8P".| "Yb|..png.`.  ,8
`8----------+----+----+----+---8+-8--`"----8'
 8          | `. |   `|n.  |`.dP| 8`. n    8
  8.        |   `|    |"YbnnndP.| `bnnP  ,8
   Y.-------+----+----+----+----+-------.P
    Y.      |    | `. |   `|    |`.    ,P
     "8.    | cg |   `|    |`.  |  `. 8"
       "Y_  | mm |  19|89  |  `.|  _P"
         `'"oo_  |    |  `.|  _oo""'
              `"""boooooood"""''')