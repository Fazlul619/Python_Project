#---------------
def new_game():
    guesses=[]
    currect_guesses=0
    Question_Number=1
    for j in Question:
        print("#---------------")
        print(j)
        for i in Options[Question_Number-1]:
            print(i)
        guess=input("Enter your answer(A,B,C,D):")
        guess=guess.upper()
        guesses.append(guess)
        currect_guesses += check_answer(Question.get(j),guess)
        Question_Number +=1
    display_score(currect_guesses,guesses)
#---------------
def check_answer(answer,guess):
    if answer==guess:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0
    
def display_score(currect_guesses,guesses):
    print("#---------------")
    print("Results:")
    print("#---------------")
    print("Answer:",end=" ")
    for i in Question:
        print(Question.get(i),end=" ")
    print()
    print("guesses:",end=" ")
    for K in guesses:
        print(K, end=" ")
    print()
    score=int(currect_guesses/len(Question)*100)
    print ("Your score is:"+str(score)+"%")

#---------------
def play_again():
    responce=input("Do you want to play again:(YES/NO):")
    responce=responce.upper()
    if responce=="YES":
        return True
    else:
        return False

Question={
    "What is the capital of Bangladesh?":"A",
    "What is the capital of Pakistan?":"B",
    "What is the name of currency in Bangladesh?":"C",
    "What is the name  of currency in Pakistan?":"D"
    }
Options=[["A.Dhaka","B.Barisal","C.Khulna","D.Karachi"],
         ["A.Dhaka","B.Karachi","C.Khulna","D.Baraisal"],
         ["A.Rupee","B.Dinner","C.Taka","D.Doller"],
         ["A.Doller","B.Dinner","C.Taka","D.Rupee"]]
new_game()
while play_again():
    new_game()

print("Byee")
