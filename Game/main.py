import random
while True:
 choise=["rock","paper","sissors"]
 computer=random.choice(choise)
 player= None
 while player not in choise:
    player=input ("rock,paper,sissors?: ").lower()
 if player==computer:
  print("computer:",computer)
  print("player:",player)
  print("The match is tye")
 elif player=="rock":
  if computer=="paper":
   print("computer:",computer)
   print("player:",player)
   print("you loss")
  if computer=="sissors":
   print("computer:",computer)
   print("player:",player)
   print("you win")
 elif player=="paper":
  if computer=="sissors":
   print("computer:",computer)
   print("player:",player)
   print("you loss")
  if computer=="rock":
   print("computer:",computer)
   print("player:",player)
   print("you win")
 elif player=="sissors":
  if computer=="rock":
   print("computer:",computer)
   print("player:",player)
   print("you loss")
  if computer=="paper":
   print("computer:",computer)
   print("player:",player)
   print("you win")
 play_again=input("play again(yes/no):").lower()
 if play_again!="yes":
  break
print("Bye!")
