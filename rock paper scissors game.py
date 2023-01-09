import random as anvit

print("Hello Welcome to RPS (Rock Paper Scissors) Game! \nYou will be playing against our Comp! ")
name=input("Enter Your Name : ")
print("Hello "+name)
score_comp=0
score_user=0
count=0
while True :
    print("Choose Rock(R)/Paper(P)/Scissors(S)")
    user_choice=input()
    if(user_choice=="R"):
        user_c="Rock"
        user = 1
    elif(user_choice=="P"):
        user_c="Paper"
        user = 2
    else:
        user_c="Scissors"
        user = 3

    comp = anvit.randint(1,3)
    if(comp == 1):
        comp_choice = "Rock"
    elif(comp==2):
         comp_choice = "Paper"
    else:
        comp_choice = "Scissors"

    print(f"Your Choice : {user_c}\nComp Choice : {comp_choice}")
    print(f"Dear {name} it's a ", end="")

    if comp == user :
        print("Tie")
    elif comp== 1 :
        if user== 2 :
            print("Win")
            score_user=score_user+1
        elif user== 3 :
            print("Lose")
            score_comp=score_comp+1
    elif comp== 2 :
        if user== 3 :
            print("Win")
            score_user=score_user+1
        elif user== 1 :
            print("Lose")
            score_comp=score_comp+1
    elif comp== 3 :
        if user== 1 :
            print("Win")
            score_user=score_user+1
        elif user== 2 :
            print("Lose")
            score_comp=score_comp+1
    count=count+1
    play_again = input(f"Play again? (y/n)[Count No.: {count+1}]: ")
    if play_again.lower() != "y":
        break

print(f"FINAL RESULTS : \nYour Score = {score_user},\nComputer Score = {score_comp}")
    
