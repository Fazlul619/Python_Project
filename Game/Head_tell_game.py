import random
while True:
 choice=["head","tell"]
 computer=random.choice(choice)
 player1=None
 player2=None
 while player1  not in choice:
  while player2 not in choice:
    player1=input("Enter 1st player option: ").lower()
    player2=input("Enter 2nd player optino: ").lower()
    if player1==player2:
     print("You can't do that!")
    elif player1==computer:
     print("Player1:",player1)
     print("player2:",player2)
     print("player1 win the toss!")
    elif player2==computer:
     print("Player1:",player1)
     print("player2:",player2)
     print("player2 win the toss!")
 Play_again=input("Wanna play again!(yes/no)").lower()
 if Play_again!="yes":
  break
print("Have a good day!")
  

