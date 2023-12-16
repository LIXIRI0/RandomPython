rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
ascii_art=[rock, paper, scissors]
usr_grp=["rock", "paper", "scissors"]
usr_prmpt=int(input("WHAT IS YOU CHOICE ROCK(0) PAPER(1) OR CISORS(2)\n"))
userchoice=usr_grp[usr_prmpt]
pc_grp=["rock", "paper", "scissors"]
pc_cho_indx=len(pc_grp)-1
pc_cho_num=random.randint(0,pc_cho_indx)
pc_choice=pc_grp[pc_cho_num]
usr_ascii_print= ascii_art[usr_prmpt]
pc_ascii_print= ascii_art[pc_cho_num]
if userchoice == pc_choice:
    print(f"You choose {userchoice}\n" + usr_ascii_print )
    print(f"PC choose {pc_choice}  \n" + pc_ascii_print )
    print("ITS A DRAW")
elif (userchoice == "rock" and pc_choice == "scissors") or (userchoice == "paper" and pc_choice == "rock") or (userchoice == "scissors" and pc_choice == "paper"):
    print(f"You choose {userchoice}\n" + usr_ascii_print)
    print(f"PC chooses {pc_choice}\n" + pc_ascii_print)
    print("YOU WIN!!!!!!!")
else:
    print(f"You choose {userchoice}\n" + usr_ascii_print )
    print(f"PC choose {pc_choice}  \n" + pc_ascii_print )
    print("YOU LOOSE LOOSER")