import random
rock = '''
    _______
---'   ____)
       (_____)
       (_____)
       (____)
---._(___)
'''
paper = '''
    _______
---'   ____)____
          ________)
          ________)
          _______)
---.__________)
'''
scissors = '''
      ____________
---'         _______)
                ______)
       _____)
      (____)
---.(___)
'''

user_point = computer_point = 0

user_name = input("Enter Your Name : ")

def printDiagram(option,name):
    if option  == 0:
        print(f"{name} Select : Rock")
        print(rock)
    elif option  == 1:
        print(f"{name} Select : Paper")
        print(paper)
    elif option == 2:
        print(f"{name} Select : Scissor")
        print(scissors)

    

gameStatus = "yes"
while gameStatus == "yes" or  gameStatus == "y"  :
    print(f"{user_name} : {user_point} VS Opponent : {computer_point}")
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors. \n"))
    computer_choice = random.randint(0,2)
    print("computer Select", computer_choice)
    if((user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0)  or (user_choice == 2 and computer_choice == 1)):
        print(f"{user_name} win this round")
        printDiagram(user_choice,user_name)
        printDiagram(computer_choice,"Oponent")
        user_point += 1
    elif((computer_choice == 0 and user_choice == 2) or (computer_choice == 1 and user_choice == 0)  or (computer_choice == 2 and user_choice == 1)):
        print("Oponent win this round")
        printDiagram(user_choice,user_name)
        printDiagram(computer_choice,"Oponent")
        computer_point += 1
    elif user_choice == computer_choice:
        print("Draw Match")
        printDiagram(user_choice,user_name)
        printDiagram(computer_choice,"Oponent")

    print(f"{user_name} : {user_point} VS Opponent : {computer_point}")
    gameStatus = input("Enter yes or just 'y' for continue or any other key for end Game ?  ")


if user_point > computer_point:
    print("You Win")
elif user_point < computer_point:
    print("You Loss")
else:
    print("Match Tie")